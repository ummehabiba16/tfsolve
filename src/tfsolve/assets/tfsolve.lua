-- Pandoc filter used by `tfsolve build`.
--   ::: tfq / ::: tfsol divs  -> tcolorbox environments (title from the inner ::: tfhead div)
--   ::: tfstem / ::: tfmeta    -> shared-setup bar / small grey note
--   tables                     -> tabular or tabularx (longtable cannot live inside a box)
--   code blocks                -> fvextra Verbatim (wraps long lines)
--   ```gantt blocks            -> TikZ Gantt chart ("P1 0 30" per line, "# caption" optional)

local function to_latex(blocks)
  local s = pandoc.write(pandoc.Pandoc(blocks), 'latex')
  return (s:gsub('^%s+', ''):gsub('%s+$', ''))
end

local function raw(s)
  return pandoc.RawBlock('latex', s)
end

local function fmt(x)
  if x == math.floor(x) then return tostring(math.floor(x)) end
  return tostring(x)
end

local function tex_escape(s)
  return (s:gsub('[\\{}%%#&_%$%^~]', function(c)
    if c == '\\' then return '\\textbackslash{}' end
    if c == '^' then return '\\textasciicircum{}' end
    if c == '~' then return '\\textasciitilde{}' end
    return '\\' .. c
  end))
end

-- tables ---------------------------------------------------------------------

local function table_to_latex(tbl)
  local s = pandoc.utils.to_simple_table(tbl)
  local n = #s.aligns
  local has_head = false
  for _, c in ipairs(s.headers) do
    if #c > 0 then has_head = true end
  end
  local width = {}
  for i = 1, n do width[i] = 0 end
  local function measure(cells)
    for i, c in ipairs(cells) do
      local t = pandoc.utils.stringify(c)
      local len = utf8.len(t) or #t
      if len > width[i] then width[i] = len end
    end
  end
  if has_head then measure(s.headers) end
  for _, r in ipairs(s.rows) do measure(r) end
  local total = 0
  for i = 1, n do total = total + width[i] end

  -- Long text columns wrap (tabularx X); if the short columns alone are too wide,
  -- shrink the whole table to the line width instead.
  local fixed = 0
  for i = 1, n do
    if not (total > 80 and width[i] > 22) then fixed = fixed + width[i] end
  end
  local wrap = total > 80 and fixed <= 60
  local spec, flexible = {}, false
  for i, a in ipairs(s.aligns) do
    if wrap and width[i] > 22 then
      spec[i] = '>{\\raggedright\\arraybackslash}X'
      flexible = true
    elseif a == 'AlignRight' then spec[i] = 'r'
    elseif a == 'AlignCenter' then spec[i] = 'c'
    else spec[i] = 'l' end
  end
  local function row(cells)
    local out = {}
    for i = 1, n do out[i] = to_latex(cells[i] or {}) end
    return table.concat(out, ' & ') .. ' \\\\'
  end
  local L = {}
  if flexible then
    L[#L + 1] = '\\par\\smallskip\\noindent\\begin{tabularx}{\\linewidth}{@{}' .. table.concat(spec) .. '@{}}'
  else
    L[#L + 1] = '\\par\\smallskip\\noindent\\begin{adjustbox}{max width=\\linewidth,center}'
    L[#L + 1] = '\\begin{tabular}{@{}' .. table.concat(spec) .. '@{}}'
  end
  L[#L + 1] = '\\toprule'
  if has_head then
    L[#L + 1] = row(s.headers)
    L[#L + 1] = '\\midrule'
  end
  for _, r in ipairs(s.rows) do L[#L + 1] = row(r) end
  L[#L + 1] = '\\bottomrule'
  L[#L + 1] = flexible and '\\end{tabularx}\\par\\smallskip' or '\\end{tabular}\\end{adjustbox}\\par\\smallskip'
  local out = { raw(table.concat(L, '\n')) }
  if #s.caption > 0 then
    out[#out + 1] = pandoc.Para({ pandoc.Emph(s.caption) })
  end
  return out
end

-- code and Gantt charts -------------------------------------------------------

local function gantt(cb)
  local caption, segs = nil, {}
  for line in (cb.text .. '\n'):gmatch('(.-)\n') do
    local c = line:match('^%s*#%s*(.-)%s*$')
    if c then
      caption = c
    else
      local lbl, a, b = line:match('^%s*(%S+)%s+(%-?[%d%.]+)%s+(%-?[%d%.]+)%s*$')
      if lbl then segs[#segs + 1] = { lbl, tonumber(a), tonumber(b) } end
    end
  end
  if #segs == 0 then return nil end
  local lo, hi = segs[1][2], segs[1][3]
  for _, s in ipairs(segs) do
    lo = math.min(lo, s[2]); hi = math.max(hi, s[3])
  end
  local span = math.max(1, math.floor((hi - lo) * 100 + 0.5))
  local T = {
    '\\par\\smallskip\\noindent\\setlength{\\tfganttunit}{\\dimexpr(\\linewidth-4pt)*100/' .. span .. '\\relax}%',
    '\\begin{tikzpicture}[x=\\tfganttunit,y=0.5cm]',
  }
  for _, s in ipairs(segs) do
    local x0, x1 = s[2] - lo, s[3] - lo
    T[#T + 1] = string.format('\\draw[fill=tfq!10] (%s,0) rectangle (%s,1) node[midway,font=\\scriptsize] {%s};',
      fmt(x0), fmt(x1), tex_escape(s[1]))
    T[#T + 1] = string.format('\\node[below,font=\\tiny] at (%s,0) {%s};', fmt(x0), fmt(s[2]))
  end
  T[#T + 1] = string.format('\\node[below,font=\\tiny] at (%s,0) {%s};', fmt(hi - lo), fmt(hi))
  T[#T + 1] = '\\end{tikzpicture}\\par'
  local out = { raw(table.concat(T, '\n')) }
  if caption then
    out[#out + 1] = raw('\\tfmeta{\\itshape ' .. to_latex(pandoc.read(caption, 'markdown').blocks) .. '}')
  end
  return out
end

-- Pandoc can colour this block (```c, ```python, ...): the language is one it knows.
local function highlightable(cb)
  if #cb.classes == 0 or cb.classes:includes('text') then return false end
  return pandoc.write(pandoc.Pandoc({ cb }), 'latex'):find('\\begin{Shaded}', 1, true) ~= nil
end

local function code_block(cb)
  if cb.classes:includes('gantt') then return gantt(cb) end
  if highlightable(cb) then return nil end  -- Pandoc writes Shaded/Highlighting (macros in the template)
  return raw('\\begin{Verbatim}\n' .. cb.text .. '\n\\end{Verbatim}')
end

local inner = {
  Table = table_to_latex,
  CodeBlock = code_block,
  -- A heading inside a question or solution would break the document outline.
  Header = function(h) return pandoc.Para({ pandoc.Strong(h.content) }) end,
}

-- divs ----------------------------------------------------------------------

local function box(div, env_begin, env_end)
  local title, body = '', pandoc.Blocks({})
  for _, b in ipairs(div.content) do
    if b.t == 'Div' and b.classes:includes('tfhead') then
      title = to_latex(b.content)
    else
      body:insert(b)
    end
  end
  body = body:walk(inner)
  local label = div.identifier ~= '' and ('\\phantomsection\\label{' .. div.identifier .. '}') or ''
  local out = pandoc.Blocks({ raw(env_begin(title) .. label) })
  out:extend(body)
  out:insert(raw(env_end))
  return out
end

function Div(div)
  local c = div.classes
  if c:includes('tfq') then
    return box(div, function(t) return '\\begin{tfq}{' .. t .. '}' end, '\\end{tfq}')
  elseif c:includes('tfsol') then
    local status = div.attributes['status'] or 'unverified'
    return box(div, function(t) return '\\begin{tfsol}{tf' .. status .. '}{' .. t .. '}' end, '\\end{tfsol}')
  elseif c:includes('tfstem') then
    local out = pandoc.Blocks({ raw('\\begin{tfstem}') })
    out:extend(div.content:walk(inner))
    out:insert(raw('\\end{tfstem}'))
    return out
  elseif c:includes('tfmeta') then
    return raw('\\tfmeta{' .. to_latex(div.content) .. '}')
  end
end

-- Tables and code outside any box.
Table = table_to_latex
CodeBlock = code_block

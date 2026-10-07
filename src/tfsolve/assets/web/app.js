// tfsolve website: theme, page counts, and the course page (filters, results with paging, printing).
// A course page holds only an index; each question is fetched when shown. The address bar keeps the view
// (#show=1&topic=deadlock&p=2) so it can be bookmarked or shared.

// Light/dark: follows the device until the toggle is used; the choice is remembered per browser.
function currentTheme() {
  var set = document.documentElement.dataset.theme;
  if (set) return set;
  return window.matchMedia && matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
}

// Pandoc marks math as <span class="math inline|display">x^2</span>. Only the formulas that are on screen are
// rendered (not those inside a closed solution), so a page of questions appears quickly even on a tablet.
function renderMath(root) {
  if (!window.katex) return;
  root.querySelectorAll(".math:not([data-done])").forEach(function (el) {
    if (el.closest("details.solution:not([open])")) return;
    el.setAttribute("data-done", "1");
    var tex = el.textContent.replace(/^\\[([]|\\[)\]]$/g, "");
    try { katex.render(tex, el, { displayMode: el.classList.contains("display"), throwOnError: false }); } catch (e) {}
  });
}

document.addEventListener("DOMContentLoaded", function () {
  var toggle = document.getElementById("theme-toggle");
  if (toggle) {
    toggle.addEventListener("click", function () {
      var next = currentTheme() === "dark" ? "light" : "dark";
      document.documentElement.dataset.theme = next;
      try { localStorage.setItem("tfsolve-theme", next); } catch (e) {}
    });
  }

  // Anonymous counting with GoatCounter: page views and Print / Save PDF clicks, nothing else.
  // Nothing is sent, and no numbers are fetched, if the browser says Do Not Track / Global Privacy Control.
  var GC = "https://tfsolve.goatcounter.com";
  var noCount = navigator.doNotTrack === "1" || window.doNotTrack === "1" || navigator.globalPrivacyControl === true;
  if (!noCount) {
    var gc = document.createElement("script");
    gc.async = true;
    gc.src = "https://gc.zgo.at/count.js";
    gc.setAttribute("data-goatcounter", GC + "/count");
    document.head.appendChild(gc);

    // The About page shows the totals (GoatCounter's public counter, cached on its side for a few hours).
    var views = document.getElementById("stat-views");
    var prints = document.getElementById("stat-prints");
    var load = function (path) {
      return fetch(GC + "/counter/" + path + ".json").then(function (r) { return r.json(); })
        .then(function (d) { return d.count || "0"; });
    };
    if (views && prints && window.fetch) {
      load("TOTAL").then(function (n) { views.textContent = n; }).catch(function () { views.textContent = "n/a"; });
      load("print-pdf").then(function (n) { prints.textContent = n; }).catch(function () { prints.textContent = "n/a"; });
    }
  } else {
    ["stat-views", "stat-prints"].forEach(function (id) {
      var el = document.getElementById(id);
      if (el) el.textContent = "n/a";
    });
    var note = document.getElementById("stat-note");
    if (note) note.textContent = "Not shown: your browser asks not to be tracked, so we make no request for these numbers.";
  }
  function countEvent(name, title) {
    try {
      if (window.goatcounter && goatcounter.count) goatcounter.count({ path: name, title: title, event: true });
    } catch (e) {}
  }


  // ---------------------------------------------------------------- course page
  // The page holds only an index of the questions (id, exam, topics, teachers). Questions are fetched one file each
  // (q/<id>.html) when they are about to be shown, ten to a page, so a course opens fast and stays light.
  // Filters are applied to the index; "Show questions" fetches and displays the matches.
  var indexEl = document.getElementById("course-index");
  if (!indexEl) return; // not a course page

  var COURSE = JSON.parse(indexEl.textContent);
  var PAGE = 10;
  function $(id) { return document.getElementById(id); }

  // A multi-choice filter: a <details> holding a checklist. Nothing selected means "all".
  function picker(id) {
    var root = $(id), boxes = root.querySelectorAll("input[type=checkbox]");
    return {
      root: root,
      get: function () {
        var v = [];
        boxes.forEach(function (b) { if (b.checked) v.push(b.value); });
        return v;
      },
      set: function (list) { boxes.forEach(function (b) { b.checked = list.indexOf(b.value) !== -1; }); },
      toggle: function (v) {
        boxes.forEach(function (b) { if (b.value === v) b.checked = !b.checked; });
      }
    };
  }
  function esc(s) {
    return String(s).replace(/[&<>"]/g, function (ch) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[ch]; });
  }

  var text = $("f-text");
  var topic = picker("f-topic");
  var faculty = picker("f-faculty");
  var exam = picker("f-exam");
  var pickers = [topic, faculty, exam];
  var solved = $("f-solved");
  var openAll = $("f-open");
  var qonly = $("f-qonly");
  var showBtn = $("f-show");
  var printBtn = $("f-print");
  var overview = $("overview");
  var resultsBox = $("results");
  var list = $("results-list");
  var printArea = $("print-area");
  var arrangeButtons = document.querySelectorAll("[data-arrange]");
  var arrangement = "topic";

  // The index: topics (in course order), exams (newest first) and one record per question.
  var info = {}, topicPos = {}, roots = [], kids = {}, examInfo = {};
  COURSE.topics.forEach(function (t, i) {
    info[t.id] = t;
    topicPos[t.id] = i;
    if (t.parent) (kids[t.parent] = kids[t.parent] || []).push(t.id); else roots.push(t.id);
  });
  COURSE.exams.forEach(function (e) { examInfo[e.label] = e; });
  function rootOf(id) {
    while (info[id] && info[id].parent) id = info[id].parent;
    return id;
  }
  var Q = COURSE.q.map(function (r, i) {
    var tags = {}, who = {};
    r[3].forEach(function (t) { tags[t] = true; });
    r[4].forEach(function (w) { who[w] = true; });
    var primary = info[r[2]] ? r[2] : "";
    // sort key for "by topic": root topic, then the topic itself; untagged last
    var tk = !primary ? 1e9 : roots.indexOf(rootOf(primary)) * 1000 + (primary === rootOf(primary) ? 0 : 1 + topicPos[primary]);
    return { i: i, id: r[0], exam: r[1], primary: primary, tags: tags, who: who, solved: r[5] === 1, tk: tk };
  });

  // ---- fetching
  function get(url, as) {
    return fetch(url).then(function (r) {
      if (!r.ok) throw new Error(String(r.status));
      return as === "json" ? r.json() : r.text();
    });
  }
  function getRetry(url, as) { // one retry: a flaky tablet connection is the usual cause of a failure
    return get(url, as).catch(function () {
      return new Promise(function (ok) { setTimeout(ok, 700); }).then(function () { return get(url, as); });
    });
  }
  var cache = {};
  function fetchCards(ids, progress) { // HTML per id (null where it could not be loaded), six at a time
    var out = new Array(ids.length), next = 0, done = 0;
    function worker() {
      if (next >= ids.length) return Promise.resolve();
      var k = next++, id = ids[k];
      var p = cache[id] ? Promise.resolve(cache[id]) :
        getRetry("q/" + id + ".html?v=" + COURSE.v, "text").then(function (h) { return (cache[id] = h); })
          .catch(function () { return null; });
      return p.then(function (h) {
        out[k] = h;
        if (progress) progress(++done, ids.length);
        return worker();
      });
    }
    var pool = [];
    for (var i = 0; i < Math.min(6, ids.length); i++) pool.push(worker());
    return Promise.all(pool).then(function () { return out; });
  }

  // Search text is a separate file, fetched the first time the search box is used.
  var searchText = null, searchLoading = null, searchFailed = false;
  var NOISE = /[$`*#|\\{}\[\]()_>~]+/g; // the same characters the build strips from the searchable text
  function loadSearch() {
    if (!searchLoading) {
      searchLoading = getRetry("search.json?v=" + COURSE.v, "json").then(function (d) { searchText = d.t; })
        .catch(function () { searchFailed = true; });
    }
    return searchLoading;
  }
  function needSearch(c) { return c.text && !searchText && !searchFailed; }

  // ---- filters
  function criteria() {
    return {
      topic: topic.get(), faculty: faculty.get(), exam: exam.get(), solved: solved.checked,
      raw: text.value.trim(), text: text.value.replace(NOISE, " ").toLowerCase().split(/\s+/).join(" ").trim()
    };
  }
  function hit(list, test) { // nothing picked = no restriction; otherwise any one of the picks will do
    if (!list.length) return true;
    for (var i = 0; i < list.length; i++) if (test(list[i])) return true;
    return false;
  }
  function inTopic(q) { return function (t) { return q.tags[t]; }; }
  function inFaculty(q) { return function (w) { return q.who[w]; }; }
  function inExam(q) { return function (e) { return q.exam === e; }; }
  function others(q, c) { // the filters that are not teacher / exam / topic
    return (!c.solved || q.solved) && (!c.text || !searchText || searchText[q.i].indexOf(c.text) !== -1);
  }
  function matches(q, c) {
    return hit(c.topic, inTopic(q)) && hit(c.exam, inExam(q)) && hit(c.faculty, inFaculty(q)) && others(q, c);
  }
  // One pass: how many questions match, and, for every choice in the three lists, how many questions you would
  // get with that choice added (the other two lists still applied). Drives the numbers next to each choice.
  function tally(c) {
    var t = {}, e = {}, f = {}, total = 0;
    Q.forEach(function (q) {
      if (!others(q, c)) return;
      var okT = hit(c.topic, inTopic(q)), okE = hit(c.exam, inExam(q)), okF = hit(c.faculty, inFaculty(q));
      if (okT && okE && okF) total++;
      if (okE && okF) for (var k in q.tags) t[k] = (t[k] || 0) + 1;
      if (okT && okF) e[q.exam] = (e[q.exam] || 0) + 1;
      if (okT && okE) for (var w in q.who) f[w] = (f[w] || 0) + 1;
    });
    return { total: total, topic: t, exam: e, faculty: f };
  }
  function arranged(c) { // the matching questions in display order
    var out = Q.filter(function (q) { return matches(q, c); });
    if (arrangement === "topic") out.sort(function (a, b) { return a.tk - b.tk || a.i - b.i; });
    return out; // by year: already newest exam first
  }
  function groupOf(q) {
    if (arrangement === "year") {
      var e = examInfo[q.exam];
      return { key: q.exam, title: e ? e.title : q.exam, note: e ? e.rules : "" };
    }
    var p = q.primary;
    if (!p) return { key: "", title: "Untagged", note: "" };
    var r = rootOf(p);
    return { key: p, title: p === r ? info[p].name : info[r].name + " › " + info[p].name, note: "" };
  }
  function nameOf(field, v) {
    return field === "topic" ? (info[v] ? info[v].name : v) : field === "exam" ? (examInfo[v] ? examInfo[v].title : v) : v;
  }
  var LABEL = { topic: "Topic", exam: "Exam", faculty: "Teacher" };
  function parts(c) { // the active filters as readable chips, one per picked value
    var out = [];
    ["faculty", "exam", "topic"].forEach(function (f) {
      c[f].forEach(function (v) { out.push({ field: f, value: v, label: LABEL[f] + ": " + nameOf(f, v) }); });
    });
    if (c.solved) out.push({ field: "solved", label: "With solutions" });
    if (c.raw) out.push({ field: "text", label: "Search: \u201c" + c.raw + "\u201d" });
    return out;
  }
  function titleFor(c) { // "Results for CSE 313: Teachers: ABC, XYZ · Exams: 3 chosen · Topic: Deadlock"
    var bits = [];
    ["faculty", "exam", "topic"].forEach(function (f) {
      var v = c[f];
      if (!v.length) return;
      var names = v.map(function (x) { return nameOf(f, x); });
      bits.push(LABEL[f] + (v.length > 1 ? "s" : "") + ": " +
        (v.length <= 3 && names.join(", ").length <= 60 ? names.join(", ") : v.length + " chosen"));
    });
    if (c.solved) bits.push("with solutions");
    if (c.raw) bits.push("\u201c" + c.raw + "\u201d");
    return "Results for " + COURSE.code + ": " + (bits.length ? bits.join(" \u00b7 ") : "all questions");
  }
  function key(c) { return JSON.stringify([arrangement, c.topic, c.exam, c.faculty, c.solved, c.text]); }
  function plural(n) { return n + " question" + (n === 1 ? "" : "s"); }

  // ---- topic / exam overview: tap to pick (several allowed), then show
  function renderOverview(c, tl) {
    var body = $("overview-body"), html;
    var chosen = arrangement === "topic" ? c.topic : c.exam;
    if (arrangement === "topic") {
      var node = function (id) {
        if (!tl.topic[id] && chosen.indexOf(id) === -1) return "";
        var sub = (kids[id] || []).map(node).join("");
        return "<li><button type=\"button\" class=\"ov-btn\" data-topic=\"" + esc(id) + "\" aria-pressed=\"" +
          (chosen.indexOf(id) !== -1) + "\">" + esc(info[id].name) +
          " <span class=\"n\">" + (tl.topic[id] || 0) + "</span></button>" + (sub ? "<ul>" + sub + "</ul>" : "") + "</li>";
      };
      html = "<ul class=\"ov\">" + roots.map(node).join("") + "</ul>";
    } else {
      html = "<ul class=\"ov flat\">" + COURSE.exams.filter(function (e) {
        return tl.exam[e.label] || chosen.indexOf(e.label) !== -1;
      }).map(function (e) {
        return "<li><button type=\"button\" class=\"ov-btn\" data-exam=\"" + esc(e.label) + "\" aria-pressed=\"" +
          (chosen.indexOf(e.label) !== -1) + "\">" + esc(e.title) +
          " <span class=\"n\">" + (tl.exam[e.label] || 0) + "</span></button></li>";
      }).join("") + "</ul>";
    }
    var noun = arrangement === "topic" ? "topic" : "exam";
    $("overview-bar").hidden = !chosen.length;
    $("overview-picked").textContent = chosen.length + " " + noun + (chosen.length === 1 ? "" : "s") + " picked";
    body.innerHTML = html;
    $("overview-title").textContent = arrangement === "topic" ? "Topics" : "Exams, newest first";
    $("overview-hint").textContent = "Tap one or more " + noun + "s to pick them, then press \u201cShow\u201d. " +
      "Teachers, exams and topics can all be combined with the filters on the left.";
  }

  // ---- showing results
  var committed = null; // what the questions on screen were filtered by
  var current = [];     // those questions, in display order
  var page = 1, token = 0;

  // Each picker's button text ("All teachers", "KRV, MMI", "3 exams"), its numbers and its tick marks.
  function syncPickers(c, tl) {
    pickers.forEach(function (pk) {
      var root = pk.root, field = root.id.slice(2), picked = pk.get();
      var names = picked.map(function (v) { return nameOf(field, v); });
      var noun = root.dataset.noun, joined = names.join(", ");
      root.querySelector(".sum").textContent = !picked.length ? root.dataset.all :
        picked.length === 1 || joined.length <= 26 ? joined : picked.length + " " + noun + "s"; // one name may be cut short by CSS
      var cnt = root.querySelector(".cnt");
      cnt.hidden = !picked.length;
      cnt.textContent = picked.length;
      root.classList.toggle("has", picked.length > 0);
      root.querySelector(".hint").textContent = picked.length ? picked.length + " picked" :
        field === "topic" ? "Includes sub-topics" : "None picked = all";
      root.querySelectorAll("li[data-v]").forEach(function (li) {
        var n = tl[field][li.dataset.v] || 0;
        li.querySelector(".n").textContent = n;
        li.classList.toggle("none", !n);
      });
    });
  }

  function refresh() { // keep counts, overview and buttons in step with the controls; shows nothing new
    var c = criteria();
    if (needSearch(c)) loadSearch().then(refresh);
    var waiting = needSearch(c);
    var tl = waiting ? { total: 0, topic: {}, exam: {}, faculty: {} } : tally(c);
    var n = tl.total;
    var stale = !!committed && key(c) !== committed.key;
    arrangeButtons.forEach(function (b) { b.setAttribute("aria-pressed", String(b.dataset.arrange === arrangement)); });
    $("arrange-now").textContent = arrangement === "topic" ? "Grouped topic by topic" : "Grouped exam by exam, newest first";
    var label = waiting ? "Searching\u2026" : n === 0 ? "No questions match" :
      stale ? "Update results (" + n + ")" : "Show " + plural(n);
    showBtn.textContent = label;
    showBtn.disabled = waiting || n === 0;
    $("overview-show").textContent = label;
    $("overview-show").disabled = showBtn.disabled;
    $("f-count").textContent = waiting ? "" : n + " of " + Q.length + " questions match" +
      (searchFailed && c.text ? " (search is unavailable right now)" : "");
    $("results-stale").hidden = !stale;
    syncPickers(c, tl);
    renderOverview(c, tl);
  }

  function pagerHtml(pages) {
    var btn = function (p, label, extra) {
      return "<button type=\"button\" data-page=\"" + p + "\"" + (extra || "") + ">" + label + "</button>";
    };
    var html = btn(page - 1, "‹ Prev", page === 1 ? " disabled" : "");
    var last = 0;
    for (var p = 1; p <= pages; p++) {
      if (p !== 1 && p !== pages && Math.abs(p - page) > 1) continue;
      if (p - last > 1) html += "<span class=\"gap\">…</span>";
      html += btn(p, p, p === page ? " class=\"cur\" aria-current=\"page\"" : "");
      last = p;
    }
    return html + btn(page + 1, "Next ›", page === pages ? " disabled" : "");
  }

  function cardsHtml(qs, htmls) { // group headings between the cards, wherever the group changes
    var out = [], last = null;
    qs.forEach(function (q, k) {
      var g = groupOf(q);
      if (g.key !== last) {
        last = g.key;
        out.push("<h3 class=\"group-head\">" + esc(g.title) + "</h3>" + (g.note ? "<p class=\"note\">" + esc(g.note) + "</p>" : ""));
      }
      out.push(htmls[k] || "<article class=\"q failed\"><p>Could not load this question (" + esc(q.id) +
        "). <button type=\"button\" data-retry>Try again</button></p></article>");
    });
    return out.join("\n");
  }

  function afterInsert(root) {
    if (openAll.checked) root.querySelectorAll(".solution").forEach(function (d) { d.open = true; });
    root.querySelectorAll(".body a[href^='http'], .stem a[href^='http']").forEach(function (a) { // outside material
      a.target = "_blank";
      a.rel = "noopener";
    });
    renderMath(root);
  }

  function scrollToResults() {
    var h = $("results-title");
    var calm = window.matchMedia && matchMedia("(prefers-reduced-motion: reduce)").matches;
    h.scrollIntoView({ behavior: calm ? "auto" : "smooth", block: "start" });
    try { h.focus({ preventScroll: true }); } catch (e) {}
  }

  function writeHash(push) {
    var p = new URLSearchParams(), c = committed.c;
    p.set("show", "1");
    if (committed.arr === "year") p.set("arrange", "year");
    if (c.faculty.length) p.set("faculty", c.faculty.join(","));
    if (c.exam.length) p.set("exam", c.exam.join(","));
    if (c.topic.length) p.set("topic", c.topic.join(","));
    if (c.solved) p.set("solved", "1");
    if (c.raw) p.set("q", c.raw);
    if (page > 1) p.set("p", String(page));
    try { history[push ? "pushState" : "replaceState"](null, "", "#" + p.toString()); } catch (e) {}
  }

  // Show the questions matching the controls, page pg. opts: noScroll, replace (don't add a history entry).
  function show(pg, opts) {
    opts = opts || {};
    var c = criteria();
    if (needSearch(c)) { loadSearch().then(function () { show(pg, opts); }); return; }
    clearPrint();
    committed = { c: c, arr: arrangement, key: key(c) };
    current = arranged(c);
    var pages = Math.max(1, Math.ceil(current.length / PAGE));
    page = Math.min(Math.max(pg || 1, 1), pages);
    var slice = current.slice((page - 1) * PAGE, page * PAGE);
    var mine = ++token;

    resultsBox.hidden = false;
    overview.open = false;
    list.className = arrangement === "year" ? "arr-year" : "arr-topic";
    $("results-title").textContent = titleFor(c);
    $("results-sub").textContent = plural(current.length) + " · " +
      (arrangement === "topic" ? "grouped by topic" : "grouped by exam, newest first") +
      (pages > 1 ? " · page " + page + " of " + pages : "");
    $("results-chips").innerHTML = parts(c).map(function (x) {
      return "<button type=\"button\" class=\"active-chip\" data-field=\"" + x.field + "\" data-value=\"" +
        esc(x.value || "") + "\" title=\"Remove this filter\">" + esc(x.label) + " <span aria-hidden=\"true\">×</span></button>";
    }).join("");
    ["pager-top", "pager-bottom"].forEach(function (id) {
      $(id).hidden = pages < 2;
      $(id).innerHTML = pages < 2 ? "" : pagerHtml(pages);
    });
    $("f-empty").hidden = current.length > 0;
    writeHash(!opts.replace);
    refresh();
    if (!opts.noScroll) scrollToResults();

    if (!slice.length) { list.innerHTML = ""; return; }
    list.setAttribute("aria-busy", "true");
    list.classList.add("loading");
    if (!list.firstChild) list.innerHTML = "<p class=\"status\">Loading questions…</p>";
    fetchCards(slice.map(function (q) { return q.id; })).then(function (htmls) {
      if (mine !== token) return; // a newer request replaced this one
      list.innerHTML = cardsHtml(slice, htmls);
      list.classList.remove("loading");
      list.removeAttribute("aria-busy");
      afterInsert(list);
    });
  }

  function hideResults() {
    token++;
    committed = null;
    current = [];
    list.innerHTML = "";
    resultsBox.hidden = true;
    overview.open = true;
    clearPrint();
    refresh();
  }

  // ---- the address bar keeps what is on screen, so a view can be bookmarked or shared
  function loadHash() {
    var p = new URLSearchParams(location.hash.slice(1));
    arrangement = p.get("arrange") === "year" ? "year" : "topic";
    var list = function (name) { return (p.get(name) || "").split(",").filter(Boolean); };
    faculty.set(list("faculty"));
    exam.set(list("exam"));
    topic.set(list("topic"));
    solved.checked = p.get("solved") === "1";
    text.value = p.get("q") || "";
    var any = p.get("show") === "1" || faculty.get().length || exam.get().length || topic.get().length ||
      solved.checked || text.value;
    return { show: !!any, page: parseInt(p.get("p"), 10) || 1 };
  }
  window.addEventListener("popstate", function () {
    var h = loadHash();
    if (h.show) show(h.page, { noScroll: true, replace: true }); else hideResults();
  });

  // ---- controls
  arrangeButtons.forEach(function (b) {
    b.addEventListener("click", function () { arrangement = b.dataset.arrange; refresh(); });
  });
  pickers.forEach(function (pk) {
    pk.root.addEventListener("change", refresh);
    pk.root.addEventListener("click", function (e) {
      if (e.target.closest("[data-act=clear]")) { pk.set([]); refresh(); }
    });
    pk.root.addEventListener("toggle", function () { // opening one closes the others, so the panel stays short
      if (!pk.root.open) return;
      pickers.forEach(function (o) { if (o !== pk) o.root.open = false; });
    });
    var find = pk.root.querySelector(".pf"); // "Find a topic": hide the choices that don't contain the words
    if (find) find.addEventListener("input", function () {
      var w = find.value.toLowerCase().trim();
      pk.root.querySelectorAll("li[data-v]").forEach(function (li) {
        li.hidden = !!w && li.textContent.toLowerCase().indexOf(w) === -1;
      });
    });
  });
  solved.addEventListener("change", refresh);
  var typing = null;
  text.addEventListener("input", function () {
    clearTimeout(typing);
    typing = setTimeout(refresh, 200);
  });
  text.addEventListener("keydown", function (e) {
    if (e.key === "Enter") { clearTimeout(typing); refresh(); if (!showBtn.disabled) show(1); }
  });
  showBtn.addEventListener("click", function () { show(1); });
  $("results-update").addEventListener("click", function () { show(1); });

  $("overview-body").addEventListener("click", function (e) { // tap to pick or unpick; "Show" displays them
    var b = e.target.closest(".ov-btn");
    if (!b) return;
    var attr = b.dataset.topic ? "topic" : "exam";
    (attr === "topic" ? topic : exam).toggle(b.dataset[attr]);
    refresh();
    var again = $("overview-body").querySelector(".ov-btn[data-" + attr + "=\"" + b.dataset[attr] + "\"]");
    if (again) try { again.focus({ preventScroll: true }); } catch (err) {} // the list was redrawn: keep focus here
  });
  $("overview-show").addEventListener("click", function () { show(1); });
  $("overview-clear").addEventListener("click", function () {
    (arrangement === "topic" ? topic : exam).set([]);
    refresh();
  });
  $("results-chips").addEventListener("click", function (e) { // remove one filter and update
    var b = e.target.closest("[data-field]");
    if (!b) return;
    var f = b.dataset.field;
    if (f === "solved") solved.checked = false;
    else if (f === "text") text.value = "";
    else ({ topic: topic, exam: exam, faculty: faculty })[f].toggle(b.dataset.value);
    show(1);
  });
  [$("pager-top"), $("pager-bottom")].forEach(function (nav) {
    nav.addEventListener("click", function (e) {
      var b = e.target.closest("[data-page]");
      if (b && !b.disabled) show(parseInt(b.dataset.page, 10));
    });
  });
  list.addEventListener("click", function (e) {
    var chip = e.target.closest(".chip"); // a topic chip on a question: show that topic
    if (chip) { topic.set([chip.dataset.topic]); show(1); return; }
    if (e.target.closest("[data-retry]")) show(page, { noScroll: true, replace: true });
  });

  $("f-clear").addEventListener("click", function () {
    pickers.forEach(function (pk) { pk.set([]); });
    text.value = "";
    solved.checked = false;
    try { history.replaceState(null, "", location.pathname + location.search); } catch (e) {}
    hideResults();
  });

  openAll.addEventListener("change", function () {
    list.querySelectorAll(".solution").forEach(function (d) { d.open = openAll.checked; });
    renderMath(list);
  });
  // A solution's formulas are drawn the first time it is opened.
  document.addEventListener("toggle", function (e) {
    var d = e.target;
    if (d.open && d.classList && d.classList.contains("solution")) renderMath(d);
  }, true);

  // Hide / show the filter sidebar; the choice is remembered in this browser.
  var layout = document.querySelector(".layout");
  var collapse = $("f-collapse");
  function setFilters(hidden) {
    layout.classList.toggle("filters-hidden", hidden);
    collapse.setAttribute("aria-expanded", hidden ? "false" : "true");
    collapse.querySelector(".arrow").textContent = hidden ? "»" : "«";
    collapse.title = hidden ? "Show the filters" : "Hide the filters to give the questions the full width";
    collapse.querySelector(".txt").textContent = "Hide filters";
    if (hidden) collapse.setAttribute("aria-label", "Show filters"); else collapse.removeAttribute("aria-label");
  }
  collapse.addEventListener("click", function () {
    var hidden = !layout.classList.contains("filters-hidden");
    setFilters(hidden);
    try { localStorage.setItem("tfsolve-filters-hidden", hidden ? "1" : "0"); } catch (e) {}
  });
  try { setFilters(localStorage.getItem("tfsolve-filters-hidden") === "1"); } catch (e) {}

  // ---- printing
  // "Print / Save PDF" prints every question matching the filters (not just this page): they are fetched into a
  // hidden area, drawn with all their solutions open (unless "Questions only"), and the browser prints that.
  var printing = false;
  function clearPrint() {
    printArea.innerHTML = "";
    document.documentElement.classList.remove("printing-all", "print-questions-only");
  }
  function imagesReady(root) { // lazy figures would otherwise be missing from the paper
    var all = Array.prototype.map.call(root.querySelectorAll("img"), function (img) {
      img.loading = "eager";
      return img.complete ? Promise.resolve() : new Promise(function (ok) { img.onload = img.onerror = ok; });
    });
    return Promise.race([Promise.all(all), new Promise(function (ok) { setTimeout(ok, 10000); })]);
  }
  function printAll() {
    if (printing) return;
    var c = criteria();
    if (needSearch(c)) { loadSearch().then(printAll); return; }
    var qs = arranged(c);
    if (!qs.length) return;
    printing = true;
    clearPrint();
    var label = printBtn.textContent;
    printBtn.disabled = true;
    fetchCards(qs.map(function (q) { return q.id; }), function (done, n) {
      printBtn.textContent = "Preparing " + done + " of " + n + "…";
    }).then(function (htmls) {
      var order = [], per = {};
      qs.forEach(function (q) {
        var g = groupOf(q);
        if (!per[g.key]) { per[g.key] = 0; order.push(g); }
        per[g.key]++;
      });
      printArea.innerHTML = "<h1 class=\"print-title\">" + esc(titleFor(c)) + "</h1>" +
        "<p class=\"muted\">" + plural(qs.length) + "</p>" +
        "<nav class=\"contents\"><h2>Contents: " + (arrangement === "topic" ? "topic by topic" : "exam by exam") + "</h2><ol>" +
        order.map(function (g) { return "<li>" + esc(g.title) + " <span class=\"n\">" + per[g.key] + "</span></li>"; }).join("") +
        "</ol></nav>" + cardsHtml(qs, htmls);
      printArea.querySelectorAll("[id]").forEach(function (el) { el.removeAttribute("id"); });
      if (!qonly.checked) printArea.querySelectorAll(".solution").forEach(function (d) { d.open = true; });
      renderMath(printArea);
      return imagesReady(printArea);
    }).then(function () {
      document.documentElement.classList.add("printing-all");
      document.documentElement.classList.toggle("print-questions-only", qonly.checked);
      countEvent("print-pdf", "Print / Save PDF");
      window.print();
    }).catch(function () {
      clearPrint();
    }).then(function () {
      printing = false;
      printBtn.disabled = false;
      printBtn.textContent = label;
    });
  }
  printBtn.addEventListener("click", printAll);

  // Ctrl/Cmd+P on the screen as it is: open the solutions of the shown page for the print job, then close them again.
  var reopen = null;
  window.addEventListener("beforeprint", function () {
    if (reopen || document.documentElement.classList.contains("printing-all")) return;
    reopen = [];
    document.documentElement.classList.toggle("print-questions-only", qonly.checked);
    if (qonly.checked) return;
    list.querySelectorAll(".solution").forEach(function (d) { if (!d.open) { d.open = true; reopen.push(d); } });
    renderMath(list);
  });
  window.addEventListener("afterprint", function () {
    if (reopen) reopen.forEach(function (d) { d.open = false; });
    reopen = null;
    clearPrint();
  });

  var start = loadHash();
  refresh();
  if (start.show) show(start.page, { noScroll: true, replace: true });
});

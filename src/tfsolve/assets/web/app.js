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
  function esc(s) {
    return String(s).replace(/[&<>"]/g, function (ch) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[ch]; });
  }

  var text = $("f-text");
  var topic = $("f-topic");
  var faculty = $("f-faculty");
  var exam = $("f-exam");
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
      topic: topic.value, faculty: faculty.value, exam: exam.value, solved: solved.checked,
      raw: text.value.trim(), text: text.value.replace(NOISE, " ").toLowerCase().split(/\s+/).join(" ").trim()
    };
  }
  function matches(q, c, skip) { // skip: ignore the topic or exam filter (to count what choosing it would show)
    return (skip === "topic" || !c.topic || q.tags[c.topic]) &&
      (skip === "exam" || !c.exam || q.exam === c.exam) &&
      (!c.faculty || q.who[c.faculty]) &&
      (!c.solved || q.solved) &&
      (!c.text || !searchText || searchText[q.i].indexOf(c.text) !== -1);
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
  function parts(c) { // the active filters as readable pieces
    var out = [];
    if (c.topic) out.push({ clear: "topic", label: "Topic: " + (info[c.topic] ? info[c.topic].name : c.topic) });
    if (c.exam) out.push({ clear: "exam", label: "Exam: " + (examInfo[c.exam] ? examInfo[c.exam].title : c.exam) });
    if (c.faculty) out.push({ clear: "faculty", label: "Teacher: " + c.faculty });
    if (c.solved) out.push({ clear: "solved", label: "With solutions" });
    if (c.raw) out.push({ clear: "text", label: "Search: “" + c.raw + "”" });
    return out;
  }
  function titleFor(c) {
    var p = parts(c).map(function (x) { return x.label; });
    return "Results for " + COURSE.code + ": " + (p.length ? p.join(" · ") : "all questions");
  }
  function key(c) { return JSON.stringify([arrangement, c.topic, c.exam, c.faculty, c.solved, c.text]); }
  function plural(n) { return n + " question" + (n === 1 ? "" : "s"); }

  // ---- topic / exam overview: tap one to see its questions
  function renderOverview(c) {
    var body = $("overview-body"), html;
    if (arrangement === "topic") {
      var counts = {};
      Q.forEach(function (q) {
        if (!matches(q, c, "topic")) return;
        for (var t in q.tags) counts[t] = (counts[t] || 0) + 1;
      });
      var node = function (id) {
        if (!counts[id]) return "";
        var sub = (kids[id] || []).map(node).join("");
        return "<li><button type=\"button\" class=\"ov-btn\" data-topic=\"" + esc(id) + "\"" +
          (c.topic === id ? " aria-pressed=\"true\"" : "") + ">" + esc(info[id].name) +
          " <span class=\"n\">" + counts[id] + "</span></button>" + (sub ? "<ul>" + sub + "</ul>" : "") + "</li>";
      };
      html = "<ul class=\"ov\">" + roots.map(node).join("") + "</ul>";
    } else {
      var per = {};
      Q.forEach(function (q) { if (matches(q, c, "exam")) per[q.exam] = (per[q.exam] || 0) + 1; });
      html = "<ul class=\"ov flat\">" + COURSE.exams.filter(function (e) { return per[e.label]; }).map(function (e) {
        return "<li><button type=\"button\" class=\"ov-btn\" data-exam=\"" + esc(e.label) + "\"" +
          (c.exam === e.label ? " aria-pressed=\"true\"" : "") + ">" + esc(e.title) +
          " <span class=\"n\">" + per[e.label] + "</span></button></li>";
      }).join("") + "</ul>";
    }
    body.innerHTML = html;
    $("overview-title").textContent = arrangement === "topic" ? "Topics" : "Exams, newest first";
    $("overview-hint").textContent = "Tap one to see its questions. To combine filters, set them on the left and press " +
      "“Show questions”.";
  }

  // ---- showing results
  var committed = null; // what the questions on screen were filtered by
  var current = [];     // those questions, in display order
  var page = 1, token = 0;

  function refresh() { // keep counts, overview and buttons in step with the controls; shows nothing new
    var c = criteria();
    if (needSearch(c)) loadSearch().then(refresh);
    var waiting = needSearch(c);
    var n = waiting ? 0 : Q.filter(function (q) { return matches(q, c); }).length;
    var stale = !!committed && key(c) !== committed.key;
    arrangeButtons.forEach(function (b) { b.setAttribute("aria-pressed", String(b.dataset.arrange === arrangement)); });
    $("arrange-now").textContent = arrangement === "topic" ? "Grouped topic by topic" : "Grouped exam by exam, newest first";
    showBtn.textContent = waiting ? "Searching…" : n === 0 ? "No questions match" :
      stale ? "Update results (" + n + ")" : "Show " + plural(n);
    showBtn.disabled = waiting || n === 0;
    $("f-count").textContent = waiting ? "" : n + " of " + Q.length + " questions match" +
      (searchFailed && c.text ? " (search is unavailable right now)" : "");
    $("results-stale").hidden = !stale;
    renderOverview(c);
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
    if (c.faculty) p.set("faculty", c.faculty);
    if (c.exam) p.set("exam", c.exam);
    if (c.topic) p.set("topic", c.topic);
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
      return "<button type=\"button\" class=\"active-chip\" data-clear=\"" + x.clear + "\" title=\"Remove this filter\">" +
        esc(x.label) + " <span aria-hidden=\"true\">×</span></button>";
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
    faculty.value = p.get("faculty") || "";
    exam.value = p.get("exam") || "";
    topic.value = p.get("topic") || "";
    solved.checked = p.get("solved") === "1";
    text.value = p.get("q") || "";
    var any = p.get("show") === "1" || faculty.value || exam.value || topic.value || solved.checked || text.value;
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
  [topic, faculty, exam, solved].forEach(function (el) { el.addEventListener("change", refresh); });
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

  $("overview-body").addEventListener("click", function (e) { // tapping a topic or exam shows it straight away
    var b = e.target.closest(".ov-btn");
    if (!b) return;
    if (b.dataset.topic) topic.value = b.dataset.topic;
    if (b.dataset.exam) exam.value = b.dataset.exam;
    show(1);
  });
  $("results-chips").addEventListener("click", function (e) { // remove one filter and update
    var b = e.target.closest("[data-clear]");
    if (!b) return;
    var what = b.dataset.clear;
    if (what === "solved") solved.checked = false; else ({ topic: topic, exam: exam, faculty: faculty, text: text })[what].value = "";
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
    if (chip) { topic.value = chip.dataset.topic; show(1); return; }
    if (e.target.closest("[data-retry]")) show(page, { noScroll: true, replace: true });
  });

  $("f-clear").addEventListener("click", function () {
    topic.value = faculty.value = exam.value = text.value = "";
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

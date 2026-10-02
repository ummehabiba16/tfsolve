// tfsolve website: math rendering and the filters on a course page.
// Filters are kept in the URL (#topic=deadlock&faculty=KRV) so a filtered view can be shared.

// Light/dark: follows the device until the toggle is used; the choice is remembered per browser.
function currentTheme() {
  var set = document.documentElement.dataset.theme;
  if (set) return set;
  return window.matchMedia && matchMedia("(prefers-color-scheme: dark)").matches ? "dark" : "light";
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

  // Pandoc marks math as <span class="math inline|display">x^2</span>.
  if (window.katex) {
    document.querySelectorAll(".math").forEach(function (el) {
      var tex = el.textContent.replace(/^\\[([]|\\[)\]]$/g, "");
      katex.render(tex, el, { displayMode: el.classList.contains("display"), throwOnError: false });
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

  var text = document.getElementById("f-text");
  if (!text) return; // not a course page

  var topic = document.getElementById("f-topic");
  var faculty = document.getElementById("f-faculty");
  var exam = document.getElementById("f-exam");
  var solved = document.getElementById("f-solved");
  var openAll = document.getElementById("f-open");
  var byYear = document.getElementById("by-year");
  var byTopic = document.getElementById("by-topic");
  var toc = document.getElementById("toc");
  var arrangeButtons = document.querySelectorAll("[data-arrange]");
  var arrangement = "topic";

  function has(list, word) {
    return (" " + list + " ").indexOf(" " + word + " ") !== -1;
  }

  // "By topic": a second copy of every question card, grouped under its first topic.
  // The page itself is laid out by exam, which is also what you get without JavaScript.
  var tree = JSON.parse(document.getElementById("topic-tree").textContent);
  var info = {};
  tree.forEach(function (t) { info[t.id] = t; });
  function rootOf(id) {
    while (info[id] && info[id].parent) id = info[id].parent;
    return id;
  }
  (function buildTopicView() {
    var cards = byYear.querySelectorAll(".q");
    var buckets = {};
    cards.forEach(function (q) {
      var p = info[q.dataset.primary] ? q.dataset.primary : "";
      (buckets[p] = buckets[p] || []).push(q);
    });
    function heading(tag, id, name) {
      var h = document.createElement(tag);
      h.id = "t-" + (id || "untagged");
      h.textContent = name;
      return h;
    }
    function addCards(box, list) {
      list.forEach(function (q) {
        var c = q.cloneNode(true);
        c.querySelectorAll("[id]").forEach(function (el) { el.removeAttribute("id"); });
        c.id = "t-" + q.id;
        box.appendChild(c);
      });
    }
    tree.filter(function (t) { return !t.parent; }).concat([{ id: "", name: "Untagged" }]).forEach(function (root) {
      var section = document.createElement("section");
      section.className = "group";
      section.appendChild(heading("h2", root.id, root.name));
      if (buckets[root.id]) addCards(section, buckets[root.id]);
      tree.forEach(function (t) {
        if (!t.parent || rootOf(t.id) !== root.id || !buckets[t.id]) return;
        var sub = document.createElement("div");
        sub.className = "sub";
        sub.appendChild(heading("h3", t.id, t.name));
        addCards(sub, buckets[t.id]);
        section.appendChild(sub);
      });
      if (section.querySelector(".q")) byTopic.appendChild(section);
    });
  })();
  var questions = document.querySelectorAll(".q");

  function teachers() {
    return faculty.value ? [faculty.value] : [];
  }

  function link(target, label, n) {
    var li = document.createElement("li");
    var a = document.createElement("a");
    a.href = "#" + target.id;
    a.textContent = label;
    a.addEventListener("click", function (e) {
      e.preventDefault();
      target.scrollIntoView({ behavior: "smooth" });
    });
    var count = document.createElement("span");
    count.className = "n";
    count.textContent = n;
    li.appendChild(a);
    li.appendChild(count);
    return li;
  }

  // Contents: the groups of the current arrangement that still have visible questions.
  function buildContents() {
    toc.innerHTML = "";
    var view = arrangement === "topic" ? byTopic : byYear;
    document.getElementById("contents-title").textContent =
      arrangement === "topic" ? "Contents: topic by topic" : "Contents: exam by exam";
    view.querySelectorAll(".group").forEach(function (g) {
      var n = g.querySelectorAll(".q:not([hidden])").length;
      if (!n) return;
      var h = g.querySelector("h2");
      var li = link(h, h.textContent, n);
      var subs = g.querySelectorAll(".sub");
      if (subs.length) {
        var ol = document.createElement("ol");
        subs.forEach(function (sub) {
          var k = sub.querySelectorAll(".q:not([hidden])").length;
          if (k) ol.appendChild(link(sub.querySelector("h3"), sub.querySelector("h3").textContent, k));
        });
        li.appendChild(ol);
      }
      toc.appendChild(li);
    });
  }

  function apply() {
    var words = text.value.toLowerCase().trim();
    var who = teachers();
    var shown = 0;
    questions.forEach(function (q) {
      var ok =
        (!topic.value || has(q.dataset.topics, topic.value)) &&
        (!who.length || who.some(function (w) { return has(q.dataset.faculty, w); })) &&
        (!exam.value || q.dataset.exam === exam.value) &&
        (!solved.checked || q.dataset.solved === "yes") &&
        (!words || q.textContent.toLowerCase().indexOf(words) !== -1);
      q.hidden = !ok;
      if (ok && byYear.contains(q)) shown++;
    });
    document.querySelectorAll(".group, .sub").forEach(function (g) {
      g.hidden = !g.querySelector(".q:not([hidden])");
    });
    byYear.hidden = arrangement !== "year";
    byTopic.hidden = arrangement !== "topic";
    arrangeButtons.forEach(function (b) { b.setAttribute("aria-pressed", String(b.dataset.arrange === arrangement)); });
    document.getElementById("arrange-now").textContent =
      arrangement === "topic" ? "Grouped topic by topic" : "Grouped exam by exam, newest first";
    buildContents();
    document.getElementById("f-count").textContent =
      shown + " of " + byYear.querySelectorAll(".q").length + " questions";
    document.getElementById("f-empty").hidden = shown > 0;
    saveHash();
  }

  function saveHash() {
    var p = new URLSearchParams();
    if (arrangement !== "topic") p.set("arrange", arrangement);
    if (faculty.value) p.set("faculty", faculty.value);
    if (exam.value) p.set("exam", exam.value);
    if (topic.value) p.set("topic", topic.value);
    if (solved.checked) p.set("solved", "1");
    if (text.value) p.set("q", text.value);
    history.replaceState(null, "", p.toString() ? "#" + p.toString() : location.pathname);
  }

  function loadHash() {
    var p = new URLSearchParams(location.hash.slice(1));
    arrangement = p.get("arrange") === "year" ? "year" : "topic";
    faculty.value = p.get("faculty") || "";
    exam.value = p.get("exam") || "";
    topic.value = p.get("topic") || "";
    solved.checked = p.get("solved") === "1";
    text.value = p.get("q") || "";
  }

  arrangeButtons.forEach(function (b) {
    b.addEventListener("click", function () {
      arrangement = b.dataset.arrange;
      apply();
    });
  });
  [topic, faculty, exam, solved].forEach(function (el) { el.addEventListener("change", apply); });
  text.addEventListener("input", apply);

  openAll.addEventListener("change", function () {
    document.querySelectorAll(".solution").forEach(function (d) { d.open = openAll.checked; });
  });

  // Clicking a topic chip on a question filters by that topic.
  document.querySelectorAll(".chip").forEach(function (chip) {
    chip.addEventListener("click", function () {
      topic.value = chip.dataset.topic;
      apply();
      window.scrollTo({ top: 0, behavior: "smooth" });
    });
  });

  document.getElementById("f-clear").addEventListener("click", function () {
    topic.value = faculty.value = exam.value = text.value = "";
    solved.checked = false;
    apply();
  });

  // Printing includes the solutions unless "Questions only when printing" is ticked. Closed <details> print as
  // just their heading, so open every one for the print job (also for Ctrl/Cmd+P) and close them afterwards.
  var reopen = null;
  var qonly = document.getElementById("f-qonly");
  function openForPrint() {
    if (reopen) return;
    reopen = [];
    document.documentElement.classList.toggle("print-questions-only", qonly.checked);
    if (qonly.checked) return;
    document.querySelectorAll(".solution").forEach(function (d) {
      if (!d.open) { d.open = true; reopen.push(d); }
    });
  }
  function restoreAfterPrint() {
    if (!reopen) return;
    reopen.forEach(function (d) { d.open = false; });
    reopen = null;
    document.documentElement.classList.remove("print-questions-only");
  }
  window.addEventListener("beforeprint", openForPrint);
  window.addEventListener("afterprint", restoreAfterPrint);

  document.getElementById("f-print").addEventListener("click", function () {
    if (!noCount) countEvent("print-pdf", "Print / Save PDF");
    openForPrint();
    window.print();
    // Some browsers don't fire afterprint reliably; print() blocks until the dialog closes in most, so restore here too.
    setTimeout(restoreAfterPrint, 500);
  });

  loadHash();
  apply();
});

// tfsolve website: math rendering and the filters on a course page.
// Filters are kept in the URL (#topic=deadlock&faculty=KRV) so a filtered view can be shared.

document.addEventListener("DOMContentLoaded", function () {
  // Pandoc marks math as <span class="math inline|display">x^2</span>.
  if (window.katex) {
    document.querySelectorAll(".math").forEach(function (el) {
      var tex = el.textContent.replace(/^\\[([]|\\[)\]]$/g, "");
      katex.render(tex, el, { displayMode: el.classList.contains("display"), throwOnError: false });
    });
  }

  var text = document.getElementById("f-text");
  if (!text) return; // not a course page

  var topic = document.getElementById("f-topic");
  var faculty = document.getElementById("f-faculty");
  var exam = document.getElementById("f-exam");
  var solved = document.getElementById("f-solved");
  var openAll = document.getElementById("f-open");
  var questions = document.querySelectorAll(".q");
  var exams = document.querySelectorAll(".exam");

  function has(list, word) {
    return (" " + list + " ").indexOf(" " + word + " ") !== -1;
  }

  function teachers() {
    if (!faculty.value) return [];
    if (faculty.value === "current") return faculty.selectedOptions[0].dataset.list.split(" ");
    return [faculty.value];
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
      if (ok) shown++;
    });
    exams.forEach(function (e) {
      e.hidden = !e.querySelector(".q:not([hidden])");
    });
    document.getElementById("f-count").textContent =
      shown + " of " + questions.length + " questions";
    document.getElementById("f-empty").hidden = shown > 0;
    saveHash();
  }

  function saveHash() {
    var p = new URLSearchParams();
    if (topic.value) p.set("topic", topic.value);
    if (faculty.value) p.set("faculty", faculty.value);
    if (exam.value) p.set("exam", exam.value);
    if (solved.checked) p.set("solved", "1");
    if (text.value) p.set("q", text.value);
    history.replaceState(null, "", p.toString() ? "#" + p.toString() : location.pathname);
  }

  function loadHash() {
    var p = new URLSearchParams(location.hash.slice(1));
    topic.value = p.get("topic") || "";
    faculty.value = p.get("faculty") || "";
    exam.value = p.get("exam") || "";
    solved.checked = p.get("solved") === "1";
    text.value = p.get("q") || "";
  }

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

  document.getElementById("f-print").addEventListener("click", function () { window.print(); });

  loadHash();
  apply();
});

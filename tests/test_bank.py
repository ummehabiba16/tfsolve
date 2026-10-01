"""Smoke tests over the real bank. Run: pytest"""
import shutil
from pathlib import Path

import pytest

from tfsolve.bank import Bank, is_under, norm_session
from tfsolve.cli import main
from tfsolve.lint import lint
from tfsolve.query import QueryError, select

BANK = Path(__file__).resolve().parents[1] / "bank"


@pytest.fixture(scope="module")
def bank():
    return Bank(BANK)


def test_bank_is_clean(bank):
    assert [i for i in lint(bank) if i.level == "error"] == []


def test_part_hierarchy():
    assert is_under("q7a-ii", "q7a") and is_under("q7a-ii", "q7") and is_under("q7a", "q7")
    assert not is_under("q10a", "q1") and not is_under("q7a-ii", "q7a-i")


def test_session_forms():
    assert norm_session("2019-2020") == norm_session("2019-20") == "2019-20"
    assert norm_session("2019") is None


def test_topic_alias_and_faculty(bank):
    sel = select(bank, "cse 313", topics=["pagetable"], faculty=["krv"])
    assert sel.topics == ["paging"] and sel.faculty == ["KRV"]
    assert sel.parts and all("KRV" in bank.setters(p)[0] for p in sel.parts)


def test_current_faculty(bank):
    sel = select(bank, "CSE313", faculty=["current"])
    assert sel.current and set(sel.faculty) == set(bank.current_faculty(sel.course))


def test_unknown_topic_suggests(bank):
    with pytest.raises(QueryError, match="Did you mean"):
        select(bank, "CSE313", topics=["pagetabel"])


def test_tex_output_without_latex(tmp_path, monkeypatch):
    # Works on any OS without LaTeX: only Pandoc (bundled) is needed for --tex.
    monkeypatch.setattr(shutil, "which", lambda name, *a, **k: None)
    out = tmp_path / "x.pdf"
    assert main(["--bank", str(BANK), "-c", "CSE313", "-t", "raid", "--tex", "-o", str(out)]) == 0
    tex = out.with_suffix(".tex").read_text(encoding="utf-8")
    assert "\\begin{tfq}" in tex and "RAID" in tex


def test_website(tmp_path):
    out = tmp_path / "site"
    assert main(["web", "--bank", str(BANK), "-o", str(out)]) == 0
    home = (out / "index.html").read_text(encoding="utf-8")
    page = (out / "CSE313" / "index.html").read_text(encoding="utf-8")
    assert 'href="CSE313/index.html"' in home
    assert 'class="q"' in page and 'class="gantt"' in page and 'class="math inline"' in page
    assert "TFSPLIT" not in page and (out / "style.css").exists() and (out / "app.js").exists()

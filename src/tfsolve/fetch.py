"""Reader mode: download the question bank so `pip install tfsolve` works outside a clone."""
from __future__ import annotations

import io
import os
import shutil
import ssl
import sys
import tempfile
import urllib.request
import zipfile
from pathlib import Path

DEFAULT_REPO = "https://github.com/ummehabiba16/tfsolve"


def data_dir():
    """Per-user data folder: %LOCALAPPDATA%\\tfsolve, ~/Library/Application Support/tfsolve or ~/.local/share/tfsolve."""
    if os.environ.get("TFSOLVE_HOME"):
        return Path(os.environ["TFSOLVE_HOME"])
    if sys.platform == "win32":
        base = Path(os.environ.get("LOCALAPPDATA") or Path.home() / "AppData" / "Local")
    elif sys.platform == "darwin":
        base = Path.home() / "Library" / "Application Support"
    else:
        base = Path(os.environ.get("XDG_DATA_HOME") or Path.home() / ".local" / "share")
    return base / "tfsolve"


def downloaded_bank():
    b = data_dir() / "bank"
    return b if b.is_dir() and any(b.glob("*/dept.yaml")) else None


def _ssl_context():
    """Trust store from `certifi`, so downloads work even where Python has no CA certificates
    (python.org installers on macOS until "Install Certificates.command" is run)."""
    try:
        import certifi
        return ssl.create_default_context(cafile=certifi.where())
    except ImportError:
        return ssl.create_default_context()


def archive_url(repo, branch):
    if repo.endswith(".zip") or repo.startswith("file:"):
        return repo
    return f"{repo.rstrip('/')}/archive/refs/heads/{branch}.zip"


def update(repo=None, branch="main"):
    """Download the repository zip and replace the local copy of bank/. Returns (path, number of files)."""
    url = archive_url(repo or os.environ.get("TFSOLVE_REPO") or DEFAULT_REPO, branch)
    req = urllib.request.Request(url, headers={"User-Agent": "tfsolve"})
    with urllib.request.urlopen(req, timeout=60, context=_ssl_context()) as r:
        data = r.read()
    with zipfile.ZipFile(io.BytesIO(data)) as z:
        names = [n for n in z.namelist() if "/bank/" in n and not n.endswith("/")]
        if not names:
            raise RuntimeError(f"{url} has no bank/ folder")
        target = data_dir()
        target.mkdir(parents=True, exist_ok=True)
        with tempfile.TemporaryDirectory(dir=target) as tmp:
            for n in names:
                rel = n.split("/bank/", 1)[1]
                if ".." in Path(rel).parts:
                    continue
                dst = Path(tmp) / "bank" / rel
                dst.parent.mkdir(parents=True, exist_ok=True)
                dst.write_bytes(z.read(n))
            shutil.rmtree(target / "bank", ignore_errors=True)
            shutil.move(str(Path(tmp) / "bank"), str(target / "bank"))
    (target / "SOURCE").write_text(url + "\n", encoding="utf-8")
    return target / "bank", len(names)

"""Modal download entry for seedvr2.

Run:
  modal run download.py::download

Requires Modal secret `huggingface` (HF_TOKEN). Self-contained: no local imports.
"""

from __future__ import annotations

import json
import os
from pathlib import Path
from typing import Any

import modal



_cfg: dict[str, Any] = {}
_sh = _cfg.get("seedvrHf") if isinstance(_cfg.get("seedvrHf"), dict) else {}

HF_REPO_3B = str(_sh.get("repo3b") or "ByteDance-Seed/SeedVR2-3B")
HF_REPO_7B = str(_sh.get("repo7b") or "ByteDance-Seed/SeedVR2-7B")

volume_name = str(_cfg.get("volumeName") or "models")
volume = modal.Volume.from_name(volume_name, create_if_missing=True)
model_downloader = modal.App("model_downloader")


@model_downloader.function(
    image=modal.Image.debian_slim(python_version="3.12")
    .pip_install("huggingface_hub>=0.34.0,<1.0"),
    volumes={"/models": volume},
    timeout=7200,
    secrets=[modal.Secret.from_dict({"HF_TOKEN": os.environ.get("HF_TOKEN", "")})],
)
def _download() -> None:
    from huggingface_hub import snapshot_download

    token = os.environ.get("HF_TOKEN") or None
    patterns = ["*.pth", "*.pt", "*.json", "*.md", "*.txt"]
    for repo_id in (HF_REPO_3B, HF_REPO_7B):
        local_dir = f"/models/{repo_id}"
        os.makedirs(local_dir, exist_ok=True)
        snapshot_download(
            repo_id=repo_id,
            local_dir=local_dir,
            token=token,
            local_dir_use_symlinks=False,
            allow_patterns=patterns,
        )
    volume.commit()


@model_downloader.local_entrypoint()
def download() -> None:
    _download.remote()

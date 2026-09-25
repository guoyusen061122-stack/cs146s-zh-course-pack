#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""S02 · 抓取官方作业仓库（两个分支）。

来源：https://github.com/mihail911/modern-software-dev-assignments
- `fall2025` 分支：整门课的作业与实验代码（week1–week8）
- `master`    分支：当前学期（Fall 2026）已发布的部分

做法：直接下 codeload 的 tarball（一次请求拿全仓库），再用 GitHub API 取
**commit SHA** 记进账本 —— 有了 SHA，任何人任何时候都能取到与本包完全一致的原文，
这是"可复现"在素材层面的保证。
"""

from __future__ import annotations

import io
import os
import sys
import tarfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import common as C  # noqa: E402

OWNER = "mihail911"
REPO = "modern-software-dev-assignments"
BRANCHES = ["fall2025", "master"]
API = f"https://api.github.com/repos/{OWNER}/{REPO}"


def api_json(url: str):
    import json

    res = C.fetch(url, None, retries=2, headers={"Accept": "application/vnd.github+json"})
    if not res.data:
        return None
    try:
        return json.loads(res.data.decode("utf-8", "replace"))
    except Exception:  # noqa: BLE001
        return None


def main() -> int:
    C.ensure_dirs(C.REPO, C.WORK)
    ledger = C.Ledger("s02_fetch_repo")
    manifest = C.read_json(C.MANIFEST, {}) or {}
    manifest.setdefault("sources", {})

    meta = api_json(API) or {}
    C.log(f"[仓库] {OWNER}/{REPO}")
    C.log(f"       描述: {meta.get('description')}")
    C.log(f"       默认分支: {meta.get('default_branch')}  最近推送: {meta.get('pushed_at')}")

    total_files = 0
    for branch in BRANCHES:
        # --- commit SHA（可复现的关键锚点）---
        commit = api_json(f"{API}/commits/{branch}") or {}
        sha = commit.get("sha") or "unknown"
        commit_date = ((commit.get("commit") or {}).get("committer") or {}).get("date", "")

        url = (f"https://codeload.github.com/{OWNER}/{REPO}"
               f"/tar.gz/refs/heads/{branch}")
        cache = os.path.join(C.REPO, f"{REPO}-{branch}.tar.gz")
        res = C.fetch(url, cache, timeout=120)
        if res.error and not res.data:
            C.log(f"[分支] {branch} 抓取失败: {res.error}")
            ledger.add(branch=branch, status="failed", error=res.error)
            continue

        dest = os.path.join(C.REPO, branch)
        C.ensure_dirs(dest)
        with tarfile.open(fileobj=io.BytesIO(res.data), mode="r:gz") as tf:
            members = [m for m in tf.getmembers()
                       if m.isfile() and not os.path.isabs(m.name) and ".." not in m.name]
            tf.extractall(dest, members=members)

        files = []
        for m in members:
            # 去掉 tarball 顶层的 <repo>-<branch>/ 前缀，落地成干净的相对路径
            rel = m.name.split("/", 1)[1] if "/" in m.name else m.name
            files.append({"path": rel, "size": m.size})

        # 只保留可翻译/需入库的文档，代码文件只登记不翻译
        docs = [f for f in files if f["path"].lower().endswith((".md", ".txt", ".rst"))]
        code = [f for f in files if f not in docs]
        C.log(f"[分支] {branch}@{sha[:10]} ({commit_date[:10]})  "
              f"{len(files)} 个文件（文档 {len(docs)} / 代码 {len(code)}）")
        for f in docs:
            C.log(f"         {f['size']:>7}  {f['path']}")

        C.write_json(os.path.join(C.REPO, f"{branch}_files.json"),
                     {"branch": branch, "sha": sha, "commit_date": commit_date,
                      "files": files})

        manifest["sources"][f"git:{OWNER}/{REPO}@{branch}"] = {
            "kind": "repo_branch", "branch": branch, "commit_sha": sha,
            "commit_date": commit_date, "files": len(files),
            "bytes": len(res.data), "sha256": C.sha256_bytes(res.data),
            "cached_at": C.now_iso(),
            "cache": os.path.relpath(cache, C.ROOT),
        }
        ledger.add(branch=branch, sha=sha, commit_date=commit_date,
                   files=len(files), docs=len(docs), code=len(code))
        total_files += len(files)

    C.write_json(C.MANIFEST, manifest)
    rec = ledger.finish({"branches": len(BRANCHES), "files": total_files})
    C.append_ledger(rec)
    C.log(f"\n完成 · 输出 sources/repo/<branch>/")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

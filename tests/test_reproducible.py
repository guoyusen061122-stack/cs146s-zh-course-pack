#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""可复现性验证：重跑抽取，语料必须逐字节相同。

为什么单独做一个测试
--------------------
"不可复现"是本挑战的三条红线之一，而它最容易在**看不见的地方**破掉：
只要有人事后动了 `htmlmd.py` / `pdftext.py` / `s05_extract_corpus.py` 里的任何一行
抽取逻辑，重跑就会产出**不同的语料**，而既有译文是按旧语料逐块对齐的 ——
整包译文会在无人察觉的情况下错位。

本测试把这件事变成一条命令：

    python tests/test_reproducible.py

流程：备份 `corpus/en/` → 重跑 `s05` + `s05b` → 逐文件比对 SHA-256 → 恢复备份。
（比对完成后一定恢复备份，不会因为跑测试而改变仓库状态。）

退出码 0 = 语料可复现；非 0 = 有文件不一致，并列出是哪几份。
"""

from __future__ import annotations

import glob
import hashlib
import os
import shutil
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CORPUS_EN = os.path.join(ROOT, "corpus", "en")
BACKUP = os.path.join(ROOT, "corpus", "_en_backup")

for _s in ("stdout", "stderr"):
    try:
        getattr(sys, _s).reconfigure(encoding="utf-8", errors="replace")
    except Exception:  # noqa: BLE001
        pass


def digest(directory: str) -> dict[str, str]:
    out = {}
    for p in glob.glob(os.path.join(directory, "*.md")):
        with open(p, "rb") as fh:
            out[os.path.basename(p)] = hashlib.sha256(fh.read()).hexdigest()
    return out


def run(script: str) -> None:
    env = dict(os.environ, PYTHONUTF8="1", PYTHONIOENCODING="utf-8")
    res = subprocess.run([sys.executable, os.path.join("src", script)],
                         cwd=ROOT, env=env, capture_output=True, text=True)
    if res.returncode != 0:
        print(f"  {script} 执行失败：\n{res.stdout}\n{res.stderr}")
        sys.exit(res.returncode)


def main() -> int:
    if not os.path.isdir(CORPUS_EN):
        print("corpus/en/ 不存在，请先跑 src/s05_extract_corpus.py")
        return 1

    if os.path.isdir(BACKUP):
        shutil.rmtree(BACKUP)
    shutil.copytree(CORPUS_EN, BACKUP)
    before = digest(BACKUP)
    print(f"[1/4] 已备份 {len(before)} 份语料到 corpus/_en_backup/")

    try:
        print("[2/4] 重跑 src/s05_extract_corpus.py …")
        run("s05_extract_corpus.py")
        print("[3/4] 重跑 src/s05b_split.py …")
        run("s05b_split.py")

        after = digest(CORPUS_EN)
        same = [k for k in before if after.get(k) == before[k]]
        diff = [k for k in before if after.get(k) != before[k]]
        extra = [k for k in after if k not in before]
        missing = [k for k in before if k not in after]
    finally:
        shutil.rmtree(CORPUS_EN, ignore_errors=True)
        shutil.copytree(BACKUP, CORPUS_EN)
        shutil.rmtree(BACKUP, ignore_errors=True)
        print("[4/4] 已从备份恢复语料，仓库状态未变")

    print()
    print(f"  逐字节相同 : {len(same)}")
    print(f"  内容不同   : {len(diff)}")
    print(f"  多出文件   : {len(extra)}")
    print(f"  缺失文件   : {len(missing)}")

    if diff or extra or missing:
        print("\n❌ 语料不可复现：抽取逻辑被改动过，或素材缓存发生变化。")
        for k in diff[:10]:
            print(f"     内容不同：{k}")
        for k in extra[:10]:
            print(f"     多出：{k}")
        for k in missing[:10]:
            print(f"     缺失：{k}")
        print("\n  提示：语料一旦冻结并与译文对齐，就不能再改抽取器。")
        print("        若确实要改，必须重跑 s05 → s05b → s07 并**重新翻译**。")
        return 1

    print("\n✅ 语料可复现：重跑抽取得到逐字节相同的结果。")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

#!/usr/bin/env bash
# C1 一键复现（macOS / Linux）
#
#     bash scripts/reproduce.sh
#     SKIP_FETCH=1 bash scripts/reproduce.sh    # 只用本地缓存
#
# 与 scripts/reproduce.ps1 等价。零第三方依赖，失败即停并以非零码退出。

set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"

export PYTHONUTF8=1
export PYTHONIOENCODING=utf-8

if command -v python3 >/dev/null 2>&1; then PY=python3
elif command -v python >/dev/null 2>&1; then PY=python
else echo "找不到 Python，请先安装 Python 3.9+"; exit 1; fi

step() {
  echo
  echo "=============================================================="
  echo "  $1"
  echo "=============================================================="
  shift
  "$@"
}

echo "C1 复现开始 · 仓库根目录 $ROOT"
echo "Python: $($PY --version 2>&1)"

if [ "${SKIP_FETCH:-0}" != "1" ]; then
  step "S01 抓取课程官网并结构化"        "$PY" src/s01_fetch_site.py
  step "S02 抓取官方作业仓库"             "$PY" src/s02_fetch_repo.py
  step "S03 批量抓取阅读素材（6 级兜底）" "$PY" src/s03_fetch_readings.py
  step "S04 抓取讲义与媒体"               "$PY" src/s04_fetch_media.py
else
  echo "[跳过] s01–s04 抓取"
fi

step "S05 抽取统一语料"                  "$PY" src/s05_extract_corpus.py
step "S05b 超长素材按块边界拆分"         "$PY" src/s05b_split.py
step "S06 清点与覆盖率"                  "$PY" src/s06_inventory.py
step "S07 切段"                          "$PY" src/s07_segment.py
step "S08 术语表校验与生成"              "$PY" src/s08_glossary.py

echo
echo "--- S09 翻译进度 ---"
"$PY" src/s09_translate.py status

step "S10 质检"                          "$PY" src/s10_qa.py
step "S10b 术语回正（幂等自检）"         "$PY" src/s10b_fix.py --apply
step "S09 装配成品（纯中文 + 中英对照）" "$PY" src/s09_translate.py assemble

if [ "${SKIP_SITE:-0}" != "1" ]; then
  step "S11 构建离线双语文档站"          "$PY" src/s11_build_site.py
fi

step "冒烟测试"                          "$PY" tests/test_smoke.py

echo
echo "=============================================================="
echo "  复现完成"
echo "=============================================================="
echo "  清点报告 : reports/_inventory.md"
echo "  质检报告 : reports/_qa_report.md"
echo "  回正留痕 : reports/_term_fix_log.md"
echo "  文档站   : site/index.html"
echo

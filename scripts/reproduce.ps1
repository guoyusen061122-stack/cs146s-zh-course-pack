# C1 一键复现（Windows PowerShell）
#
#     powershell -ExecutionPolicy Bypass -File scripts/reproduce.ps1
#     powershell -ExecutionPolicy Bypass -File scripts/reproduce.ps1 -SkipFetch   # 只用本地缓存
#
# 设计要点：
#   · 零第三方依赖，不需要 pip install、不需要虚拟环境；
#   · 抓取结果带磁盘缓存，重跑直接命中缓存，所以默认也能离线跑；
#   · 每步失败即停止并以非零码退出（不把"跑挂"当"跑完"）。

param(
    [switch]$SkipFetch,          # 跳过 s01–s04 抓取（用已有缓存/已有素材）
    [switch]$SkipSite            # 跳过建站
)

$ErrorActionPreference = "Stop"
$Root = Split-Path -Parent $PSScriptRoot
Set-Location $Root

$env:PYTHONUTF8 = "1"
$env:PYTHONIOENCODING = "utf-8"

$Python = if (Get-Command python -ErrorAction SilentlyContinue) { "python" }
          elseif (Get-Command python3 -ErrorAction SilentlyContinue) { "python3" }
          else { throw "找不到 Python，请先安装 Python 3.9+ 并加入 PATH" }

function Step($name, $script) {
    Write-Host ""
    Write-Host "==============================================================" -ForegroundColor Cyan
    Write-Host "  $name" -ForegroundColor Cyan
    Write-Host "==============================================================" -ForegroundColor Cyan
    & $Python $script
    if ($LASTEXITCODE -ne 0) {
        Write-Host ""
        Write-Host "[失败] $name 以退出码 $LASTEXITCODE 结束，已停止。" -ForegroundColor Red
        exit $LASTEXITCODE
    }
}

Write-Host "C1 复现开始 · 仓库根目录 $Root"
Write-Host "Python: $(& $Python --version 2>&1)"

# ---------- 获取层（需要联网；有缓存时不联网）----------
if (-not $SkipFetch) {
    Step "S01 抓取课程官网并结构化"        "src/s01_fetch_site.py"
    Step "S02 抓取官方作业仓库"             "src/s02_fetch_repo.py"
    Step "S03 批量抓取阅读素材（6 级兜底）" "src/s03_fetch_readings.py"
    Step "S04 抓取讲义与媒体"               "src/s04_fetch_media.py"
} else {
    Write-Host "[跳过] s01–s04 抓取" -ForegroundColor Yellow
}

# ---------- 语料层 ----------
Step "S05 抽取统一语料"                 "src/s05_extract_corpus.py"
Step "S05b 超长素材按块边界拆分"        "src/s05b_split.py"

# ---------- 处理层 ----------
Step "S06 清点与覆盖率"                 "src/s06_inventory.py"
Step "S07 切段"                         "src/s07_segment.py"
Step "S08 术语表校验与生成"             "src/s08_glossary.py"

Write-Host ""
Write-Host "--- S09 翻译进度 ---" -ForegroundColor Cyan
& $Python "src/s09_translate.py" status

Step "S10 质检"                         "src/s10_qa.py"
Step "S10b 术语回正（幂等自检）"        "src/s10b_fix.py" "--apply"
Step "S09 装配成品（纯中文 + 中英对照）" "src/s09_translate.py" "assemble"

# ---------- 交付层 ----------
if (-not $SkipSite) {
    Step "S11 构建离线双语文档站"       "src/s11_build_site.py"
}

# ---------- 冒烟测试 ----------
Step "冒烟测试"                         "tests/test_smoke.py"

Write-Host ""
Write-Host "==============================================================" -ForegroundColor Green
Write-Host "  复现完成" -ForegroundColor Green
Write-Host "==============================================================" -ForegroundColor Green
Write-Host "  清点报告 : reports/_inventory.md"
Write-Host "  质检报告 : reports/_qa_report.md"
Write-Host "  回正留痕 : reports/_term_fix_log.md"
Write-Host "  文档站   : site/index.html"
Write-Host ""

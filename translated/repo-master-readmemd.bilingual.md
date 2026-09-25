# Assignments for CS146S: The Modern Software Developer

# CS146S：现代软件开发者的作业

This is the home of the assignments for [CS146S: The Modern Software Developer](https://themodernsoftware.dev), taught at Stanford University fall 2026.

这里是 [CS146S：现代软件开发者](https://themodernsoftware.dev) 课程作业的主页，该课程于 2026 年秋季在斯坦福大学开设。

## Repo Setup

## 仓库准备

These steps work with Python 3.12.

以下步骤适用于 Python 3.12。

1. Install Anaconda
1. Download and install: [Anaconda Individual Edition](https://www.anaconda.com/download)
1. Open a new terminal so `conda` is on your `PATH`.

1. 安装 Anaconda
1. 下载并安装：[Anaconda Individual Edition](https://www.anaconda.com/download)
1. 打开一个新的终端，使 `conda` 位于你的 `PATH` 中。

1. Create and activate a Conda environment (Python 3.12) ```bash conda create -n cs146s python=3.12 -y conda activate cs146s ```

1. 创建并激活 Conda 环境（Python 3.12） ```bash conda create -n cs146s python=3.12 -y conda activate cs146s ```

1. Install Poetry ```bash curl -sSL https://install.python-poetry.org | python - ```

1. 安装 Poetry ```bash curl -sSL https://install.python-poetry.org | python - ```

1. Install project dependencies with Poetry (inside the activated Conda env) From the repository root: ```bash poetry install --no-interaction ```

1. 用 Poetry 安装项目依赖（在已激活的 Conda 环境中） 在仓库根目录下： ```bash poetry install --no-interaction ```

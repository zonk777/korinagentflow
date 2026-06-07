# ResearchAgent

基于 LangGraph 的学术调研 Agent，提供论文搜索、文献综述、趋势分析和 LaTeX 草稿生成。

## 架构

```
用户输入 → planner → agent ⇄ tools → reflector → 输出
```

- **Planner**: 拆解任务为子步骤
- **Agent**: ReAct 循环，调用 LLM 选择工具
- **Tools**: ArXiv、Semantic Scholar、Web Search、Calculator、Bash
- **Reflector**: 自动检查执行结果

## 快速开始

### 环境要求

- Python >= 3.13
- [uv](https://docs.astral.sh/uv/) 包管理器

### 安装

```bash
git clone https://github.com/zonk777/researchagent.git
cd researchagent
uv sync
```

### 配置

```bash
cp .env.example .env
```

编辑 `.env` 填入：

```
API_KEY=sk-xxxxxxxx          # DeepSeek API Key
MODEL=deepseek-v4-pro        # 或 deepseek-chat（更快）
BASE_URL=https://api.deepseek.com
TAVILY_API_KEY=tvly-xxxx     # 从 https://tavily.com 获取
```

### 运行

```bash
# 学术调研
uv run researchagent research "Transformer efficiency optimization" -p 10

# 通用 Agent
uv run researchagent run "计算 123 * 456"

# Web 界面
uv run python webui.py        # 访问 http://localhost:7860

# 单独测试工具
uv run researchagent tool-test -t calculator "sqrt(144)"
uv run researchagent tool-test -t search "Python"
```

### 测试

```bash
uv run pytest tests/ -v       # 89 个测试
```

### Docker

```bash
docker-compose up
```

## 工具

| 工具 | 能力 |
|------|------|
| ArXivSearch | 预印本论文搜索（免费 API） |
| SemanticScholar | 已发表论文 + 被引数 + 会议信息 |
| WebSearch | Tavily 网络搜索 |
| Calculator | AST 白名单安全求值 |
| Bash | Shell 命令执行（危险命令拦截） |

## 分析功能

| 功能 | 说明 |
|------|------|
| 引用分析 | 总被引、H-index 估算、高被引排行 |
| 方法对比 | 提取 15 种 ML 方法模式的频率分布 |
| 趋势分析 | 年份分布 + growing/stable/declining + 关键词 |
| LaTeX 渲染 | Jinja2 模板生成论文草稿 |
| BibTeX 管理 | 自动生成 .bib 引用文件 |
| 研究空白分析 | LLM 分析现有方法局限性 |

## 项目结构

```
src/researchagent/
├── cli/           # CLI 入口 (Typer)
├── core/          # 状态、日志、重试、Token 追踪、LLM 工厂
├── graph/         # LangGraph 4 节点 pipeline
├── memory/        # 短期缓冲 + 长期向量库 (LanceDB + BGE-M3)
├── tools/         # 计算器 / Bash / Web 搜索
├── prompts/       # Agent / Planner / Reflector 提示词
├── providers/     # OpenAI 兼容 LLM 接口
└── research/      # 学术调研引擎
    ├── tools/     # ArXiv + Semantic Scholar + PaperDB
    ├── analysis/  # 引用 / 方法对比 / 趋势分析
    ├── output/    # LaTeX 渲染 + BibTeX + 论文追踪
    └── prompts/   # 研究空白分析提示词
```

## 技术栈

Python 3.13 / LangGraph / LanceDB / BGE-M3 / DeepSeek API / Gradio / Docker

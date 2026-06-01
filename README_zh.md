# Awesome Agent Harness

一个面向 **Agent Harness Engineering** 的工程实践清单，优先收录可直接落地的 GitHub 项目。

- 当前条目数: **251**
- GitHub 条目: **226 (90.0%)**
- 项目分类 GitHub 占比（不含阅读类）: **222/222 (100.0%)**
- 分类数量: **9**
- 最近核对日期: **2026-05-31**
- 语言: [English](./README.md) | [中文](./README_zh.md)

<a id="featured-harness-blogs"></a>
## 精选 Harness 博客

- [Scaling Managed Agents: Decoupling the brain from the hands](https://www.anthropic.com/engineering/managed-agents): Anthropic 提出的 meta-harness 架构，将长任务代理中的 session 日志、harness 循环与 sandbox 解耦。
- [Claude Code auto mode](https://www.anthropic.com/engineering/claude-code-auto-mode): Anthropic 介绍如何用分类器接管审批，在更高自治度下维持更安全的编码代理运行。
- [Harness engineering (OpenAI)](https://openai.com/index/harness-engineering/): 关于如何通过约束与验证构建可靠 agent-first 软件的实践报告。
- [Building Effective AI Agents](https://www.anthropic.com/engineering/building-effective-agents): Anthropic 关于何时使用工作流或自治代理以及如何组织系统的实践指南。
- [Writing effective tools for AI agents](https://www.anthropic.com/engineering/writing-tools-for-agents): 讲解如何设计工具接口，使代理更稳定且更安全地调用工具。
- [Effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents): 讲解长时代理运行中状态维护、可恢复性与可靠性的实践指南。
- [Harness design for long-running application development](https://www.anthropic.com/engineering/harness-design-long-running-apps): 关于通过 harness 结构改进长任务应用生成的后续文章。
- [Improving Deep Agents with harness engineering](https://blog.langchain.com/improving-deep-agents-with-harness-engineering/): 说明仅通过 harness 改进也能显著提升基准表现。
- [Evaluating Deep Agents: Our Learnings](https://blog.langchain.com/evaluating-deep-agents-our-learnings/): LangChain 关于有状态、长时代理评测设计的实战经验总结。
- [Your Agent Needs a Harness, Not a Framework](https://www.inngest.com/blog/your-agent-needs-a-harness-not-a-framework): 强调代理系统应优先建设可靠性基础设施，而非仅依赖框架思维。

## 目录

- [分类总览](#分类总览)
- [精选 Harness 博客](#featured-harness-blogs)
- [项目清单](#项目清单)
  - [Harness Architecture & Orchestration](#harness-architecture-orchestration)
  - [Context & Working-State Engineering](#context-working-state-engineering)
  - [Execution Substrates & Sandboxing](#execution-substrates-sandboxing)
  - [Protocols, Tool Interfaces & Agent Contracts](#protocols-tool-interfaces-agent-contracts)
  - [Evaluation Harnesses & Benchmarks](#evaluation-harnesses-benchmarks)
  - [Observability & Reliability Operations](#observability-reliability-operations)
  - [Guardrails, Security & Governance](#guardrails-security-governance)
  - [Reference Harness Implementations](#reference-harness-implementations)
  - [Essential Readings & Ecosystem Maps](#essential-readings-ecosystem-maps)
- [维护说明](#维护说明)
- [引用](#引用)

## 分类总览

| 分类 | 条目数 |
| --- | ---: |
| Harness Architecture & Orchestration | 39 |
| Context & Working-State Engineering | 15 |
| Execution Substrates & Sandboxing | 26 |
| Protocols, Tool Interfaces & Agent Contracts | 16 |
| Evaluation Harnesses & Benchmarks | 27 |
| Observability & Reliability Operations | 15 |
| Guardrails, Security & Governance | 19 |
| Reference Harness Implementations | 65 |
| Essential Readings & Ecosystem Maps | 29 |

## 项目清单

说明：
- `Stars` 使用徽章展示（来自快照值）。
- 仓库更新时间统一记录在 `data/projects.yaml` 与验证报告中。
- 每个分类内按 Stars 降序排序。

<a id="harness-architecture-orchestration"></a>
### Harness Architecture & Orchestration

| 项目 | 链接 | Stars | 标签 | 简介 |
| --- | --- | --- | --- | --- |
| Superpowers | [GitHub](https://github.com/obra/superpowers) | [![star](https://img.shields.io/badge/star-213521-f4b400?style=flat-square)](https://github.com/obra/superpowers) | skills, workflow, cross-agent | 由可组合技能、强制工作流、worktree、规划、TDD、评审与子代理执行构成的跨代理软件开发方法论。 |
| ECC | [GitHub](https://github.com/affaan-m/ECC) | [![star](https://img.shields.io/badge/star-200020-f4b400?style=flat-square)](https://github.com/affaan-m/ECC) | cross-harness, hooks, skills | 跨 harness 的操作系统，整合技能、钩子、记忆优化、安全扫描与校验工作流，用于 agentic 工作。 |
| gstack | [GitHub](https://github.com/garrytan/gstack) | [![star](https://img.shields.io/badge/star-105014-f4b400?style=flat-square)](https://github.com/garrytan/gstack) | skills, qa, release | 面向 Claude Code 与多种编码代理的技能栈，将产品规划、架构评审、QA、安全、发布与复盘转化为可重复的代理工作流。 |
| DeerFlow | [GitHub](https://github.com/bytedance/deer-flow) | [![star](https://img.shields.io/badge/star-70080-f4b400?style=flat-square)](https://github.com/bytedance/deer-flow) | long-horizon, memory, subagents | 面向长任务的 SuperAgent harness，整合记忆、工具、子代理与沙箱。 |
| oh-my-openagent | [GitHub](https://github.com/code-yeongyu/oh-my-openagent) | [![star](https://img.shields.io/badge/star-60415-f4b400?style=flat-square)](https://github.com/code-yeongyu/oh-my-openagent) | multi-harness, team-mode, skills | 面向 OpenCode、Codex、Claude Code 等编码代理的多 harness agent OS，提供团队模式编排、后台代理、MCP 与技能。 |
| AutoGen | [GitHub](https://github.com/microsoft/autogen) | [![star](https://img.shields.io/badge/star-58562-f4b400?style=flat-square)](https://github.com/microsoft/autogen) | multi-agent, orchestration, framework | 支持多代理交互与编排的 agentic AI 编程框架。 |
| Ruflo | [GitHub](https://github.com/ruvnet/ruflo) | [![star](https://img.shields.io/badge/star-56847-f4b400?style=flat-square)](https://github.com/ruvnet/ruflo) | multi-agent, swarm, mcp | 面向 Claude Code 的多代理编排平台，提供群组协作、持久记忆、联邦通信、插件与 MCP 钩子。 |
| CrewAI | [GitHub](https://github.com/crewAIInc/crewAI) | [![star](https://img.shields.io/badge/star-52521-f4b400?style=flat-square)](https://github.com/crewAIInc/crewAI) | multi-agent, workflows, control-plane | 多代理自动化框架，提供生产级 Flows、自治 Crews、事件驱动控制、追踪、护栏、记忆与人工审核钩子。 |
| Agno | [GitHub](https://github.com/agno-agi/agno) | [![star](https://img.shields.io/badge/star-40436-f4b400?style=flat-square)](https://github.com/agno-agi/agno) | scale, runtime, management | 面向规模化运行与管理的 agent 软件运行时。 |
| LangGraph | [GitHub](https://github.com/langchain-ai/langgraph) | [![star](https://img.shields.io/badge/star-33457-f4b400?style=flat-square)](https://github.com/langchain-ai/langgraph) | graph, workflow, runtime | 图结构运行时，用于构建具备状态管理与确定性流程控制的可靠代理。 |
| Semantic Kernel | [GitHub](https://github.com/microsoft/semantic-kernel) | [![star](https://img.shields.io/badge/star-28015-f4b400?style=flat-square)](https://github.com/microsoft/semantic-kernel) | enterprise, orchestration, plugins | 面向企业应用的 agentic 框架，支持编排与插件化扩展。 |
| OpenAI Agents SDK (Python) | [GitHub](https://github.com/openai/openai-agents-python) | [![star](https://img.shields.io/badge/star-26794-f4b400?style=flat-square)](https://github.com/openai/openai-agents-python) | sdk, handoff, workflows | 轻量级多代理工作流框架，支持交接、编排和生产化模式。 |
| Symphony | [GitHub](https://github.com/openai/symphony) | [![star](https://img.shields.io/badge/star-24877-f4b400?style=flat-square)](https://github.com/openai/symphony) | orchestration, control-plane, workflows | 以工单驱动的编排层，可将项目工作转成隔离的自治实现任务。 |
| deepagents | [GitHub](https://github.com/langchain-ai/deepagents) | [![star](https://img.shields.io/badge/star-23602-f4b400?style=flat-square)](https://github.com/langchain-ai/deepagents) | runtime, orchestration, long-running | 面向长时任务的开源 harness，支持规划、工具调用与子代理协作模式。 |
| Archon | [GitHub](https://github.com/coleam00/Archon) | [![star](https://img.shields.io/badge/star-22034-f4b400?style=flat-square)](https://github.com/coleam00/Archon) | workflow-engine, worktrees, validation | 面向 AI 编码代理的工作流引擎，提供 YAML 定义阶段、隔离 worktree 与校验门禁。 |
| Google ADK (Python) | [GitHub](https://github.com/google/adk-python) | [![star](https://img.shields.io/badge/star-19932-f4b400?style=flat-square)](https://github.com/google/adk-python) | toolkit, deployment, evaluation | 代码优先的工具包，用于构建、评估和部署复杂 AI 代理。 |
| elizaOS | [GitHub](https://github.com/elizaOS/eliza) | [![star](https://img.shields.io/badge/star-18486-f4b400?style=flat-square)](https://github.com/elizaOS/eliza) | agent-os, plugins, benchmarks | 可扩展的代理运行时与操作系统，提供 CLI 脚手架、代理循环、插件、记忆/状态原语、仪表盘、连接器与基准套件。 |
| PydanticAI | [GitHub](https://github.com/pydantic/pydantic-ai) | [![star](https://img.shields.io/badge/star-17418-f4b400?style=flat-square)](https://github.com/pydantic/pydantic-ai) | python, typing, schema | 强调类型与结构化约束的 Python agent 框架，适合稳定化 harness 开发。 |
| Microsoft Agent Framework | [GitHub](https://github.com/microsoft/agent-framework) | [![star](https://img.shields.io/badge/star-10908-f4b400?style=flat-square)](https://github.com/microsoft/agent-framework) | multi-agent, workflows, observability | 多语言代理框架，支持图工作流、编排、部署与可观测能力。 |
| Hive | [GitHub](https://github.com/aden-hive/hive) | [![star](https://img.shields.io/badge/star-10465-f4b400?style=flat-square)](https://github.com/aden-hive/hive) | harness, orchestration, runtime | 以结果驱动的 agent runtime harness，强调控制回路与编排模块。 |
| VoltAgent | [GitHub](https://github.com/VoltAgent/voltagent) | [![star](https://img.shields.io/badge/star-9275-f4b400?style=flat-square)](https://github.com/VoltAgent/voltagent) | typescript, platform, runtime | 基于 TypeScript 的 agent 工程平台，提供开放运行时抽象。 |
| mcp-agent | [GitHub](https://github.com/lastmile-ai/mcp-agent) | [![star](https://img.shields.io/badge/star-8347-f4b400?style=flat-square)](https://github.com/lastmile-ai/mcp-agent) | mcp, runtime, workflow | 以 MCP 工具体系为核心的实用 agent 框架，强调工作流组合。 |
| Agent Squad | [GitHub](https://github.com/2FastLabs/agent-squad) | [![star](https://img.shields.io/badge/star-7642-f4b400?style=flat-square)](https://github.com/2FastLabs/agent-squad) | routing, multi-agent, context | 多代理编排框架，可进行请求路由、保持会话上下文，支持 Python/TypeScript，并协调专业代理团队。 |
| Yao | [GitHub](https://github.com/YaoApp/yao) | [![star](https://img.shields.io/badge/star-7542-f4b400?style=flat-square)](https://github.com/YaoApp/yao) | single-binary, runtime, autonomous | 单二进制运行时，用于定义并运行自治代理。 |
| Open Multi-Agent | [GitHub](https://github.com/open-multi-agent/open-multi-agent) | [![star](https://img.shields.io/badge/star-6294-f4b400?style=flat-square)](https://github.com/open-multi-agent/open-multi-agent) | multi-agent, dag, tracing | 基于 TypeScript 的多代理编排器，可将目标自动分解为任务 DAG，并提供并行执行、MCP 集成与实时追踪。 |
| Strands Agents | [GitHub](https://github.com/strands-agents/sdk-python) | [![star](https://img.shields.io/badge/star-5987-f4b400?style=flat-square)](https://github.com/strands-agents/sdk-python) | sdk, mcp, tools | 模型驱动的代理 SDK 与 monorepo，包含 Python/TypeScript 代理循环、模型适配器、工具、MCP 集成、多代理系统与流式能力。 |
| Cloudflare Agents | [GitHub](https://github.com/cloudflare/agents) | [![star](https://img.shields.io/badge/star-5011-f4b400?style=flat-square)](https://github.com/cloudflare/agents) | platform, deployment, runtime | 提供面向生产基础设施的 agent 构建与部署运行时。 |
| Flue | [GitHub](https://github.com/withastro/flue) | [![star](https://img.shields.io/badge/star-3823-f4b400?style=flat-square)](https://github.com/withastro/flue) | typescript, headless, sandbox | 面向无界面代理的 TypeScript harness 框架，提供会话、工具、技能与可插拔沙箱。 |
| OpenAI Agents SDK (JS/TS) | [GitHub](https://github.com/openai/openai-agents-js) | [![star](https://img.shields.io/badge/star-3152-f4b400?style=flat-square)](https://github.com/openai/openai-agents-js) | typescript, workflows, sandbox-agents | 面向 JavaScript/TypeScript 的多代理工作流框架，支持交接、工具、护栏、会话、追踪与沙箱代理。 |
| Docker Agent | [GitHub](https://github.com/docker/docker-agent) | [![star](https://img.shields.io/badge/star-2976-f4b400?style=flat-square)](https://github.com/docker/docker-agent) | docker, runtime, container | 强调容器原生执行的 agent 构建与运行时栈。 |
| NeMo Agent Toolkit | [GitHub](https://github.com/NVIDIA/NeMo-Agent-Toolkit) | [![star](https://img.shields.io/badge/star-2347-f4b400?style=flat-square)](https://github.com/NVIDIA/NeMo-Agent-Toolkit) | multi-agent, optimization, toolkit | 用于连接与优化多代理协作的开源工具包。 |
| Scion | [GitHub](https://github.com/GoogleCloudPlatform/scion) | [![star](https://img.shields.io/badge/star-1557-f4b400?style=flat-square)](https://github.com/GoogleCloudPlatform/scion) | multi-agent, containers, orchestration | 实验性多代理编排测试平台，可在容器、git worktree 与远程运行时中隔离运行各类 agent harness。 |
| deepagentsjs | [GitHub](https://github.com/langchain-ai/deepagentsjs) | [![star](https://img.shields.io/badge/star-1281-f4b400?style=flat-square)](https://github.com/langchain-ai/deepagentsjs) | typescript, langgraph, subagents | 基于 TypeScript 的 agent harness，内置规划、文件系统工具、子代理与 LangGraph 原生运行时能力。 |
| oh-my-agent | [GitHub](https://github.com/first-fluke/oh-my-agent) | [![star](https://img.shields.io/badge/star-1039-f4b400?style=flat-square)](https://github.com/first-fluke/oh-my-agent) | multi-agent, skills, cross-runtime | 可移植多代理 harness，可将共享代理、技能、工作流与规则投射到多个编码代理运行时。 |
| Chorus | [GitHub](https://github.com/Chorus-AIDLC/Chorus) | [![star](https://img.shields.io/badge/star-938-f4b400?style=flat-square)](https://github.com/Chorus-AIDLC/Chorus) | ai-dlc, permissions, task-state | 面向人机协作的 harness，管理会话生命周期、任务状态、子代理编排、可观测性与故障恢复。 |
| Pydantic AI Harness | [GitHub](https://github.com/pydantic/pydantic-ai-harness) | [![star](https://img.shields.io/badge/star-456-f4b400?style=flat-square)](https://github.com/pydantic/pydantic-ai-harness) | capabilities, hooks, pydantic | Pydantic AI 官方能力库，可将工具、生命周期钩子、指令与模型设置组合为可复用的 agent harness。 |
| Water | [GitHub](https://github.com/manthanguptaa/water) | [![star](https://img.shields.io/badge/star-288-f4b400?style=flat-square)](https://github.com/manthanguptaa/water) | python, framework, approval-gates | Python agent harness 框架，覆盖编排、韧性、可观测性、护栏、审批门禁、沙箱与部署。 |
| OmniCoreAgent | [GitHub](https://github.com/omnirexflora-labs/omnicoreagent) | [![star](https://img.shields.io/badge/star-241-f4b400?style=flat-square)](https://github.com/omnirexflora-labs/omnicoreagent) | python, mcp, serving | Python 生产级 harness，包含模型循环、工具、MCP、记忆、工作区文件、护栏、事件、子代理、后台任务与 REST/SSE 服务。 |
| hankweave | [GitHub](https://github.com/SouthBridgeAI/hankweave-runtime) | [![star](https://img.shields.io/badge/star-125-f4b400?style=flat-square)](https://github.com/SouthBridgeAI/hankweave-runtime) | long-horizon, runtime, checkpoints | 面向长任务的无界面运行时，可编排现有 agent harness，并提供 sentinels、循环、检查点与事件日志。 |

<a id="context-working-state-engineering"></a>
### Context & Working-State Engineering

| 项目 | 链接 | Stars | 标签 | 简介 |
| --- | --- | --- | --- | --- |
| claude-mem | [GitHub](https://github.com/thedotmack/claude-mem) | [![star](https://img.shields.io/badge/star-79855-f4b400?style=flat-square)](https://github.com/thedotmack/claude-mem) | memory, context, session | 插件化记忆层，可记录会话历史并在后续编码任务中注入相关上下文。 |
| planning-with-files | [GitHub](https://github.com/OthmanAdi/planning-with-files) | [![star](https://img.shields.io/badge/star-22407-f4b400?style=flat-square)](https://github.com/OthmanAdi/planning-with-files) | planning, skills, persistence | 用于编码代理工作流的持久化文件规划技能包。 |
| agentmemory | [GitHub](https://github.com/rohitg00/agentmemory) | [![star](https://img.shields.io/badge/star-20119-f4b400?style=flat-square)](https://github.com/rohitg00/agentmemory) | memory, mcp, hooks | 面向编码代理的持久记忆服务器，使用钩子、MCP/REST 集成、混合搜索与跨会话召回。 |
| Agent Skills for Context Engineering | [GitHub](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering) | [![star](https://img.shields.io/badge/star-16182-f4b400?style=flat-square)](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering) | skills, context, production | 面向上下文工程与生产代理的大型技能库。 |
| Context Mode | [GitHub](https://github.com/mksglu/context-mode) | [![star](https://img.shields.io/badge/star-16077-f4b400?style=flat-square)](https://github.com/mksglu/context-mode) | context, mcp, session | MCP 上下文优化服务器，可隔离工具输出、索引会话事件，并在代理压缩上下文后恢复连续性。 |
| Context-Engineering Handbook | [GitHub](https://github.com/davidkimai/Context-Engineering) | [![star](https://img.shields.io/badge/star-9032-f4b400?style=flat-square)](https://github.com/davidkimai/Context-Engineering) | context-engineering, handbook, practices | 面向代理系统的第一性原理上下文工程手册，强调实践落地。 |
| Trellis | [GitHub](https://github.com/mindfold-ai/Trellis) | [![star](https://img.shields.io/badge/star-8758-f4b400?style=flat-square)](https://github.com/mindfold-ai/Trellis) | specs, memory, workflow | 面向多平台编码代理的工作流框架，提供任务上下文、项目记忆与规范注入。 |
| CCPM | [GitHub](https://github.com/automazeio/ccpm) | [![star](https://img.shields.io/badge/star-8160-f4b400?style=flat-square)](https://github.com/automazeio/ccpm) | planning, github-issues, parallel-execution | 规格驱动的项目管理技能，将 PRD 与 GitHub issue 转化为持久上下文和并行代理执行流程。 |
| TencentDB Agent Memory | [GitHub](https://github.com/Tencent/TencentDB-Agent-Memory) | [![star](https://img.shields.io/badge/star-4486-f4b400?style=flat-square)](https://github.com/Tencent/TencentDB-Agent-Memory) | memory, context-offloading, openclaw | 本地 agent 记忆插件，结合符号化短期状态、分层长期记忆、可追溯链路，并支持 OpenClaw 与 Hermes 集成。 |
| Acontext | [GitHub](https://github.com/memodb-io/Acontext) | [![star](https://img.shields.io/badge/star-3495-f4b400?style=flat-square)](https://github.com/memodb-io/Acontext) | skills, memory, progressive-disclosure | 技能式记忆层，可将代理运行经验沉淀为可检查的技能文件，并通过代理可控工具召回。 |
| Awesome Context Engineering | [GitHub](https://github.com/Meirtz/Awesome-Context-Engineering) | [![star](https://img.shields.io/badge/star-3160-f4b400?style=flat-square)](https://github.com/Meirtz/Awesome-Context-Engineering) | awesome-list, context, survey | 面向上下文工程的综述型清单，覆盖资源与框架。 |
| agentic-stack | [GitHub](https://github.com/codejunkie99/agentic-stack) | [![star](https://img.shields.io/badge/star-2056-f4b400?style=flat-square)](https://github.com/codejunkie99/agentic-stack) | cross-harness, memory, skills | 可移植的记忆、技能、协议与仪表盘层，可在多个编码代理 harness 之间保持状态连续。 |
| context-space | [GitHub](https://github.com/context-space/context-space) | [![star](https://img.shields.io/badge/star-810-f4b400?style=flat-square)](https://github.com/context-space/context-space) | context, infrastructure, mcp | 聚焦上下文工程基础设施的项目，强调 MCP 生态集成能力。 |
| Memorix | [GitHub](https://github.com/AVIDS2/memorix) | [![star](https://img.shields.io/badge/star-442-f4b400?style=flat-square)](https://github.com/AVIDS2/memorix) | memory, mcp, cross-agent | 本地优先的跨代理记忆控制平面，支持 MCP、工作区同步、会话与编排状态。 |
| sd0x-dev-flow | [GitHub](https://github.com/sd0xdev/sd0x-dev-flow) | [![star](https://img.shields.io/badge/star-163-f4b400?style=flat-square)](https://github.com/sd0xdev/sd0x-dev-flow) | hooks, state-machine, claude-code | Claude Code harness 层，提供钩子强制双重评审、持久状态机门禁、上下文压缩恢复与 fail-closed 安全机制。 |

<a id="execution-substrates-sandboxing"></a>
### Execution Substrates & Sandboxing

| 项目 | 链接 | Stars | 标签 | 简介 |
| --- | --- | --- | --- | --- |
| Daytona | [GitHub](https://github.com/daytonaio/daytona) | [![star](https://img.shields.io/badge/star-72503-f4b400?style=flat-square)](https://github.com/daytonaio/daytona) | sandbox, execution, infra | 面向 AI 生成代码的安全弹性沙箱基础设施，提供文件、Git、LSP 与执行 API。 |
| CUA | [GitHub](https://github.com/trycua/cua) | [![star](https://img.shields.io/badge/star-17378-f4b400?style=flat-square)](https://github.com/trycua/cua) | computer-use, sandbox, infra | 面向计算机操作代理的基础设施栈，包含沙箱、SDK 与基准支持。 |
| Browser Harness | [GitHub](https://github.com/browser-use/browser-harness) | [![star](https://img.shields.io/badge/star-14107-f4b400?style=flat-square)](https://github.com/browser-use/browser-harness) | browser, cdp, self-healing | 轻量可编辑的 CDP harness，可将 LLM 直接接入真实浏览器，并允许代理在运行中扩展辅助能力。 |
| E2B | [GitHub](https://github.com/e2b-dev/E2B) | [![star](https://img.shields.io/badge/star-12418-f4b400?style=flat-square)](https://github.com/e2b-dev/E2B) | cloud-sandbox, execution, enterprise | 提供真实工具的安全云端环境，面向生产级代理执行。 |
| OpenSandbox | [GitHub](https://github.com/alibaba/OpenSandbox) | [![star](https://img.shields.io/badge/star-10898-f4b400?style=flat-square)](https://github.com/alibaba/OpenSandbox) | sandbox, security, runtime | 面向代理工作负载的安全可扩展沙箱运行时。 |
| Microsandbox | [GitHub](https://github.com/superradcompany/microsandbox) | [![star](https://img.shields.io/badge/star-6363-f4b400?style=flat-square)](https://github.com/superradcompany/microsandbox) | sandbox, vm, mcp | 本地 rootless VM 沙箱运行时，提供 SDK、可分离长会话、agent skills 与 MCP server 集成。 |
| OpenShell | [GitHub](https://github.com/NVIDIA/OpenShell) | [![star](https://img.shields.io/badge/star-6348-f4b400?style=flat-square)](https://github.com/NVIDIA/OpenShell) | sandbox, policy, runtime | 面向自治代理的安全私有运行时，提供沙箱生命周期控制，以及声明式文件系统、网络、进程与推理策略。 |
| CubeSandbox | [GitHub](https://github.com/TencentCloud/CubeSandbox) | [![star](https://img.shields.io/badge/star-6021-f4b400?style=flat-square)](https://github.com/TencentCloud/CubeSandbox) | microvm, sandbox, e2b-compatible | 面向 AI 代理的 MicroVM 沙箱服务，提供低于 60ms 的启动速度、E2B 兼容 API 与硬件级隔离。 |
| Sandcastle | [GitHub](https://github.com/mattpocock/sandcastle) | [![star](https://img.shields.io/badge/star-5527-f4b400?style=flat-square)](https://github.com/mattpocock/sandcastle) | sandbox, typescript, branch-strategy | 用于在隔离沙箱中编排编码代理的 TypeScript 库，支持可配置分支策略。 |
| agent-infra sandbox | [GitHub](https://github.com/agent-infra/sandbox) | [![star](https://img.shields.io/badge/star-4868-f4b400?style=flat-square)](https://github.com/agent-infra/sandbox) | all-in-one, browser, shell | 集成浏览器、Shell、文件、MCP 与 IDE 服务的一体化沙箱。 |
| Judge0 | [GitHub](https://github.com/judge0/judge0) | [![star](https://img.shields.io/badge/star-4195-f4b400?style=flat-square)](https://github.com/judge0/judge0) | code-execution, sandbox, backend | 可扩展的沙箱代码执行系统，可作为代理执行后端。 |
| Agent Sandbox | [GitHub](https://github.com/kubernetes-sigs/agent-sandbox) | [![star](https://img.shields.io/badge/star-2672-f4b400?style=flat-square)](https://github.com/kubernetes-sigs/agent-sandbox) | kubernetes, sandbox, stateful | 面向隔离且有状态 agent runtime 的 Kubernetes 原生沙箱控制平面，提供稳定身份、持久化与预热池能力。 |
| stakpak/agent | [GitHub](https://github.com/stakpak/agent) | [![star](https://img.shields.io/badge/star-1572-f4b400?style=flat-square)](https://github.com/stakpak/agent) | always-on, autonomous, ops | 常驻机器运行的开源自治代理，强调持续运维闭环。 |
| Sandbox Agent | [GitHub](https://github.com/rivet-dev/sandbox-agent) | [![star](https://img.shields.io/badge/star-1414-f4b400?style=flat-square)](https://github.com/rivet-dev/sandbox-agent) | sandbox, coding-agents, session-schema | 用于在沙箱内运行编码代理的 HTTP/SSE 控制服务器，提供标准化会话、权限、事件流与回放能力。 |
| OSS-Fuzz Gen | [GitHub](https://github.com/google/oss-fuzz-gen) | [![star](https://img.shields.io/badge/star-1400-f4b400?style=flat-square)](https://github.com/google/oss-fuzz-gen) | fuzzing, security, execution | 将 LLM 驱动模糊测试与受控执行环境结合的工程实现。 |
| E2B Desktop Sandbox | [GitHub](https://github.com/e2b-dev/desktop) | [![star](https://img.shields.io/badge/star-1391-f4b400?style=flat-square)](https://github.com/e2b-dev/desktop) | desktop, sandbox, computer-use | 面向 computer-use 代理的安全虚拟桌面沙箱，提供 SDK 控制与屏幕流式能力。 |
| AgentBay SDK | [GitHub](https://github.com/agentbay-ai/wuying-agentbay-sdk) | [![star](https://img.shields.io/badge/star-1127-f4b400?style=flat-square)](https://github.com/agentbay-ai/wuying-agentbay-sdk) | cloud-sandbox, computer-use, sdk | 面向代理的云沙箱 SDK，覆盖浏览器、桌面、移动端与代码执行环境。 |
| Tensorlake | [GitHub](https://github.com/tensorlakeai/tensorlake) | [![star](https://img.shields.io/badge/star-928-f4b400?style=flat-square)](https://github.com/tensorlakeai/tensorlake) | microvm, sandbox, orchestration | 面向 agent 沙箱的无服务器运行时，提供 MicroVM 隔离、快照、挂起恢复与后台编排能力。 |
| Arrakis | [GitHub](https://github.com/abshkbh/arrakis) | [![star](https://img.shields.io/badge/star-815-f4b400?style=flat-square)](https://github.com/abshkbh/arrakis) | sandbox, microvm, snapshots | 自托管沙箱基座，提供 MicroVM 隔离、快照恢复，以及面向代理代码执行与 computer use 的 REST、SDK 与 MCP 接口。 |
| AgentScope Runtime | [GitHub](https://github.com/agentscope-ai/agentscope-runtime) | [![star](https://img.shields.io/badge/star-804-f4b400?style=flat-square)](https://github.com/agentscope-ai/agentscope-runtime) | runtime, sandbox, deployment | 面向代理应用的生产运行时，提供安全工具沙箱、部署 API、可观测能力与状态服务。 |
| SWE-ReX | [GitHub](https://github.com/SWE-agent/SWE-ReX) | [![star](https://img.shields.io/badge/star-516-f4b400?style=flat-square)](https://github.com/SWE-agent/SWE-ReX) | sandbox, execution, coding-agent | 面向 AI 编码代理的沙箱执行基础设施，支持本地与云端扩展。 |
| sandboxed.sh | [GitHub](https://github.com/Th0rgal/sandboxed.sh) | [![star](https://img.shields.io/badge/star-441-f4b400?style=flat-square)](https://github.com/Th0rgal/sandboxed.sh) | self-hosted, isolation, orchestrator | 在隔离 Linux 工作区中运行编码代理的自托管编排器。 |
| Capsule | [GitHub](https://github.com/capsulerun/capsule) | [![star](https://img.shields.io/badge/star-288-f4b400?style=flat-square)](https://github.com/capsulerun/capsule) | wasm, sandbox, task-runtime | 在隔离 WebAssembly 沙箱中协调 agent 任务的耐久运行时，提供重试与生命周期跟踪。 |
| agentbox | [GitHub](https://github.com/mattolson/agent-sandbox) | [![star](https://img.shields.io/badge/star-174-f4b400?style=flat-square)](https://github.com/mattolson/agent-sandbox) | sandbox, coding-agents, network-policy | 面向 AI 编码代理的本地锁定沙箱，提供限定文件访问、出站策略、密钥注入、防火墙与持久代理状态。 |
| HexAgent | [GitHub](https://github.com/UnicomAI/hexagent) | [![star](https://img.shields.io/badge/star-123-f4b400?style=flat-square)](https://github.com/UnicomAI/hexagent) | computer-layer, sandbox, runtime | 将代理运行时与其操作的计算机分离的 agent harness，支持本地、VM 与云端沙箱后端。 |
| terminal-bench-env | [GitHub](https://github.com/ucsb-mlsec/terminal-bench-env) | [![star](https://img.shields.io/badge/star-82-f4b400?style=flat-square)](https://github.com/ucsb-mlsec/terminal-bench-env) | terminal, benchmark-env, sandbox | 为终端代理基准测试提供执行环境层。 |

<a id="protocols-tool-interfaces-agent-contracts"></a>
### Protocols, Tool Interfaces & Agent Contracts

| 项目 | 链接 | Stars | 标签 | 简介 |
| --- | --- | --- | --- | --- |
| Anthropic Agent Skills | [GitHub](https://github.com/anthropics/skills) | [![star](https://img.shields.io/badge/star-144584-f4b400?style=flat-square)](https://github.com/anthropics/skills) | skills, spec, claude | Anthropic 官方 Agent Skills 仓库，包含技能规范、模板与 Claude 的参考技能实现。 |
| GitHub Spec Kit | [GitHub](https://github.com/github/spec-kit) | [![star](https://img.shields.io/badge/star-107305-f4b400?style=flat-square)](https://github.com/github/spec-kit) | spec-driven, workflows, tooling | 面向规范驱动开发的工具包，可引导代理进行确定性执行。 |
| MCP Servers | [GitHub](https://github.com/modelcontextprotocol/servers) | [![star](https://img.shields.io/badge/star-86522-f4b400?style=flat-square)](https://github.com/modelcontextprotocol/servers) | mcp, servers, implementations | 官方 MCP Server 实现集合，覆盖多种工具与场景。 |
| Chrome DevTools MCP | [GitHub](https://github.com/ChromeDevTools/chrome-devtools-mcp) | [![star](https://img.shields.io/badge/star-42407-f4b400?style=flat-square)](https://github.com/ChromeDevTools/chrome-devtools-mcp) | mcp, browser, devtools | 官方 MCP server，为编码代理提供 Chrome DevTools 接入能力，用于可靠的浏览器自动化、调试与性能分析。 |
| Playwright MCP | [GitHub](https://github.com/microsoft/playwright-mcp) | [![star](https://img.shields.io/badge/star-33260-f4b400?style=flat-square)](https://github.com/microsoft/playwright-mcp) | mcp, browser, playwright | Playwright 官方 MCP server，为代理提供结构化可访问性快照与确定性浏览器自动化工具。 |
| AGENTS.md | [GitHub](https://github.com/agentsmd/agents.md) | [![star](https://img.shields.io/badge/star-21856-f4b400?style=flat-square)](https://github.com/agentsmd/agents.md) | spec, agent-file, instructions | 面向代码仓库本地代理指令的开放格式规范。 |
| Model Context Protocol | [GitHub](https://github.com/modelcontextprotocol/modelcontextprotocol) | [![star](https://img.shields.io/badge/star-8282-f4b400?style=flat-square)](https://github.com/modelcontextprotocol/modelcontextprotocol) | mcp, protocol, interoperability | MCP 的核心规范与文档，定义工具与上下文互操作方式。 |
| directories (rules and MCP indexes) | [GitHub](https://github.com/leerob/directories) | [![star](https://img.shields.io/badge/star-3942-f4b400?style=flat-square)](https://github.com/leerob/directories) | directories, mcp, rules | 面向规则与 MCP server 发现的目录索引集合。 |
| Atmosphere | [GitHub](https://github.com/Atmosphere/atmosphere) | [![star](https://img.shields.io/badge/star-3771-f4b400?style=flat-square)](https://github.com/Atmosphere/atmosphere) | jvm, multi-protocol, governance | 面向 JVM 的可治理 AI 代理运行时，可通过 MCP、A2A、AG-UI 与浏览器侧传输协议对外提供服务。 |
| LangChain MCP Adapters | [GitHub](https://github.com/langchain-ai/langchain-mcp-adapters) | [![star](https://img.shields.io/badge/star-3550-f4b400?style=flat-square)](https://github.com/langchain-ai/langchain-mcp-adapters) | mcp, adapters, integration | 用于连接 LangChain 组件与 MCP server 的适配层。 |
| Microsoft MCP Servers | [GitHub](https://github.com/microsoft/mcp) | [![star](https://img.shields.io/badge/star-3233-f4b400?style=flat-square)](https://github.com/microsoft/mcp) | mcp, enterprise, servers | 微软官方 MCP server 目录，连接企业数据与工具。 |
| GitAgentProtocol | [GitHub](https://github.com/open-gitagent/gitagent-protocol) | [![star](https://img.shields.io/badge/star-2794-f4b400?style=flat-square)](https://github.com/open-gitagent/gitagent-protocol) | standard, git-native, workflows | 以 Git 为原生载体、框架无关的代理定义标准，可在仓库内组织 agents、skills、workflows、tools 与运行时记忆。 |
| ACPX | [GitHub](https://github.com/openclaw/acpx) | [![star](https://img.shields.io/badge/star-2790-f4b400?style=flat-square)](https://github.com/openclaw/acpx) | acp, client, sessions | 面向有状态 Agent Client Protocol 会话的无头 CLI 客户端。 |
| Microsoft Learn MCP | [GitHub](https://github.com/MicrosoftDocs/mcp) | [![star](https://img.shields.io/badge/star-1671-f4b400?style=flat-square)](https://github.com/MicrosoftDocs/mcp) | mcp, docs, grounding | 为代理接入微软文档知识提供的 MCP server 与 CLI。 |
| IBM MCP | [GitHub](https://github.com/IBM/mcp) | [![star](https://img.shields.io/badge/star-379-f4b400?style=flat-square)](https://github.com/IBM/mcp) | mcp, clients, tooling | IBM 提供的 MCP server、client 与开发工具集合。 |
| AGENT.md | [GitHub](https://github.com/agentmd/agent.md) | [![star](https://img.shields.io/badge/star-81-f4b400?style=flat-square)](https://github.com/agentmd/agent.md) | standard, agent-file, interoperability | 面向代理编码工具的标准化机器可读文件格式。 |

<a id="evaluation-harnesses-benchmarks"></a>
### Evaluation Harnesses & Benchmarks

| 项目 | 链接 | Stars | 标签 | 简介 |
| --- | --- | --- | --- | --- |
| Promptfoo | [GitHub](https://github.com/promptfoo/promptfoo) | [![star](https://img.shields.io/badge/star-21747-f4b400?style=flat-square)](https://github.com/promptfoo/promptfoo) | eval, red-team, ci | 配置驱动的 Prompt/Agent/RAG 测试、对比与红队评估工具。 |
| DeepEval | [GitHub](https://github.com/confident-ai/deepeval) | [![star](https://img.shields.io/badge/star-15819-f4b400?style=flat-square)](https://github.com/confident-ai/deepeval) | evaluation, framework, testing | 支持代理与工作流质量测试的 LLM 评估框架。 |
| RAGAS | [GitHub](https://github.com/vibrantlabsai/ragas) | [![star](https://img.shields.io/badge/star-14163-f4b400?style=flat-square)](https://github.com/vibrantlabsai/ragas) | rag, metrics, evaluation | 面向 LLM 与 RAG 质量指标的开源评测工具集。 |
| lm-evaluation-harness | [GitHub](https://github.com/EleutherAI/lm-evaluation-harness) | [![star](https://img.shields.io/badge/star-12760-f4b400?style=flat-square)](https://github.com/EleutherAI/lm-evaluation-harness) | benchmark, harness, llm | 广泛使用的 LLM 基准 harness，用于跨任务一致评估。 |
| SWE-bench | [GitHub](https://github.com/SWE-bench/SWE-bench) | [![star](https://img.shields.io/badge/star-5053-f4b400?style=flat-square)](https://github.com/SWE-bench/SWE-bench) | benchmark, swe, evaluation | 软件工程代理 issue 修复能力的标准评测基准。 |
| verifiers | [GitHub](https://github.com/PrimeIntellect-ai/verifiers) | [![star](https://img.shields.io/badge/star-4148-f4b400?style=flat-square)](https://github.com/PrimeIntellect-ai/verifiers) | verifier, rl, evaluation | 面向 RL 环境与 verifier 评测回路的库。 |
| AgentBench | [GitHub](https://github.com/THUDM/AgentBench) | [![star](https://img.shields.io/badge/star-3460-f4b400?style=flat-square)](https://github.com/THUDM/AgentBench) | benchmark, cross-domain, agent | 跨环境评测基准，用于衡量 LLM 代理的工具使用能力。 |
| LangWatch | [GitHub](https://github.com/langwatch/langwatch) | [![star](https://img.shields.io/badge/star-3274-f4b400?style=flat-square)](https://github.com/langwatch/langwatch) | simulation, evaluation, testing | 面向代理模拟、评测闭环与生产测试的端到端平台。 |
| EvalScope | [GitHub](https://github.com/modelscope/evalscope) | [![star](https://img.shields.io/badge/star-2868-f4b400?style=flat-square)](https://github.com/modelscope/evalscope) | benchmark, framework, llm | 可定制的大模型基准与性能评测框架。 |
| Terminal-Bench | [GitHub](https://github.com/harbor-framework/terminal-bench) | [![star](https://img.shields.io/badge/star-2299-f4b400?style=flat-square)](https://github.com/harbor-framework/terminal-bench) | terminal, benchmark, long-horizon | 面向长时与重验证任务的终端原生代理基准套件。 |
| Harbor | [GitHub](https://github.com/harbor-framework/harbor) | [![star](https://img.shields.io/badge/star-2207-f4b400?style=flat-square)](https://github.com/harbor-framework/harbor) | evaluation, harness, rl-env | 用于运行代理评测并构建类 RL 环境的框架。 |
| WebArena | [GitHub](https://github.com/web-arena-x/webarena) | [![star](https://img.shields.io/badge/star-1493-f4b400?style=flat-square)](https://github.com/web-arena-x/webarena) | web-agent, benchmark, environment | 可自托管的 Web 环境与评测 harness，用于对自治网页代理进行可复现的端到端任务评测。 |
| tau2-bench | [GitHub](https://github.com/sierra-research/tau2-bench) | [![star](https://img.shields.io/badge/star-1265-f4b400?style=flat-square)](https://github.com/sierra-research/tau2-bench) | tool-use, interaction, benchmark | 强调多步执行质量的工具-代理-用户交互基准。 |
| Meta-Harness | [GitHub](https://github.com/stanford-iris-lab/meta-harness) | [![star](https://img.shields.io/badge/star-1001-f4b400?style=flat-square)](https://github.com/stanford-iris-lab/meta-harness) | harness-search, optimization, terminal-bench | 面向任务特定模型 harness 的自动化搜索框架，并附带记忆系统与终端代理脚手架的参考实验。 |
| NeMo Gym | [GitHub](https://github.com/NVIDIA-NeMo/Gym) | [![star](https://img.shields.io/badge/star-929-f4b400?style=flat-square)](https://github.com/NVIDIA-NeMo/Gym) | rl-env, training, evaluation | 用于构建 LLM/代理训练与评测 RL 环境的工具集。 |
| TheAgentCompany | [GitHub](https://github.com/TheAgentCompany/TheAgentCompany) | [![star](https://img.shields.io/badge/star-715-f4b400?style=flat-square)](https://github.com/TheAgentCompany/TheAgentCompany) | benchmark, workplace, multi-step | 以模拟软件公司任务评测多步工作场景自治能力的 agent 基准。 |
| Claw-Eval | [GitHub](https://github.com/claw-eval/claw-eval) | [![star](https://img.shields.io/badge/star-626-f4b400?style=flat-square)](https://github.com/claw-eval/claw-eval) | benchmark, trajectory, safety | 面向自治代理的评测 harness 与基准，包含人工核验任务、轨迹审计，以及完成度、安全性与鲁棒性评分规则。 |
| Inspect Evals | [GitHub](https://github.com/UKGovernmentBEIS/inspect_evals) | [![star](https://img.shields.io/badge/star-518-f4b400?style=flat-square)](https://github.com/UKGovernmentBEIS/inspect_evals) | inspect, eval-suite, reproducibility | 面向 Inspect AI 工作流的评测套件集合。 |
| auto-harness | [GitHub](https://github.com/neosigmaai/auto-harness) | [![star](https://img.shields.io/badge/star-510-f4b400?style=flat-square)](https://github.com/neosigmaai/auto-harness) | optimization, regression, evals | 以基准门控的优化闭环，可自动挖掘失败样例、修改 agent 代码，并在夜间持续防回归。 |
| WildClawBench | [GitHub](https://github.com/InternLM/WildClawBench) | [![star](https://img.shields.io/badge/star-416-f4b400?style=flat-square)](https://github.com/InternLM/WildClawBench) | benchmark, harness-comparison, multimodal | 面向真实环境的评测基准，在真实 OpenClaw 环境中比较多种 agent harness 在多模态、编码、安全与生产力任务上的端到端表现。 |
| SWE-Bench Pro | [GitHub](https://github.com/scaleapi/SWE-bench_Pro-os) | [![star](https://img.shields.io/badge/star-411-f4b400?style=flat-square)](https://github.com/scaleapi/SWE-bench_Pro-os) | swe, benchmark, long-horizon | 面向 issue 驱动编码代理的长时软件工程基准，提供可复现的 Docker 化评测流程。 |
| Agent Evaluation | [GitHub](https://github.com/awslabs/agent-evaluation) | [![star](https://img.shields.io/badge/star-364-f4b400?style=flat-square)](https://github.com/awslabs/agent-evaluation) | evaluation, testing, ci | AWS 的虚拟代理测试框架，支持评估器驱动的多轮对话、钩子扩展与 CI 友好工作流。 |
| ClawBench | [GitHub](https://github.com/TIGER-AI-Lab/ClawBench) | [![star](https://img.shields.io/badge/star-349-f4b400?style=flat-square)](https://github.com/TIGER-AI-Lab/ClawBench) | browser-agent, benchmark, recording | 浏览器代理基准，覆盖真实网站任务、隔离容器、五层记录与 agentic 评分流程。 |
| WorkArena | [GitHub](https://github.com/ServiceNow/WorkArena) | [![star](https://img.shields.io/badge/star-251-f4b400?style=flat-square)](https://github.com/ServiceNow/WorkArena) | browser, benchmark, enterprise | 面向企业知识工作任务的浏览器代理基准。 |
| OpenHands Benchmarks | [GitHub](https://github.com/OpenHands/benchmarks) | [![star](https://img.shields.io/badge/star-85-f4b400?style=flat-square)](https://github.com/OpenHands/benchmarks) | openhands, eval, harness | OpenHands 体系的评测 harness 与基准定义。 |
| WebArena-Verified | [GitHub](https://github.com/ServiceNow/webarena-verified) | [![star](https://img.shields.io/badge/star-39-f4b400?style=flat-square)](https://github.com/ServiceNow/webarena-verified) | web-agent, benchmark, deterministic | 带确定性评测器的已验证 Web 代理基准。 |
| HarnessBench | [GitHub](https://github.com/reacher-z/HarnessBench) | [![star](https://img.shields.io/badge/star-11-f4b400?style=flat-square)](https://github.com/reacher-z/HarnessBench) | harness-comparison, browser-agent, benchmark | 用固定模型在相同日常网页任务上比较不同 agent harness 的基准，并为每个 harness 使用独立容器。 |

<a id="observability-reliability-operations"></a>
### Observability & Reliability Operations

| 项目 | 链接 | Stars | 标签 | 简介 |
| --- | --- | --- | --- | --- |
| Langfuse | [GitHub](https://github.com/langfuse/langfuse) | [![star](https://img.shields.io/badge/star-28260-f4b400?style=flat-square)](https://github.com/langfuse/langfuse) | llmops, tracing, metrics | 开源 LLM 工程平台，覆盖链路追踪、指标、提示词与评测。 |
| MLflow | [GitHub](https://github.com/mlflow/mlflow) | [![star](https://img.shields.io/badge/star-26212-f4b400?style=flat-square)](https://github.com/mlflow/mlflow) | platform, monitoring, evaluation | 通用 AI 工程平台，支持代理系统的监控与评测。 |
| Opik | [GitHub](https://github.com/comet-ml/opik) | [![star](https://img.shields.io/badge/star-19409-f4b400?style=flat-square)](https://github.com/comet-ml/opik) | monitoring, eval, tracing | 面向 LLM 应用与代理流程的端到端调试、评测与监控平台。 |
| RagaAI Catalyst | [GitHub](https://github.com/raga-ai-hub/RagaAI-Catalyst) | [![star](https://img.shields.io/badge/star-16169-f4b400?style=flat-square)](https://github.com/raga-ai-hub/RagaAI-Catalyst) | agentops, analytics, monitoring | 带时间线与执行图分析的代理可观测性监控框架。 |
| TensorZero | [GitHub](https://github.com/tensorzero/tensorzero) | [![star](https://img.shields.io/badge/star-11422-f4b400?style=flat-square)](https://github.com/tensorzero/tensorzero) | llmops, gateway, optimization | 开源 LLMOps 栈，统一网关、可观测性、评测与优化。 |
| Arize Phoenix | [GitHub](https://github.com/Arize-ai/phoenix) | [![star](https://img.shields.io/badge/star-9931-f4b400?style=flat-square)](https://github.com/Arize-ai/phoenix) | observability, tracing, evaluation | 开放的 AI 可观测性平台，支持追踪与评测分析。 |
| OpenLLMetry | [GitHub](https://github.com/traceloop/openllmetry) | [![star](https://img.shields.io/badge/star-7158-f4b400?style=flat-square)](https://github.com/traceloop/openllmetry) | opentelemetry, instrumentation, tracing | 基于 OpenTelemetry 的 GenAI/LLM 应用可观测性埋点方案。 |
| Helicone | [GitHub](https://github.com/Helicone/helicone) | [![star](https://img.shields.io/badge/star-5761-f4b400?style=flat-square)](https://github.com/Helicone/helicone) | monitoring, traffic, production | 轻量平台，用于生产环境 LLM 流量监控与评估。 |
| AgentOps SDK | [GitHub](https://github.com/AgentOps-AI/agentops) | [![star](https://img.shields.io/badge/star-5584-f4b400?style=flat-square)](https://github.com/AgentOps-AI/agentops) | agentops, monitoring, cost | 面向代理工作流的监控与基准 SDK，支持成本与链路追踪。 |
| Latitude | [GitHub](https://github.com/latitude-dev/latitude-llm) | [![star](https://img.shields.io/badge/star-4036-f4b400?style=flat-square)](https://github.com/latitude-dev/latitude-llm) | platform, eval, observability | 开源 agent 工程平台，集成评测与可观测性能力。 |
| Laminar | [GitHub](https://github.com/lmnr-ai/lmnr) | [![star](https://img.shields.io/badge/star-2961-f4b400?style=flat-square)](https://github.com/lmnr-ai/lmnr) | observability, tracing, evals | 面向代理系统的可观测平台，覆盖追踪、评测运行、监控与仪表盘。 |
| claude-code-reverse | [GitHub](https://github.com/Yuyz0112/claude-code-reverse) | [![star](https://img.shields.io/badge/star-2370-f4b400?style=flat-square)](https://github.com/Yuyz0112/claude-code-reverse) | trace, visualization, debugging | 可视化并分析 Claude Code 大模型交互链路的工具。 |
| Future AGI | [GitHub](https://github.com/future-agi/future-agi) | [![star](https://img.shields.io/badge/star-1064-f4b400?style=flat-square)](https://github.com/future-agi/future-agi) | observability, evaluation, guardrails | 可自托管的平台，将代理追踪、评测、模拟、护栏与网关运维闭环整合在一起。 |
| OpenInference | [GitHub](https://github.com/Arize-ai/openinference) | [![star](https://img.shields.io/badge/star-998-f4b400?style=flat-square)](https://github.com/Arize-ai/openinference) | spec, instrumentation, observability | 面向 AI 可观测性的开放埋点规范与工具。 |
| AgentSight | [GitHub](https://github.com/eunomia-bpf/AgentSight) | [![star](https://img.shields.io/badge/star-357-f4b400?style=flat-square)](https://github.com/eunomia-bpf/AgentSight) | ebpf, tracing, zero-instrumentation | 基于 eBPF 的零侵入 LLM 代理可观测性工具（支持主流编码代理），在系统调用层采集追踪数据，无需修改代理或工具。 |

<a id="guardrails-security-governance"></a>
### Guardrails, Security & Governance

| 项目 | 链接 | Stars | 标签 | 简介 |
| --- | --- | --- | --- | --- |
| LiteLLM | [GitHub](https://github.com/BerriAI/litellm) | [![star](https://img.shields.io/badge/star-48835-f4b400?style=flat-square)](https://github.com/BerriAI/litellm) | gateway, proxy, guardrails | 统一 LLM 网关/代理，支持成本追踪、负载均衡与护栏。 |
| Kong | [GitHub](https://github.com/Kong/kong) | [![star](https://img.shields.io/badge/star-43493-f4b400?style=flat-square)](https://github.com/Kong/kong) | gateway, policy, infra | API 与 AI 网关基础设施，可用于代理系统的策略执行。 |
| Parlant | [GitHub](https://github.com/emcie-co/parlant) | [![star](https://img.shields.io/badge/star-18093-f4b400?style=flat-square)](https://github.com/emcie-co/parlant) | interaction-control, guardrails, customer-agents | 面向客户交互代理的交互控制 harness，强调一致、可预测且可治理的 LLM 行为。 |
| Portkey Gateway | [GitHub](https://github.com/Portkey-AI/gateway) | [![star](https://img.shields.io/badge/star-11918-f4b400?style=flat-square)](https://github.com/Portkey-AI/gateway) | gateway, guardrails, routing | 支持多模型路由与护栏控制的 AI 网关。 |
| CAI (Cybersecurity AI) | [GitHub](https://github.com/aliasrobotics/cai) | [![star](https://img.shields.io/badge/star-8796-f4b400?style=flat-square)](https://github.com/aliasrobotics/cai) | security, governance, framework | 面向攻防场景的安全型代理框架。 |
| OpenAI Realtime Agents | [GitHub](https://github.com/openai/openai-realtime-agents) | [![star](https://img.shields.io/badge/star-6878-f4b400?style=flat-square)](https://github.com/openai/openai-realtime-agents) | realtime, orchestration, control | 展示高级实时代理模式，强调结构化控制与交互回路。 |
| Plano | [GitHub](https://github.com/katanemo/plano) | [![star](https://img.shields.io/badge/star-6552-f4b400?style=flat-square)](https://github.com/katanemo/plano) | proxy, safety, data-plane | 内置编排、安全与可观测性的 AI 原生代理与数据平面。 |
| OpenAI CS Agents Demo | [GitHub](https://github.com/openai/openai-cs-agents-demo) | [![star](https://img.shields.io/badge/star-6386-f4b400?style=flat-square)](https://github.com/openai/openai-cs-agents-demo) | demo, handoffs, governance | 客服多代理示例，展示交接流程与类似护栏的控制节点。 |
| ContextForge | [GitHub](https://github.com/IBM/mcp-context-forge) | [![star](https://img.shields.io/badge/star-3792-f4b400?style=flat-square)](https://github.com/IBM/mcp-context-forge) | gateway, governance, observability | 统一 MCP、A2A 与 REST/gRPC 端点的注册与代理层，提供集中治理与可观测能力。 |
| Archestra | [GitHub](https://github.com/archestra-ai/archestra) | [![star](https://img.shields.io/badge/star-3758-f4b400?style=flat-square)](https://github.com/archestra-ai/archestra) | enterprise, guardrails, governance | 企业级 AI 平台，提供护栏、MCP 注册中心与编排能力。 |
| Tracecat | [GitHub](https://github.com/TracecatHQ/tracecat) | [![star](https://img.shields.io/badge/star-3624-f4b400?style=flat-square)](https://github.com/TracecatHQ/tracecat) | security, automation, policy | 面向安全团队的 AI 自动化平台，提供策略与工作流控制。 |
| Agent Governance Toolkit | [GitHub](https://github.com/microsoft/agent-governance-toolkit) | [![star](https://img.shields.io/badge/star-3531-f4b400?style=flat-square)](https://github.com/microsoft/agent-governance-toolkit) | governance, policy, sandboxing | 面向运行时治理的工具包，可在代理动作执行前以确定性方式执行策略、身份、沙箱与审计控制。 |
| AgentGateway | [GitHub](https://github.com/agentgateway/agentgateway) | [![star](https://img.shields.io/badge/star-2930-f4b400?style=flat-square)](https://github.com/agentgateway/agentgateway) | gateway, mcp, proxy | 面向 AI 代理与 MCP 生态的代理网关。 |
| ClawManager | [GitHub](https://github.com/Yuan-lab-LLM/ClawManager) | [![star](https://img.shields.io/badge/star-1616-f4b400?style=flat-square)](https://github.com/Yuan-lab-LLM/ClawManager) | control-plane, governance, runtimes | 面向 Kubernetes 的控制平面，用于治理多种 agent 后端的运行时、AI Gateway 访问与可复用技能资源。 |
| Agent Vault | [GitHub](https://github.com/Infisical/agent-vault) | [![star](https://img.shields.io/badge/star-1521-f4b400?style=flat-square)](https://github.com/Infisical/agent-vault) | credentials, egress-policy, proxy | 面向代理的凭据代理与金库，在不暴露真实密钥的情况下代管 API 访问，并提供出站过滤与请求日志。 |
| Haft | [GitHub](https://github.com/m0n0x41d/haft) | [![star](https://img.shields.io/badge/star-1335-f4b400?style=flat-square)](https://github.com/m0n0x41d/haft) | governance, decisions, mcp | 面向决策治理的 harness，在代理执行前沉淀可证伪契约、证据与 commission 生命周期。 |
| Sponsio | [GitHub](https://github.com/SponsioLabs/Sponsio) | [![star](https://img.shields.io/badge/star-469-f4b400?style=flat-square)](https://github.com/SponsioLabs/Sponsio) | contracts, runtime-safety, guardrails | 运行时强制执行层，在代理动作执行前用确定性契约逐项检查。 |
| DashClaw | [GitHub](https://github.com/ucsandman/DashClaw) | [![star](https://img.shields.io/badge/star-269-f4b400?style=flat-square)](https://github.com/ucsandman/DashClaw) | approvals, policy, audit | 面向代理的治理层，可拦截高风险动作、执行策略、路由审批，并记录可审计的决策轨迹。 |
| ActPlane | [GitHub](https://github.com/eunomia-bpf/ActPlane) | [![star](https://img.shields.io/badge/star-19-f4b400?style=flat-square)](https://github.com/eunomia-bpf/ActPlane) | ebpf, kernel, policy | 操作系统级代理约束工具，将策略 DSL 编译为 eBPF 引擎，在系统调用边界执行带标签的信息流控制并提供纠正反馈。 |

<a id="reference-harness-implementations"></a>
### Reference Harness Implementations

| 项目 | 链接 | Stars | 标签 | 简介 |
| --- | --- | --- | --- | --- |
| OpenClaw | [GitHub](https://github.com/openclaw/openclaw) | [![star](https://img.shields.io/badge/star-375821-f4b400?style=flat-square)](https://github.com/openclaw/openclaw) | gateway, channels, sandboxing | 本地优先的个人助手 harness，通过 gateway 控制平面管理会话、通道、工具、事件、技能与非主会话沙箱。 |
| Claw Code | [GitHub](https://github.com/ultraworkers/claw-code) | [![star](https://img.shields.io/badge/star-192977-f4b400?style=flat-square)](https://github.com/ultraworkers/claw-code) | rust, cli, sessions | claw CLI agent harness 的公开 Rust 实现，覆盖认证、会话、兼容性检查、容器工作流与终端执行指引。 |
| Hermes Agent | [GitHub](https://github.com/NousResearch/hermes-agent) | [![star](https://img.shields.io/badge/star-174411-f4b400?style=flat-square)](https://github.com/NousResearch/hermes-agent) | memory, skills, subagents | 自改进代理运行时，提供记忆、技能创建、子代理、定时自动化与可插拔终端后端。 |
| OpenCode | [GitHub](https://github.com/anomalyco/opencode) | [![star](https://img.shields.io/badge/star-167726-f4b400?style=flat-square)](https://github.com/anomalyco/opencode) | terminal, coding-agent, subagents | 开源编码代理，提供内置 plan/build 角色、子代理、LSP 支持与客户端-服务端运行时。 |
| Claude Code | [GitHub](https://github.com/anthropics/claude-code) | [![star](https://img.shields.io/badge/star-128713-f4b400?style=flat-square)](https://github.com/anthropics/claude-code) | terminal, coding-agent, git-workflows | 官方终端编码代理，可理解代码库并通过自然语言执行编辑、调试与 Git 工作流。 |
| Gemini CLI | [GitHub](https://github.com/google-gemini/gemini-cli) | [![star](https://img.shields.io/badge/star-104785-f4b400?style=flat-square)](https://github.com/google-gemini/gemini-cli) | terminal, coding-agent, mcp | 开源终端代理，提供内置工具、MCP 支持、会话检查点与沙箱控制能力。 |
| Browser Use | [GitHub](https://github.com/browser-use/browser-use) | [![star](https://img.shields.io/badge/star-96393-f4b400?style=flat-square)](https://github.com/browser-use/browser-use) | browser-agent, automation, benchmarks | 浏览器代理框架，通过浏览器状态、工具、云浏览器与基准任务运行，让 LLM 能稳定操作网站。 |
| Codex CLI | [GitHub](https://github.com/openai/codex) | [![star](https://img.shields.io/badge/star-87277-f4b400?style=flat-square)](https://github.com/openai/codex) | terminal, coding-agent, local-execution | 终端原生的本地编码代理，提供面向软件任务的实用 agent 工作流。 |
| LobeHub | [GitHub](https://github.com/lobehub/lobehub) | [![star](https://img.shields.io/badge/star-78018-f4b400?style=flat-square)](https://github.com/lobehub/lobehub) | operator, multi-agent, scheduling | 面向多代理工作流的 Chief Agent Operator 平台，用于调度、运行与汇报代理工作。 |
| OpenHands | [GitHub](https://github.com/OpenHands/OpenHands) | [![star](https://img.shields.io/badge/star-75472-f4b400?style=flat-square)](https://github.com/OpenHands/OpenHands) | coding-agent, software-engineering, repo | 开源 AI 软件工程代理，聚焦仓库级编码任务执行。 |
| Paperclip | [GitHub](https://github.com/paperclipai/paperclip) | [![star](https://img.shields.io/badge/star-68452-f4b400?style=flat-square)](https://github.com/paperclipai/paperclip) | managed-agents, control-plane, governance | 面向 agent 团队协作的 managed-agent 控制平面，提供组织结构、工单、预算、心跳调度与审计轨迹。 |
| learn-claude-code | [GitHub](https://github.com/shareAI-lab/learn-claude-code) | [![star](https://img.shields.io/badge/star-63835-f4b400?style=flat-square)](https://github.com/shareAI-lab/learn-claude-code) | tutorial, harness, claude-code | 从 0 到 1 构建 Claude Code 类系统的实战 harness 教程。 |
| Cline | [GitHub](https://github.com/cline/cline) | [![star](https://img.shields.io/badge/star-62573-f4b400?style=flat-square)](https://github.com/cline/cline) | coding-agent, mcp, checkpoints | 开源编码代理，覆盖 IDE、终端、SDK 与看板等入口，并共享审批、MCP、检查点与代理团队能力。 |
| pi | [GitHub](https://github.com/earendil-works/pi) | [![star](https://img.shields.io/badge/star-58076-f4b400?style=flat-square)](https://github.com/earendil-works/pi) | coding-agent, runtime, monorepo | 将编码代理 CLI、共享运行时与多模型 LLM 栈整合在一起的 agent harness monorepo。 |
| OpenManus | [GitHub](https://github.com/FoundationAgents/OpenManus) | [![star](https://img.shields.io/badge/star-56422-f4b400?style=flat-square)](https://github.com/FoundationAgents/OpenManus) | general-agent, autonomy, workflows | 面向广义自治任务的开放基础系统，覆盖编码等复杂场景。 |
| aider | [GitHub](https://github.com/Aider-AI/aider) | [![star](https://img.shields.io/badge/star-45588-f4b400?style=flat-square)](https://github.com/Aider-AI/aider) | terminal, repo-map, testing | 终端编码助手，提供仓库映射、Git 感知编辑与内置 lint/test 反馈回路。 |
| CowAgent | [GitHub](https://github.com/zhayujie/CowAgent) | [![star](https://img.shields.io/badge/star-44984-f4b400?style=flat-square)](https://github.com/zhayujie/CowAgent) | reference, skills, multi-channel | 参考级 agent harness 实现，包含规划、记忆、知识库、技能、工具、MCP 集成、调度、浏览器自动化与多渠道交付。 |
| CLI-Anything | [GitHub](https://github.com/HKUDS/CLI-Anything) | [![star](https://img.shields.io/badge/star-41482-f4b400?style=flat-square)](https://github.com/HKUDS/CLI-Anything) | cli, tool-use, automation | 在代理回路中统一命令行工具使用的 CLI agent 系统。 |
| Claude Code Plugins: Orchestration and Automation | [GitHub](https://github.com/wshobson/agents) | [![star](https://img.shields.io/badge/star-36178-f4b400?style=flat-square)](https://github.com/wshobson/agents) | claude-code, plugins, orchestration | 面向 Claude Code 的生产级插件仓库，整合 agents、skills、tools 与多代理工作流编排器。 |
| Agent TARS | [GitHub](https://github.com/bytedance/UI-TARS-desktop) | [![star](https://img.shields.io/badge/star-35793-f4b400?style=flat-square)](https://github.com/bytedance/UI-TARS-desktop) | computer-use, browser-agent, mcp | 多模态电脑与浏览器代理栈，提供 CLI/Web UI、GUI/DOM 混合浏览器控制、MCP 工具、事件流与沙箱支持。 |
| oh-my-claudecode | [GitHub](https://github.com/Yeachan-Heo/oh-my-claudecode) | [![star](https://img.shields.io/badge/star-35416-f4b400?style=flat-square)](https://github.com/Yeachan-Heo/oh-my-claudecode) | claude-code, multi-agent, worktrees | 面向 Claude Code 的团队优先编排层，提供分阶段多代理执行、worktree 感知配置与持久化会话产物。 |
| Multica | [GitHub](https://github.com/multica-ai/multica) | [![star](https://img.shields.io/badge/star-34362-f4b400?style=flat-square)](https://github.com/multica-ai/multica) | managed-agents, coding-agent, runtimes | 将 issue 分配给编码代理、通过 runtime 路由执行并沉淀可复用技能的 managed-agent 平台。 |
| ZeroClaw | [GitHub](https://github.com/zeroclaw-labs/zeroclaw) | [![star](https://img.shields.io/badge/star-31659-f4b400?style=flat-square)](https://github.com/zeroclaw-labs/zeroclaw) | runtime, approval-gates, sandboxing | 单二进制 agent runtime，提供模型供应商、渠道、工具、记忆、SOP、审批门禁、沙箱、ACP 与工具回执。 |
| oh-my-codex | [GitHub](https://github.com/Yeachan-Heo/oh-my-codex) | [![star](https://img.shields.io/badge/star-30038-f4b400?style=flat-square)](https://github.com/Yeachan-Heo/oh-my-codex) | codex, workflow, worktrees | 面向 OpenAI Codex CLI 的工作流层，提供更强启动、从澄清到完成的标准流程、持久状态、技能、钩子与 worktree 启动。 |
| NanoClaw | [GitHub](https://github.com/qwibitai/nanoclaw) | [![star](https://img.shields.io/badge/star-29556-f4b400?style=flat-square)](https://github.com/qwibitai/nanoclaw) | containers, claude-sdk, scheduling | 基于容器隔离的 Claude 代理 harness，提供多通道路由、定时任务、按群组隔离的记忆，以及小代码库定制能力。 |
| Vibe Kanban | [GitHub](https://github.com/BloopAI/vibe-kanban) | [![star](https://img.shields.io/badge/star-26686-f4b400?style=flat-square)](https://github.com/BloopAI/vibe-kanban) | coding-agent, workspaces, review | 面向编码代理的看板控制平面，用于在隔离工作区中规划、运行、审查并合并代理产出。 |
| Qwen Code | [GitHub](https://github.com/QwenLM/qwen-code) | [![star](https://img.shields.io/badge/star-24793-f4b400?style=flat-square)](https://github.com/QwenLM/qwen-code) | terminal, coding-agent, cli | 终端原生开源编码代理，面向实际开发循环优化。 |
| SuperClaude Framework | [GitHub](https://github.com/SuperClaude-Org/SuperClaude_Framework) | [![star](https://img.shields.io/badge/star-23090-f4b400?style=flat-square)](https://github.com/SuperClaude-Org/SuperClaude_Framework) | config, personas, workflow | 为编码代理增强命令、角色与方法模板的配置框架。 |
| cmux | [GitHub](https://github.com/manaflow-ai/cmux) | [![star](https://img.shields.io/badge/star-20542-f4b400?style=flat-square)](https://github.com/manaflow-ai/cmux) | macos, workspace, browser | 面向 AI 编码代理的原生 macOS 终端与浏览器工作区，提供通知、分屏与可脚本化控制。 |
| Devika | [GitHub](https://github.com/stitionai/devika) | [![star](https://img.shields.io/badge/star-19509-f4b400?style=flat-square)](https://github.com/stitionai/devika) | assistant, planning, coding | 开源编码助手系统，支持任务规划与实现。 |
| SWE-agent | [GitHub](https://github.com/SWE-agent/SWE-agent) | [![star](https://img.shields.io/badge/star-19375-f4b400?style=flat-square)](https://github.com/SWE-agent/SWE-agent) | swe, issue-fixing, tooling | 研究级编码代理，通过明确的工具回路自动修复 GitHub issue。 |
| Compound Engineering | [GitHub](https://github.com/EveryInc/compound-engineering-plugin) | [![star](https://img.shields.io/badge/star-18598-f4b400?style=flat-square)](https://github.com/EveryInc/compound-engineering-plugin) | plugins, worktrees, review | 面向多种 coding agent 的工程插件，将 brainstorm、planning、worktree 执行、review 与知识沉淀回路标准化。 |
| OpenFang | [GitHub](https://github.com/RightNow-AI/openfang) | [![star](https://img.shields.io/badge/star-17692-f4b400?style=flat-square)](https://github.com/RightNow-AI/openfang) | agent-os, guardrails, rust | Rust agent 操作系统，包含自治能力包、manifest、护栏、工具、记忆、沙箱、审计链路与渠道适配器。 |
| Aperant | [GitHub](https://github.com/AndyMik90/Aperant) | [![star](https://img.shields.io/badge/star-14312-f4b400?style=flat-square)](https://github.com/AndyMik90/Aperant) | coding-agent, parallel, memory | 自治多代理编码框架，提供并行执行、隔离工作区、质量校验回路与持久记忆。 |
| Eigent | [GitHub](https://github.com/eigent-ai/eigent) | [![star](https://img.shields.io/badge/star-14167-f4b400?style=flat-square)](https://github.com/eigent-ai/eigent) | desktop, cowork, productivity | 开源桌面协作代理，可执行自治任务并提升开发生产力。 |
| OpenHarness | [GitHub](https://github.com/HKUDS/OpenHarness) | [![star](https://img.shields.io/badge/star-13345-f4b400?style=flat-square)](https://github.com/HKUDS/OpenHarness) | tool-use, memory, multi-agent | 开放式 agent harness 实现，覆盖工具调用、技能、记忆、权限与多代理协作。 |
| IronClaw | [GitHub](https://github.com/nearai/ironclaw) | [![star](https://img.shields.io/badge/star-12376-f4b400?style=flat-square)](https://github.com/nearai/ironclaw) | security, wasm, routines | 安全优先的个人 agent harness，集成 WASM 沙箱、例程调度、工具插件与持久记忆。 |
| Agent S | [GitHub](https://github.com/simular-ai/Agent-S) | [![star](https://img.shields.io/badge/star-11719-f4b400?style=flat-square)](https://github.com/simular-ai/Agent-S) | computer-use, gui-agent, evaluation | 开源 computer-use 代理框架，支持 grounding 模型、反思、本地代码执行选项，以及 OSWorld 风格评测。 |
| Superset | [GitHub](https://github.com/superset-sh/superset) | [![star](https://img.shields.io/badge/star-11458-f4b400?style=flat-square)](https://github.com/superset-sh/superset) | worktrees, desktop, parallel | 基于 worktree 的桌面编排器，可在统一工作区中并行运行并审阅多个 CLI 编码代理。 |
| GitHub Copilot CLI | [GitHub](https://github.com/github/copilot-cli) | [![star](https://img.shields.io/badge/star-10656-f4b400?style=flat-square)](https://github.com/github/copilot-cli) | terminal, coding-agent, mcp | 官方终端编码代理，基于 GitHub Copilot harness，提供 MCP 扩展、审批控制与 GitHub 原生上下文。 |
| Open SWE | [GitHub](https://github.com/langchain-ai/open-swe) | [![star](https://img.shields.io/badge/star-9894-f4b400?style=flat-square)](https://github.com/langchain-ai/open-swe) | async, coding-agent, swe | 面向软件问题流的异步开源编码代理。 |
| oh-my-pi | [GitHub](https://github.com/can1357/oh-my-pi) | [![star](https://img.shields.io/badge/star-9023-f4b400?style=flat-square)](https://github.com/can1357/oh-my-pi) | terminal, lsp, subagents | 终端 AI 编码代理，包含编辑安全、LSP 集成与子代理支持。 |
| Agent Orchestrator | [GitHub](https://github.com/ComposioHQ/agent-orchestrator) | [![star](https://img.shields.io/badge/star-7342-f4b400?style=flat-square)](https://github.com/ComposioHQ/agent-orchestrator) | worktrees, parallel, dashboard | 基于 worktree 的并行编码代理编排层，可自治处理 CI 与评审反馈。 |
| Paseo | [GitHub](https://github.com/getpaseo/paseo) | [![star](https://img.shields.io/badge/star-7015-f4b400?style=flat-square)](https://github.com/getpaseo/paseo) | coding-agent, daemon, multi-device | 面向多设备的编码代理守护进程与客户端栈，用于编排本地代理、并行运行与跨模型工作流。 |
| jcode | [GitHub](https://github.com/1jehuang/jcode) | [![star](https://img.shields.io/badge/star-6779-f4b400?style=flat-square)](https://github.com/1jehuang/jcode) | coding-agent, terminal, rust | 面向多会话工作流、可定制性、记忆与终端性能优化的 Rust 编码代理 harness。 |
| 1Code | [GitHub](https://github.com/21st-dev/1code) | [![star](https://img.shields.io/badge/star-5548-f4b400?style=flat-square)](https://github.com/21st-dev/1code) | coding-agent, orchestration, worktrees | 桌面优先的编码代理编排器，提供 worktree 隔离、后台沙箱、MCP 工具管理与自动化触发。 |
| OSAURUS | [GitHub](https://github.com/osaurus-ai/osaurus) | [![star](https://img.shields.io/badge/star-5536-f4b400?style=flat-square)](https://github.com/osaurus-ai/osaurus) | macos, local-first, memory | 面向 macOS 的本地自治编码代理 harness，支持持久记忆。 |
| holaOS | [GitHub](https://github.com/holaboss-ai/holaOS) | [![star](https://img.shields.io/badge/star-5461-f4b400?style=flat-square)](https://github.com/holaboss-ai/holaOS) | long-horizon, desktop, durable-state | 面向长时任务的桌面优先 agent environment，整合运行时、记忆、工具、应用与持久状态。 |
| mini-swe-agent | [GitHub](https://github.com/SWE-agent/mini-swe-agent) | [![star](https://img.shields.io/badge/star-4751-f4b400?style=flat-square)](https://github.com/SWE-agent/mini-swe-agent) | minimal, swe, coding-agent | 极简编码代理实现，同时具备较强基准表现。 |
| HiClaw | [GitHub](https://github.com/agentscope-ai/HiClaw) | [![star](https://img.shields.io/badge/star-4710-f4b400?style=flat-square)](https://github.com/agentscope-ai/HiClaw) | multi-agent, human-in-the-loop, shared-state | 协作式多代理操作系统，通过 Matrix 房间提供管理者-工作者协同、共享状态与人在回路监督。 |
| Webwright | [GitHub](https://github.com/microsoft/Webwright) | [![star](https://img.shields.io/badge/star-4572-f4b400?style=flat-square)](https://github.com/microsoft/Webwright) | browser-agent, code-as-action, playwright | 轻量浏览器代理 harness，让编码模型通过在工作区编写可重跑的 Playwright 脚本来完成网页任务。 |
| Harness | [GitHub](https://github.com/revfactory/harness) | [![star](https://img.shields.io/badge/star-4482-f4b400?style=flat-square)](https://github.com/revfactory/harness) | claude-code, meta-factory, agent-teams | 面向 Claude Code 的元工厂，可根据项目描述生成领域化代理团队、技能、编排模式与验证步骤。 |
| TinyAGI | [GitHub](https://github.com/TinyAGI/tinyagi) | [![star](https://img.shields.io/badge/star-3570-f4b400?style=flat-square)](https://github.com/TinyAGI/tinyagi) | team-orchestration, autonomous, workflows | 面向“一人公司”场景的团队化代理编排器。 |
| Open Claude Cowork | [GitHub](https://github.com/DevAgentForge/Open-Claude-Cowork) | [![star](https://img.shields.io/badge/star-3292-f4b400?style=flat-square)](https://github.com/DevAgentForge/Open-Claude-Cowork) | desktop, ui, orchestration | 桌面化协作编码助手，将代理编排能力图形化。 |
| Maestro | [GitHub](https://github.com/RunMaestro/Maestro) | [![star](https://img.shields.io/badge/star-2968-f4b400?style=flat-square)](https://github.com/RunMaestro/Maestro) | desktop, worktrees, orchestration | 面向并行编码代理的桌面指挥台，集成 worktree 隔离、任务队列、自动运行 playbook 与会话复用。 |
| Amazon Bedrock AgentCore Samples | [GitHub](https://github.com/awslabs/agentcore-samples) | [![star](https://img.shields.io/badge/star-2899-f4b400?style=flat-square)](https://github.com/awslabs/agentcore-samples) | aws, runtime, operations | 官方示例套件，覆盖基于 Runtime、Gateway、Memory、可观测、评测与策略层的代理部署与运维。 |
| Google Agents CLI | [GitHub](https://github.com/google/agents-cli) | [![star](https://img.shields.io/badge/star-2665-f4b400?style=flat-square)](https://github.com/google/agents-cli) | google-cloud, lifecycle, skills | Google Cloud 的 CLI 与技能包，为编码代理提供脚手架、评测、部署、发布和可观测工作流。 |
| AI-DLC Workflows | [GitHub](https://github.com/awslabs/aidlc-workflows) | [![star](https://img.shields.io/badge/star-2560-f4b400?style=flat-square)](https://github.com/awslabs/aidlc-workflows) | workflow-rules, quality-gates, steering | AWS 官方工作流规则集，通过自适应阶段、质量门禁与面向 IDE 的上下文文件来约束编码代理。 |
| Open Cowork | [GitHub](https://github.com/OpenCoworkAI/open-cowork) | [![star](https://img.shields.io/badge/star-1459-f4b400?style=flat-square)](https://github.com/OpenCoworkAI/open-cowork) | desktop, sandbox, mcp | 桌面代理应用，集成 VM 级沙箱、MCP 连接器、GUI 控制与内置技能工作流。 |
| thClaws | [GitHub](https://github.com/thClaws/thClaws) | [![star](https://img.shields.io/badge/star-1058-f4b400?style=flat-square)](https://github.com/thClaws/thClaws) | rust, workspace, skills | 原生 Rust 代理工作区，提供共享代理循环、会话、工具、技能、MCP、记忆、钩子与沙箱。 |
| mini-coding-agent | [GitHub](https://github.com/rasbt/mini-coding-agent) | [![star](https://img.shields.io/badge/star-891-f4b400?style=flat-square)](https://github.com/rasbt/mini-coding-agent) | coding-agent, minimal, approvals | 极简编码 agent harness，实现了审批、记忆、受限委派与持久化转录等核心机制。 |
| codex-autorunner | [GitHub](https://github.com/Git-on-my-level/codex-autorunner) | [![star](https://img.shields.io/badge/star-808-f4b400?style=flat-square)](https://github.com/Git-on-my-level/codex-autorunner) | meta-harness, tickets, long-running | 将 ticket 作为控制平面的长时编码代理 meta-harness，提供队列执行、hub 控制台与聊天通知。 |
| MateClaw | [GitHub](https://github.com/matevip/mateclaw) | [![star](https://img.shields.io/badge/star-537-f4b400?style=flat-square)](https://github.com/matevip/mateclaw) | self-hosted, approvals, channels | 自托管多用户 agent harness，集成 StateGraph 推理、技能、MCP/ACP 注册表、审批、审计轨迹与多通道适配。 |
| OpenClaw.NET | [GitHub](https://github.com/clawdotnet/openclaw.net) | [![star](https://img.shields.io/badge/star-357-f4b400?style=flat-square)](https://github.com/clawdotnet/openclaw.net) | dotnet, gateway, governance | NativeAOT 友好的 .NET 代理运行时与网关，提供工具、记忆、MCP、治理账本、证据包与 harness 回归测试。 |
| Utah | [GitHub](https://github.com/inngest/utah) | [![star](https://img.shields.io/badge/star-117-f4b400?style=flat-square)](https://github.com/inngest/utah) | durable-execution, event-driven, multi-channel | 基于 Inngest 的持久代理 harness，提供思考-行动-观察循环、步骤级重试、单例并发、取消与多通道适配。 |

<a id="essential-readings-ecosystem-maps"></a>
### Essential Readings & Ecosystem Maps

| 项目 | 链接 | Stars | 标签 | 简介 |
| --- | --- | --- | --- | --- |
| awesome-claude-code | [GitHub](https://github.com/hesreallyhim/awesome-claude-code) | [![star](https://img.shields.io/badge/star-45304-f4b400?style=flat-square)](https://github.com/hesreallyhim/awesome-claude-code) | awesome-list, claude-code, skills | Claude Code 技能、钩子与编排工具的社区清单。 |
| awesome-agentic-patterns | [GitHub](https://github.com/nibzard/awesome-agentic-patterns) | [![star](https://img.shields.io/badge/star-4608-f4b400?style=flat-square)](https://github.com/nibzard/awesome-agentic-patterns) | awesome-list, patterns, design | 可复用的 agentic 设计模式与实现范式目录。 |
| awesome-mcp-servers | [GitHub](https://github.com/wong2/awesome-mcp-servers) | [![star](https://img.shields.io/badge/star-4122-f4b400?style=flat-square)](https://github.com/wong2/awesome-mcp-servers) | awesome-list, mcp, tools | MCP server 精选索引，便于代理系统进行工具互操作。 |
| awesome-harness-engineering | [GitHub](https://github.com/walkinglabs/awesome-harness-engineering) | [![star](https://img.shields.io/badge/star-2866-f4b400?style=flat-square)](https://github.com/walkinglabs/awesome-harness-engineering) | awesome-list, curation, harness | 聚焦 harness engineering 的精选清单，覆盖文章、基准与实现。 |
| 12 Factor Agents | [Reference](https://www.humanlayer.dev/blog/12-factor-agents) | - | reading, operations, principles | 面向生产代理可维护性的运维原则总结。 |
| Agent Frameworks, Runtimes, and Harnesses, oh my! | [Reference](https://blog.langchain.com/agent-frameworks-runtimes-and-harnesses-oh-my/) | - | reading, langchain, architecture | 清晰拆解 framework、runtime 与 harness 的职责边界。 |
| An open-source spec for Codex orchestration: Symphony. | [Reference](https://openai.com/index/open-source-codex-orchestration-symphony/) | - | reading, openai, orchestration | OpenAI 对编排层的实践拆解，介绍如何把 issue 跟踪器变成面向编码代理的常驻控制平面。 |
| Building agents with the Claude Agent SDK | [Reference](https://claude.com/blog/building-agents-with-the-claude-agent-sdk) | - | reading, claude, sdk | Claude 官方博客，介绍面向生产的 SDK 会话、工具与编排实践。 |
| Building Effective AI Agents | [Reference](https://www.anthropic.com/engineering/building-effective-agents) | - | reading, anthropic, agents | Anthropic 关于何时使用工作流或自治代理以及如何组织系统的实践指南。 |
| Claude Code auto mode | [Reference](https://www.anthropic.com/engineering/claude-code-auto-mode) | - | reading, anthropic, permissions | Anthropic 介绍如何用分类器接管审批，在更高自治度下维持更安全的编码代理运行。 |
| Code execution with MCP | [Reference](https://www.anthropic.com/engineering/code-execution-with-mcp) | - | reading, anthropic, mcp | Anthropic 关于通过 MCP 边界进行受控代码执行的工程设计说明。 |
| Demystifying Evals for AI Agents | [Reference](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) | - | reading, evals, anthropic | 讲解在非确定性轨迹下设计稳健代理评测的方法论。 |
| Effective context engineering for AI agents | [Reference](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) | - | reading, context, anthropic | 介绍代理系统中的上下文预算与工作状态管理方法。 |
| Effective harnesses for long-running agents | [Reference](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents) | - | reading, long-running, anthropic | 讲解长时代理运行中状态维护、可恢复性与可靠性的实践指南。 |
| Evaluating Deep Agents: Our Learnings | [Reference](https://blog.langchain.com/evaluating-deep-agents-our-learnings/) | - | reading, langchain, evaluation | LangChain 关于有状态、长时代理评测设计的实战经验总结。 |
| Harness design for long-running application development | [Reference](https://www.anthropic.com/engineering/harness-design-long-running-apps) | - | reading, app-dev, anthropic | 关于通过 harness 结构改进长任务应用生成的后续文章。 |
| Harness Engineering (Martin Fowler) | [Reference](https://martinfowler.com/articles/exploring-gen-ai/harness-engineering.html) | - | reading, architecture, fowler | 从架构视角讨论 harness engineering 与系统熵控制。 |
| Harness engineering (OpenAI) | [Reference](https://openai.com/index/harness-engineering/) | - | reading, methodology, openai | 关于如何通过约束与验证构建可靠 agent-first 软件的实践报告。 |
| How we built our multi-agent research system | [Reference](https://www.anthropic.com/engineering/multi-agent-research-system) | - | reading, anthropic, multi-agent | Anthropic 对多代理系统中角色分工与协同机制的架构复盘。 |
| Improving Deep Agents with harness engineering | [Reference](https://blog.langchain.com/improving-deep-agents-with-harness-engineering/) | - | reading, langchain, harness | 说明仅通过 harness 改进也能显著提升基准表现。 |
| Making Claude Code more secure and autonomous with sandboxing | [Reference](https://www.anthropic.com/engineering/claude-code-sandboxing) | - | reading, anthropic, sandboxing | 讲解 Anthropic 如何借助沙箱边界在不放松安全控制的前提下提升代理自治性。 |
| Quantifying infrastructure noise in agentic coding evals | [Reference](https://www.anthropic.com/engineering/infrastructure-noise) | - | reading, anthropic, evaluation | 分析基础设施选择如何显著影响编码代理基准结果。 |
| Scaling Managed Agents: Decoupling the brain from the hands | [Reference](https://www.anthropic.com/engineering/managed-agents) | - | reading, anthropic, architecture | Anthropic 提出的 meta-harness 架构，将长任务代理中的 session 日志、harness 循环与 sandbox 解耦。 |
| Skill Issue: Harness Engineering for Coding Agents | [Reference](https://www.humanlayer.dev/blog/skill-issue-harness-engineering-for-coding-agents) | - | reading, humanlayer, coding-agents | 实践向拆解：编码代理效果很大程度取决于 harness 的工程配置。 |
| Testing Agent Skills Systematically with Evals | [Reference](https://developers.openai.com/blog/eval-skills) | - | reading, openai, evals | OpenAI Developers 指南：将代理轨迹转化为可重复的技能评测。 |
| The Anatomy of an Agent Harness | [Reference](https://blog.langchain.com/the-anatomy-of-an-agent-harness/) | - | reading, architecture, langchain | 对 agent harness 组件及其职责的结构化拆解。 |
| Unrolling the Codex agent loop | [Reference](https://openai.com/index/unrolling-the-codex-agent-loop/) | - | reading, openai, architecture | OpenAI 工程向拆解 Codex harness 回路，涵盖提示增长、工具调用回放与无状态执行权衡。 |
| Writing effective tools for AI agents | [Reference](https://www.anthropic.com/engineering/writing-tools-for-agents) | - | reading, anthropic, tools | 讲解如何设计工具接口，使代理更稳定且更安全地调用工具。 |
| Your Agent Needs a Harness, Not a Framework | [Reference](https://www.inngest.com/blog/your-agent-needs-a-harness-not-a-framework) | - | reading, inngest, reliability | 强调代理系统应优先建设可靠性基础设施，而非仅依赖框架思维。 |

## 维护说明

- 单一数据源: `data/projects.yaml`
- 重新生成 README: `python3 scripts/render_readme.py`
- 校验条目与链接: `python3 scripts/verify_catalog.py`

## 引用

```bibtex
@misc{li2026agentharness,
  title={Agent Harness Engineering: A Survey},
  author={Li, Junjie and Xiao, Xi and Zhang, Yunbei and Liu, Chen and Zhao, Lin and Liao, Xiaoying and Ji, Yingrui and Wang, Janet and Gu, Jianyang and Ge, Yingqiang and Xu, Weijie and Fang, Xi and Xu, Xiang and Zhao, Tianchen and Kim, Youngeun and Wang, Tianyang and Hamm, Jihun and Krishnaswamy, Smita and Huan, Jun and Reddy, Chandan},
  url={https://openreview.net/pdf?id=eONq7FdiHa},
  year={2026}
}
```

# Awesome Agent Harness

一个面向 **Agent Harness Engineering** 的工程实践清单，优先收录可直接落地的 GitHub 项目。

- 当前条目数: **172**
- GitHub 条目: **147 (85.5%)**
- 项目分类 GitHub 占比（不含阅读类）: **143/143 (100.0%)**
- 分类数量: **9**
- 最近核对日期: **2026-05-08**
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
| Harness Architecture & Orchestration | 21 |
| Context & Working-State Engineering | 9 |
| Execution Substrates & Sandboxing | 18 |
| Protocols, Tool Interfaces & Agent Contracts | 11 |
| Evaluation Harnesses & Benchmarks | 21 |
| Observability & Reliability Operations | 14 |
| Guardrails, Security & Governance | 12 |
| Reference Harness Implementations | 37 |
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
| DeerFlow | [GitHub](https://github.com/bytedance/deer-flow) | [![star](https://img.shields.io/badge/star-66070-f4b400?style=flat-square)](https://github.com/bytedance/deer-flow) | long-horizon, memory, subagents | 面向长任务的 SuperAgent harness，整合记忆、工具、子代理与沙箱。 |
| AutoGen | [GitHub](https://github.com/microsoft/autogen) | [![star](https://img.shields.io/badge/star-57835-f4b400?style=flat-square)](https://github.com/microsoft/autogen) | multi-agent, orchestration, framework | 支持多代理交互与编排的 agentic AI 编程框架。 |
| Agno | [GitHub](https://github.com/agno-agi/agno) | [![star](https://img.shields.io/badge/star-39996-f4b400?style=flat-square)](https://github.com/agno-agi/agno) | scale, runtime, management | 面向规模化运行与管理的 agent 软件运行时。 |
| LangGraph | [GitHub](https://github.com/langchain-ai/langgraph) | [![star](https://img.shields.io/badge/star-31531-f4b400?style=flat-square)](https://github.com/langchain-ai/langgraph) | graph, workflow, runtime | 图结构运行时，用于构建具备状态管理与确定性流程控制的可靠代理。 |
| Semantic Kernel | [GitHub](https://github.com/microsoft/semantic-kernel) | [![star](https://img.shields.io/badge/star-27858-f4b400?style=flat-square)](https://github.com/microsoft/semantic-kernel) | enterprise, orchestration, plugins | 面向企业应用的 agentic 框架，支持编排与插件化扩展。 |
| OpenAI Agents SDK (Python) | [GitHub](https://github.com/openai/openai-agents-python) | [![star](https://img.shields.io/badge/star-26069-f4b400?style=flat-square)](https://github.com/openai/openai-agents-python) | sdk, handoff, workflows | 轻量级多代理工作流框架，支持交接、编排和生产化模式。 |
| deepagents | [GitHub](https://github.com/langchain-ai/deepagents) | [![star](https://img.shields.io/badge/star-22473-f4b400?style=flat-square)](https://github.com/langchain-ai/deepagents) | runtime, orchestration, long-running | 面向长时任务的开源 harness，支持规划、工具调用与子代理协作模式。 |
| Archon | [GitHub](https://github.com/coleam00/Archon) | [![star](https://img.shields.io/badge/star-21055-f4b400?style=flat-square)](https://github.com/coleam00/Archon) | workflow-engine, worktrees, validation | 面向 AI 编码代理的工作流引擎，提供 YAML 定义阶段、隔离 worktree 与校验门禁。 |
| Google ADK (Python) | [GitHub](https://github.com/google/adk-python) | [![star](https://img.shields.io/badge/star-19531-f4b400?style=flat-square)](https://github.com/google/adk-python) | toolkit, deployment, evaluation | 代码优先的工具包，用于构建、评估和部署复杂 AI 代理。 |
| PydanticAI | [GitHub](https://github.com/pydantic/pydantic-ai) | [![star](https://img.shields.io/badge/star-16937-f4b400?style=flat-square)](https://github.com/pydantic/pydantic-ai) | python, typing, schema | 强调类型与结构化约束的 Python agent 框架，适合稳定化 harness 开发。 |
| Hive | [GitHub](https://github.com/aden-hive/hive) | [![star](https://img.shields.io/badge/star-10263-f4b400?style=flat-square)](https://github.com/aden-hive/hive) | harness, orchestration, runtime | 以结果驱动的 agent runtime harness，强调控制回路与编排模块。 |
| Microsoft Agent Framework | [GitHub](https://github.com/microsoft/agent-framework) | [![star](https://img.shields.io/badge/star-10243-f4b400?style=flat-square)](https://github.com/microsoft/agent-framework) | multi-agent, workflows, observability | 多语言代理框架，支持图工作流、编排、部署与可观测能力。 |
| VoltAgent | [GitHub](https://github.com/VoltAgent/voltagent) | [![star](https://img.shields.io/badge/star-8701-f4b400?style=flat-square)](https://github.com/VoltAgent/voltagent) | typescript, platform, runtime | 基于 TypeScript 的 agent 工程平台，提供开放运行时抽象。 |
| mcp-agent | [GitHub](https://github.com/lastmile-ai/mcp-agent) | [![star](https://img.shields.io/badge/star-8313-f4b400?style=flat-square)](https://github.com/lastmile-ai/mcp-agent) | mcp, runtime, workflow | 以 MCP 工具体系为核心的实用 agent 框架，强调工作流组合。 |
| Yao | [GitHub](https://github.com/YaoApp/yao) | [![star](https://img.shields.io/badge/star-7536-f4b400?style=flat-square)](https://github.com/YaoApp/yao) | single-binary, runtime, autonomous | 单二进制运行时，用于定义并运行自治代理。 |
| Cloudflare Agents | [GitHub](https://github.com/cloudflare/agents) | [![star](https://img.shields.io/badge/star-4887-f4b400?style=flat-square)](https://github.com/cloudflare/agents) | platform, deployment, runtime | 提供面向生产基础设施的 agent 构建与部署运行时。 |
| Docker Agent | [GitHub](https://github.com/docker/docker-agent) | [![star](https://img.shields.io/badge/star-2895-f4b400?style=flat-square)](https://github.com/docker/docker-agent) | docker, runtime, container | 强调容器原生执行的 agent 构建与运行时栈。 |
| NeMo Agent Toolkit | [GitHub](https://github.com/NVIDIA/NeMo-Agent-Toolkit) | [![star](https://img.shields.io/badge/star-2274-f4b400?style=flat-square)](https://github.com/NVIDIA/NeMo-Agent-Toolkit) | multi-agent, optimization, toolkit | 用于连接与优化多代理协作的开源工具包。 |
| Scion | [GitHub](https://github.com/GoogleCloudPlatform/scion) | [![star](https://img.shields.io/badge/star-1483-f4b400?style=flat-square)](https://github.com/GoogleCloudPlatform/scion) | multi-agent, containers, orchestration | 实验性多代理编排测试平台，可在容器、git worktree 与远程运行时中隔离运行各类 agent harness。 |
| deepagentsjs | [GitHub](https://github.com/langchain-ai/deepagentsjs) | [![star](https://img.shields.io/badge/star-1205-f4b400?style=flat-square)](https://github.com/langchain-ai/deepagentsjs) | typescript, langgraph, subagents | 基于 TypeScript 的 agent harness，内置规划、文件系统工具、子代理与 LangGraph 原生运行时能力。 |
| hankweave | [GitHub](https://github.com/SouthBridgeAI/hankweave-runtime) | [![star](https://img.shields.io/badge/star-121-f4b400?style=flat-square)](https://github.com/SouthBridgeAI/hankweave-runtime) | long-horizon, runtime, checkpoints | 面向长任务的无界面运行时，可编排现有 agent harness，并提供 sentinels、循环、检查点与事件日志。 |

<a id="context-working-state-engineering"></a>
### Context & Working-State Engineering

| 项目 | 链接 | Stars | 标签 | 简介 |
| --- | --- | --- | --- | --- |
| everything-claude-code | [GitHub](https://github.com/affaan-m/everything-claude-code) | [![star](https://img.shields.io/badge/star-175768-f4b400?style=flat-square)](https://github.com/affaan-m/everything-claude-code) | context, skills, harness-practices | 大型开源实践库，聚焦编码代理的记忆、技能与上下文控制策略。 |
| claude-mem | [GitHub](https://github.com/thedotmack/claude-mem) | [![star](https://img.shields.io/badge/star-73659-f4b400?style=flat-square)](https://github.com/thedotmack/claude-mem) | memory, context, session | 插件化记忆层，可记录会话历史并在后续编码任务中注入相关上下文。 |
| planning-with-files | [GitHub](https://github.com/OthmanAdi/planning-with-files) | [![star](https://img.shields.io/badge/star-20675-f4b400?style=flat-square)](https://github.com/OthmanAdi/planning-with-files) | planning, skills, persistence | 用于编码代理工作流的持久化文件规划技能包。 |
| Agent Skills for Context Engineering | [GitHub](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering) | [![star](https://img.shields.io/badge/star-15517-f4b400?style=flat-square)](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering) | skills, context, production | 面向上下文工程与生产代理的大型技能库。 |
| Context-Engineering Handbook | [GitHub](https://github.com/davidkimai/Context-Engineering) | [![star](https://img.shields.io/badge/star-8880-f4b400?style=flat-square)](https://github.com/davidkimai/Context-Engineering) | context-engineering, handbook, practices | 面向代理系统的第一性原理上下文工程手册，强调实践落地。 |
| CCPM | [GitHub](https://github.com/automazeio/ccpm) | [![star](https://img.shields.io/badge/star-8078-f4b400?style=flat-square)](https://github.com/automazeio/ccpm) | planning, github-issues, parallel-execution | 规格驱动的项目管理技能，将 PRD 与 GitHub issue 转化为持久上下文和并行代理执行流程。 |
| Trellis | [GitHub](https://github.com/mindfold-ai/Trellis) | [![star](https://img.shields.io/badge/star-7503-f4b400?style=flat-square)](https://github.com/mindfold-ai/Trellis) | specs, memory, workflow | 面向多平台编码代理的工作流框架，提供任务上下文、项目记忆与规范注入。 |
| Awesome Context Engineering | [GitHub](https://github.com/Meirtz/Awesome-Context-Engineering) | [![star](https://img.shields.io/badge/star-3112-f4b400?style=flat-square)](https://github.com/Meirtz/Awesome-Context-Engineering) | awesome-list, context, survey | 面向上下文工程的综述型清单，覆盖资源与框架。 |
| context-space | [GitHub](https://github.com/context-space/context-space) | [![star](https://img.shields.io/badge/star-809-f4b400?style=flat-square)](https://github.com/context-space/context-space) | context, infrastructure, mcp | 聚焦上下文工程基础设施的项目，强调 MCP 生态集成能力。 |

<a id="execution-substrates-sandboxing"></a>
### Execution Substrates & Sandboxing

| 项目 | 链接 | Stars | 标签 | 简介 |
| --- | --- | --- | --- | --- |
| Daytona | [GitHub](https://github.com/daytonaio/daytona) | [![star](https://img.shields.io/badge/star-72379-f4b400?style=flat-square)](https://github.com/daytonaio/daytona) | sandbox, execution, infra | 面向 AI 生成代码的安全弹性沙箱基础设施，提供文件、Git、LSP 与执行 API。 |
| CUA | [GitHub](https://github.com/trycua/cua) | [![star](https://img.shields.io/badge/star-15750-f4b400?style=flat-square)](https://github.com/trycua/cua) | computer-use, sandbox, infra | 面向计算机操作代理的基础设施栈，包含沙箱、SDK 与基准支持。 |
| E2B | [GitHub](https://github.com/e2b-dev/E2B) | [![star](https://img.shields.io/badge/star-12114-f4b400?style=flat-square)](https://github.com/e2b-dev/E2B) | cloud-sandbox, execution, enterprise | 提供真实工具的安全云端环境，面向生产级代理执行。 |
| Browser Harness | [GitHub](https://github.com/browser-use/browser-harness) | [![star](https://img.shields.io/badge/star-11610-f4b400?style=flat-square)](https://github.com/browser-use/browser-harness) | browser, cdp, self-healing | 轻量可编辑的 CDP harness，可将 LLM 直接接入真实浏览器，并允许代理在运行中扩展辅助能力。 |
| OpenSandbox | [GitHub](https://github.com/alibaba/OpenSandbox) | [![star](https://img.shields.io/badge/star-10492-f4b400?style=flat-square)](https://github.com/alibaba/OpenSandbox) | sandbox, security, runtime | 面向代理工作负载的安全可扩展沙箱运行时。 |
| agent-infra sandbox | [GitHub](https://github.com/agent-infra/sandbox) | [![star](https://img.shields.io/badge/star-4571-f4b400?style=flat-square)](https://github.com/agent-infra/sandbox) | all-in-one, browser, shell | 集成浏览器、Shell、文件、MCP 与 IDE 服务的一体化沙箱。 |
| Judge0 | [GitHub](https://github.com/judge0/judge0) | [![star](https://img.shields.io/badge/star-4159-f4b400?style=flat-square)](https://github.com/judge0/judge0) | code-execution, sandbox, backend | 可扩展的沙箱代码执行系统，可作为代理执行后端。 |
| Agent Sandbox | [GitHub](https://github.com/kubernetes-sigs/agent-sandbox) | [![star](https://img.shields.io/badge/star-2081-f4b400?style=flat-square)](https://github.com/kubernetes-sigs/agent-sandbox) | kubernetes, sandbox, stateful | 面向隔离且有状态 agent runtime 的 Kubernetes 原生沙箱控制平面，提供稳定身份、持久化与预热池能力。 |
| stakpak/agent | [GitHub](https://github.com/stakpak/agent) | [![star](https://img.shields.io/badge/star-1497-f4b400?style=flat-square)](https://github.com/stakpak/agent) | always-on, autonomous, ops | 常驻机器运行的开源自治代理，强调持续运维闭环。 |
| OSS-Fuzz Gen | [GitHub](https://github.com/google/oss-fuzz-gen) | [![star](https://img.shields.io/badge/star-1390-f4b400?style=flat-square)](https://github.com/google/oss-fuzz-gen) | fuzzing, security, execution | 将 LLM 驱动模糊测试与受控执行环境结合的工程实现。 |
| E2B Desktop Sandbox | [GitHub](https://github.com/e2b-dev/desktop) | [![star](https://img.shields.io/badge/star-1361-f4b400?style=flat-square)](https://github.com/e2b-dev/desktop) | desktop, sandbox, computer-use | 面向 computer-use 代理的安全虚拟桌面沙箱，提供 SDK 控制与屏幕流式能力。 |
| Tensorlake | [GitHub](https://github.com/tensorlakeai/tensorlake) | [![star](https://img.shields.io/badge/star-914-f4b400?style=flat-square)](https://github.com/tensorlakeai/tensorlake) | microvm, sandbox, orchestration | 面向 agent 沙箱的无服务器运行时，提供 MicroVM 隔离、快照、挂起恢复与后台编排能力。 |
| Arrakis | [GitHub](https://github.com/abshkbh/arrakis) | [![star](https://img.shields.io/badge/star-809-f4b400?style=flat-square)](https://github.com/abshkbh/arrakis) | sandbox, microvm, snapshots | 自托管沙箱基座，提供 MicroVM 隔离、快照恢复，以及面向代理代码执行与 computer use 的 REST、SDK 与 MCP 接口。 |
| AgentScope Runtime | [GitHub](https://github.com/agentscope-ai/agentscope-runtime) | [![star](https://img.shields.io/badge/star-769-f4b400?style=flat-square)](https://github.com/agentscope-ai/agentscope-runtime) | runtime, sandbox, deployment | 面向代理应用的生产运行时，提供安全工具沙箱、部署 API、可观测能力与状态服务。 |
| SWE-ReX | [GitHub](https://github.com/SWE-agent/SWE-ReX) | [![star](https://img.shields.io/badge/star-493-f4b400?style=flat-square)](https://github.com/SWE-agent/SWE-ReX) | sandbox, execution, coding-agent | 面向 AI 编码代理的沙箱执行基础设施，支持本地与云端扩展。 |
| sandboxed.sh | [GitHub](https://github.com/Th0rgal/sandboxed.sh) | [![star](https://img.shields.io/badge/star-417-f4b400?style=flat-square)](https://github.com/Th0rgal/sandboxed.sh) | self-hosted, isolation, orchestrator | 在隔离 Linux 工作区中运行编码代理的自托管编排器。 |
| Capsule | [GitHub](https://github.com/capsulerun/capsule) | [![star](https://img.shields.io/badge/star-281-f4b400?style=flat-square)](https://github.com/capsulerun/capsule) | wasm, sandbox, task-runtime | 在隔离 WebAssembly 沙箱中协调 agent 任务的耐久运行时，提供重试与生命周期跟踪。 |
| terminal-bench-env | [GitHub](https://github.com/ucsb-mlsec/terminal-bench-env) | [![star](https://img.shields.io/badge/star-81-f4b400?style=flat-square)](https://github.com/ucsb-mlsec/terminal-bench-env) | terminal, benchmark-env, sandbox | 为终端代理基准测试提供执行环境层。 |

<a id="protocols-tool-interfaces-agent-contracts"></a>
### Protocols, Tool Interfaces & Agent Contracts

| 项目 | 链接 | Stars | 标签 | 简介 |
| --- | --- | --- | --- | --- |
| GitHub Spec Kit | [GitHub](https://github.com/github/spec-kit) | [![star](https://img.shields.io/badge/star-93332-f4b400?style=flat-square)](https://github.com/github/spec-kit) | spec-driven, workflows, tooling | 面向规范驱动开发的工具包，可引导代理进行确定性执行。 |
| MCP Servers | [GitHub](https://github.com/modelcontextprotocol/servers) | [![star](https://img.shields.io/badge/star-85276-f4b400?style=flat-square)](https://github.com/modelcontextprotocol/servers) | mcp, servers, implementations | 官方 MCP Server 实现集合，覆盖多种工具与场景。 |
| AGENTS.md | [GitHub](https://github.com/agentsmd/agents.md) | [![star](https://img.shields.io/badge/star-21109-f4b400?style=flat-square)](https://github.com/agentsmd/agents.md) | spec, agent-file, instructions | 面向代码仓库本地代理指令的开放格式规范。 |
| Model Context Protocol | [GitHub](https://github.com/modelcontextprotocol/modelcontextprotocol) | [![star](https://img.shields.io/badge/star-8048-f4b400?style=flat-square)](https://github.com/modelcontextprotocol/modelcontextprotocol) | mcp, protocol, interoperability | MCP 的核心规范与文档，定义工具与上下文互操作方式。 |
| directories (rules and MCP indexes) | [GitHub](https://github.com/leerob/directories) | [![star](https://img.shields.io/badge/star-3929-f4b400?style=flat-square)](https://github.com/leerob/directories) | directories, mcp, rules | 面向规则与 MCP server 发现的目录索引集合。 |
| LangChain MCP Adapters | [GitHub](https://github.com/langchain-ai/langchain-mcp-adapters) | [![star](https://img.shields.io/badge/star-3516-f4b400?style=flat-square)](https://github.com/langchain-ai/langchain-mcp-adapters) | mcp, adapters, integration | 用于连接 LangChain 组件与 MCP server 的适配层。 |
| Microsoft MCP Servers | [GitHub](https://github.com/microsoft/mcp) | [![star](https://img.shields.io/badge/star-3112-f4b400?style=flat-square)](https://github.com/microsoft/mcp) | mcp, enterprise, servers | 微软官方 MCP server 目录，连接企业数据与工具。 |
| ACPX | [GitHub](https://github.com/openclaw/acpx) | [![star](https://img.shields.io/badge/star-2605-f4b400?style=flat-square)](https://github.com/openclaw/acpx) | acp, client, sessions | 面向有状态 Agent Client Protocol 会话的无头 CLI 客户端。 |
| Microsoft Learn MCP | [GitHub](https://github.com/MicrosoftDocs/mcp) | [![star](https://img.shields.io/badge/star-1614-f4b400?style=flat-square)](https://github.com/MicrosoftDocs/mcp) | mcp, docs, grounding | 为代理接入微软文档知识提供的 MCP server 与 CLI。 |
| IBM MCP | [GitHub](https://github.com/IBM/mcp) | [![star](https://img.shields.io/badge/star-374-f4b400?style=flat-square)](https://github.com/IBM/mcp) | mcp, clients, tooling | IBM 提供的 MCP server、client 与开发工具集合。 |
| AGENT.md | [GitHub](https://github.com/agentmd/agent.md) | [![star](https://img.shields.io/badge/star-78-f4b400?style=flat-square)](https://github.com/agentmd/agent.md) | standard, agent-file, interoperability | 面向代理编码工具的标准化机器可读文件格式。 |

<a id="evaluation-harnesses-benchmarks"></a>
### Evaluation Harnesses & Benchmarks

| 项目 | 链接 | Stars | 标签 | 简介 |
| --- | --- | --- | --- | --- |
| Promptfoo | [GitHub](https://github.com/promptfoo/promptfoo) | [![star](https://img.shields.io/badge/star-21000-f4b400?style=flat-square)](https://github.com/promptfoo/promptfoo) | eval, red-team, ci | 配置驱动的 Prompt/Agent/RAG 测试、对比与红队评估工具。 |
| DeepEval | [GitHub](https://github.com/confident-ai/deepeval) | [![star](https://img.shields.io/badge/star-15247-f4b400?style=flat-square)](https://github.com/confident-ai/deepeval) | evaluation, framework, testing | 支持代理与工作流质量测试的 LLM 评估框架。 |
| RAGAS | [GitHub](https://github.com/vibrantlabsai/ragas) | [![star](https://img.shields.io/badge/star-13836-f4b400?style=flat-square)](https://github.com/vibrantlabsai/ragas) | rag, metrics, evaluation | 面向 LLM 与 RAG 质量指标的开源评测工具集。 |
| lm-evaluation-harness | [GitHub](https://github.com/EleutherAI/lm-evaluation-harness) | [![star](https://img.shields.io/badge/star-12477-f4b400?style=flat-square)](https://github.com/EleutherAI/lm-evaluation-harness) | benchmark, harness, llm | 广泛使用的 LLM 基准 harness，用于跨任务一致评估。 |
| SWE-bench | [GitHub](https://github.com/SWE-bench/SWE-bench) | [![star](https://img.shields.io/badge/star-4875-f4b400?style=flat-square)](https://github.com/SWE-bench/SWE-bench) | benchmark, swe, evaluation | 软件工程代理 issue 修复能力的标准评测基准。 |
| verifiers | [GitHub](https://github.com/PrimeIntellect-ai/verifiers) | [![star](https://img.shields.io/badge/star-4087-f4b400?style=flat-square)](https://github.com/PrimeIntellect-ai/verifiers) | verifier, rl, evaluation | 面向 RL 环境与 verifier 评测回路的库。 |
| AgentBench | [GitHub](https://github.com/THUDM/AgentBench) | [![star](https://img.shields.io/badge/star-3401-f4b400?style=flat-square)](https://github.com/THUDM/AgentBench) | benchmark, cross-domain, agent | 跨环境评测基准，用于衡量 LLM 代理的工具使用能力。 |
| LangWatch | [GitHub](https://github.com/langwatch/langwatch) | [![star](https://img.shields.io/badge/star-3245-f4b400?style=flat-square)](https://github.com/langwatch/langwatch) | simulation, evaluation, testing | 面向代理模拟、评测闭环与生产测试的端到端平台。 |
| EvalScope | [GitHub](https://github.com/modelscope/evalscope) | [![star](https://img.shields.io/badge/star-2768-f4b400?style=flat-square)](https://github.com/modelscope/evalscope) | benchmark, framework, llm | 可定制的大模型基准与性能评测框架。 |
| Terminal-Bench | [GitHub](https://github.com/harbor-framework/terminal-bench) | [![star](https://img.shields.io/badge/star-2170-f4b400?style=flat-square)](https://github.com/harbor-framework/terminal-bench) | terminal, benchmark, long-horizon | 面向长时与重验证任务的终端原生代理基准套件。 |
| Harbor | [GitHub](https://github.com/harbor-framework/harbor) | [![star](https://img.shields.io/badge/star-1839-f4b400?style=flat-square)](https://github.com/harbor-framework/harbor) | evaluation, harness, rl-env | 用于运行代理评测并构建类 RL 环境的框架。 |
| tau2-bench | [GitHub](https://github.com/sierra-research/tau2-bench) | [![star](https://img.shields.io/badge/star-1137-f4b400?style=flat-square)](https://github.com/sierra-research/tau2-bench) | tool-use, interaction, benchmark | 强调多步执行质量的工具-代理-用户交互基准。 |
| NeMo Gym | [GitHub](https://github.com/NVIDIA-NeMo/Gym) | [![star](https://img.shields.io/badge/star-877-f4b400?style=flat-square)](https://github.com/NVIDIA-NeMo/Gym) | rl-env, training, evaluation | 用于构建 LLM/代理训练与评测 RL 环境的工具集。 |
| TheAgentCompany | [GitHub](https://github.com/TheAgentCompany/TheAgentCompany) | [![star](https://img.shields.io/badge/star-697-f4b400?style=flat-square)](https://github.com/TheAgentCompany/TheAgentCompany) | benchmark, workplace, multi-step | 以模拟软件公司任务评测多步工作场景自治能力的 agent 基准。 |
| auto-harness | [GitHub](https://github.com/neosigmaai/auto-harness) | [![star](https://img.shields.io/badge/star-491-f4b400?style=flat-square)](https://github.com/neosigmaai/auto-harness) | optimization, regression, evals | 以基准门控的优化闭环，可自动挖掘失败样例、修改 agent 代码，并在夜间持续防回归。 |
| Inspect Evals | [GitHub](https://github.com/UKGovernmentBEIS/inspect_evals) | [![star](https://img.shields.io/badge/star-484-f4b400?style=flat-square)](https://github.com/UKGovernmentBEIS/inspect_evals) | inspect, eval-suite, reproducibility | 面向 Inspect AI 工作流的评测套件集合。 |
| SWE-Bench Pro | [GitHub](https://github.com/scaleapi/SWE-bench_Pro-os) | [![star](https://img.shields.io/badge/star-378-f4b400?style=flat-square)](https://github.com/scaleapi/SWE-bench_Pro-os) | swe, benchmark, long-horizon | 面向 issue 驱动编码代理的长时软件工程基准，提供可复现的 Docker 化评测流程。 |
| Agent Evaluation | [GitHub](https://github.com/awslabs/agent-evaluation) | [![star](https://img.shields.io/badge/star-360-f4b400?style=flat-square)](https://github.com/awslabs/agent-evaluation) | evaluation, testing, ci | AWS 的虚拟代理测试框架，支持评估器驱动的多轮对话、钩子扩展与 CI 友好工作流。 |
| WorkArena | [GitHub](https://github.com/ServiceNow/WorkArena) | [![star](https://img.shields.io/badge/star-247-f4b400?style=flat-square)](https://github.com/ServiceNow/WorkArena) | browser, benchmark, enterprise | 面向企业知识工作任务的浏览器代理基准。 |
| OpenHands Benchmarks | [GitHub](https://github.com/OpenHands/benchmarks) | [![star](https://img.shields.io/badge/star-78-f4b400?style=flat-square)](https://github.com/OpenHands/benchmarks) | openhands, eval, harness | OpenHands 体系的评测 harness 与基准定义。 |
| WebArena-Verified | [GitHub](https://github.com/ServiceNow/webarena-verified) | [![star](https://img.shields.io/badge/star-38-f4b400?style=flat-square)](https://github.com/ServiceNow/webarena-verified) | web-agent, benchmark, deterministic | 带确定性评测器的已验证 Web 代理基准。 |

<a id="observability-reliability-operations"></a>
### Observability & Reliability Operations

| 项目 | 链接 | Stars | 标签 | 简介 |
| --- | --- | --- | --- | --- |
| Langfuse | [GitHub](https://github.com/langfuse/langfuse) | [![star](https://img.shields.io/badge/star-26828-f4b400?style=flat-square)](https://github.com/langfuse/langfuse) | llmops, tracing, metrics | 开源 LLM 工程平台，覆盖链路追踪、指标、提示词与评测。 |
| MLflow | [GitHub](https://github.com/mlflow/mlflow) | [![star](https://img.shields.io/badge/star-25828-f4b400?style=flat-square)](https://github.com/mlflow/mlflow) | platform, monitoring, evaluation | 通用 AI 工程平台，支持代理系统的监控与评测。 |
| Opik | [GitHub](https://github.com/comet-ml/opik) | [![star](https://img.shields.io/badge/star-19249-f4b400?style=flat-square)](https://github.com/comet-ml/opik) | monitoring, eval, tracing | 面向 LLM 应用与代理流程的端到端调试、评测与监控平台。 |
| RagaAI Catalyst | [GitHub](https://github.com/raga-ai-hub/RagaAI-Catalyst) | [![star](https://img.shields.io/badge/star-16158-f4b400?style=flat-square)](https://github.com/raga-ai-hub/RagaAI-Catalyst) | agentops, analytics, monitoring | 带时间线与执行图分析的代理可观测性监控框架。 |
| TensorZero | [GitHub](https://github.com/tensorzero/tensorzero) | [![star](https://img.shields.io/badge/star-11340-f4b400?style=flat-square)](https://github.com/tensorzero/tensorzero) | llmops, gateway, optimization | 开源 LLMOps 栈，统一网关、可观测性、评测与优化。 |
| Arize Phoenix | [GitHub](https://github.com/Arize-ai/phoenix) | [![star](https://img.shields.io/badge/star-9574-f4b400?style=flat-square)](https://github.com/Arize-ai/phoenix) | observability, tracing, evaluation | 开放的 AI 可观测性平台，支持追踪与评测分析。 |
| OpenLLMetry | [GitHub](https://github.com/traceloop/openllmetry) | [![star](https://img.shields.io/badge/star-7078-f4b400?style=flat-square)](https://github.com/traceloop/openllmetry) | opentelemetry, instrumentation, tracing | 基于 OpenTelemetry 的 GenAI/LLM 应用可观测性埋点方案。 |
| Helicone | [GitHub](https://github.com/Helicone/helicone) | [![star](https://img.shields.io/badge/star-5625-f4b400?style=flat-square)](https://github.com/Helicone/helicone) | monitoring, traffic, production | 轻量平台，用于生产环境 LLM 流量监控与评估。 |
| AgentOps SDK | [GitHub](https://github.com/AgentOps-AI/agentops) | [![star](https://img.shields.io/badge/star-5529-f4b400?style=flat-square)](https://github.com/AgentOps-AI/agentops) | agentops, monitoring, cost | 面向代理工作流的监控与基准 SDK，支持成本与链路追踪。 |
| Latitude | [GitHub](https://github.com/latitude-dev/latitude-llm) | [![star](https://img.shields.io/badge/star-3980-f4b400?style=flat-square)](https://github.com/latitude-dev/latitude-llm) | platform, eval, observability | 开源 agent 工程平台，集成评测与可观测性能力。 |
| Laminar | [GitHub](https://github.com/lmnr-ai/lmnr) | [![star](https://img.shields.io/badge/star-2852-f4b400?style=flat-square)](https://github.com/lmnr-ai/lmnr) | observability, tracing, evals | 面向代理系统的可观测平台，覆盖追踪、评测运行、监控与仪表盘。 |
| claude-code-reverse | [GitHub](https://github.com/Yuyz0112/claude-code-reverse) | [![star](https://img.shields.io/badge/star-2361-f4b400?style=flat-square)](https://github.com/Yuyz0112/claude-code-reverse) | trace, visualization, debugging | 可视化并分析 Claude Code 大模型交互链路的工具。 |
| OpenInference | [GitHub](https://github.com/Arize-ai/openinference) | [![star](https://img.shields.io/badge/star-956-f4b400?style=flat-square)](https://github.com/Arize-ai/openinference) | spec, instrumentation, observability | 面向 AI 可观测性的开放埋点规范与工具。 |
| Future AGI | [GitHub](https://github.com/future-agi/future-agi) | [![star](https://img.shields.io/badge/star-892-f4b400?style=flat-square)](https://github.com/future-agi/future-agi) | observability, evaluation, guardrails | 可自托管的平台，将代理追踪、评测、模拟、护栏与网关运维闭环整合在一起。 |

<a id="guardrails-security-governance"></a>
### Guardrails, Security & Governance

| 项目 | 链接 | Stars | 标签 | 简介 |
| --- | --- | --- | --- | --- |
| LiteLLM | [GitHub](https://github.com/BerriAI/litellm) | [![star](https://img.shields.io/badge/star-46177-f4b400?style=flat-square)](https://github.com/BerriAI/litellm) | gateway, proxy, guardrails | 统一 LLM 网关/代理，支持成本追踪、负载均衡与护栏。 |
| Kong | [GitHub](https://github.com/Kong/kong) | [![star](https://img.shields.io/badge/star-43338-f4b400?style=flat-square)](https://github.com/Kong/kong) | gateway, policy, infra | API 与 AI 网关基础设施，可用于代理系统的策略执行。 |
| Portkey Gateway | [GitHub](https://github.com/Portkey-AI/gateway) | [![star](https://img.shields.io/badge/star-11642-f4b400?style=flat-square)](https://github.com/Portkey-AI/gateway) | gateway, guardrails, routing | 支持多模型路由与护栏控制的 AI 网关。 |
| CAI (Cybersecurity AI) | [GitHub](https://github.com/aliasrobotics/cai) | [![star](https://img.shields.io/badge/star-8438-f4b400?style=flat-square)](https://github.com/aliasrobotics/cai) | security, governance, framework | 面向攻防场景的安全型代理框架。 |
| OpenAI Realtime Agents | [GitHub](https://github.com/openai/openai-realtime-agents) | [![star](https://img.shields.io/badge/star-6852-f4b400?style=flat-square)](https://github.com/openai/openai-realtime-agents) | realtime, orchestration, control | 展示高级实时代理模式，强调结构化控制与交互回路。 |
| Plano | [GitHub](https://github.com/katanemo/plano) | [![star](https://img.shields.io/badge/star-6439-f4b400?style=flat-square)](https://github.com/katanemo/plano) | proxy, safety, data-plane | 内置编排、安全与可观测性的 AI 原生代理与数据平面。 |
| OpenAI CS Agents Demo | [GitHub](https://github.com/openai/openai-cs-agents-demo) | [![star](https://img.shields.io/badge/star-6326-f4b400?style=flat-square)](https://github.com/openai/openai-cs-agents-demo) | demo, handoffs, governance | 客服多代理示例，展示交接流程与类似护栏的控制节点。 |
| ContextForge | [GitHub](https://github.com/IBM/mcp-context-forge) | [![star](https://img.shields.io/badge/star-3673-f4b400?style=flat-square)](https://github.com/IBM/mcp-context-forge) | gateway, governance, observability | 统一 MCP、A2A 与 REST/gRPC 端点的注册与代理层，提供集中治理与可观测能力。 |
| Archestra | [GitHub](https://github.com/archestra-ai/archestra) | [![star](https://img.shields.io/badge/star-3638-f4b400?style=flat-square)](https://github.com/archestra-ai/archestra) | enterprise, guardrails, governance | 企业级 AI 平台，提供护栏、MCP 注册中心与编排能力。 |
| Tracecat | [GitHub](https://github.com/TracecatHQ/tracecat) | [![star](https://img.shields.io/badge/star-3582-f4b400?style=flat-square)](https://github.com/TracecatHQ/tracecat) | security, automation, policy | 面向安全团队的 AI 自动化平台，提供策略与工作流控制。 |
| AgentGateway | [GitHub](https://github.com/agentgateway/agentgateway) | [![star](https://img.shields.io/badge/star-2647-f4b400?style=flat-square)](https://github.com/agentgateway/agentgateway) | gateway, mcp, proxy | 面向 AI 代理与 MCP 生态的代理网关。 |
| Haft | [GitHub](https://github.com/m0n0x41d/haft) | [![star](https://img.shields.io/badge/star-1316-f4b400?style=flat-square)](https://github.com/m0n0x41d/haft) | governance, decisions, mcp | 面向决策治理的 harness，在代理执行前沉淀可证伪契约、证据与 commission 生命周期。 |

<a id="reference-harness-implementations"></a>
### Reference Harness Implementations

| 项目 | 链接 | Stars | 标签 | 简介 |
| --- | --- | --- | --- | --- |
| OpenCode | [GitHub](https://github.com/anomalyco/opencode) | [![star](https://img.shields.io/badge/star-156925-f4b400?style=flat-square)](https://github.com/anomalyco/opencode) | terminal, coding-agent, subagents | 开源编码代理，提供内置 plan/build 角色、子代理、LSP 支持与客户端-服务端运行时。 |
| Claude Code | [GitHub](https://github.com/anthropics/claude-code) | [![star](https://img.shields.io/badge/star-121609-f4b400?style=flat-square)](https://github.com/anthropics/claude-code) | terminal, coding-agent, git-workflows | 官方终端编码代理，可理解代码库并通过自然语言执行编辑、调试与 Git 工作流。 |
| Gemini CLI | [GitHub](https://github.com/google-gemini/gemini-cli) | [![star](https://img.shields.io/badge/star-103438-f4b400?style=flat-square)](https://github.com/google-gemini/gemini-cli) | terminal, coding-agent, mcp | 开源终端代理，提供内置工具、MCP 支持、会话检查点与沙箱控制能力。 |
| Codex CLI | [GitHub](https://github.com/openai/codex) | [![star](https://img.shields.io/badge/star-80949-f4b400?style=flat-square)](https://github.com/openai/codex) | terminal, coding-agent, local-execution | 终端原生的本地编码代理，提供面向软件任务的实用 agent 工作流。 |
| OpenHands | [GitHub](https://github.com/OpenHands/OpenHands) | [![star](https://img.shields.io/badge/star-72918-f4b400?style=flat-square)](https://github.com/OpenHands/OpenHands) | coding-agent, software-engineering, repo | 开源 AI 软件工程代理，聚焦仓库级编码任务执行。 |
| learn-claude-code | [GitHub](https://github.com/shareAI-lab/learn-claude-code) | [![star](https://img.shields.io/badge/star-59100-f4b400?style=flat-square)](https://github.com/shareAI-lab/learn-claude-code) | tutorial, harness, claude-code | 从 0 到 1 构建 Claude Code 类系统的实战 harness 教程。 |
| OpenManus | [GitHub](https://github.com/FoundationAgents/OpenManus) | [![star](https://img.shields.io/badge/star-56125-f4b400?style=flat-square)](https://github.com/FoundationAgents/OpenManus) | general-agent, autonomy, workflows | 面向广义自治任务的开放基础系统，覆盖编码等复杂场景。 |
| pi | [GitHub](https://github.com/earendil-works/pi) | [![star](https://img.shields.io/badge/star-46494-f4b400?style=flat-square)](https://github.com/earendil-works/pi) | coding-agent, runtime, monorepo | 将编码代理 CLI、共享运行时与多模型 LLM 栈整合在一起的 agent harness monorepo。 |
| aider | [GitHub](https://github.com/Aider-AI/aider) | [![star](https://img.shields.io/badge/star-44530-f4b400?style=flat-square)](https://github.com/Aider-AI/aider) | terminal, repo-map, testing | 终端编码助手，提供仓库映射、Git 感知编辑与内置 lint/test 反馈回路。 |
| Claude Code Plugins: Orchestration and Automation | [GitHub](https://github.com/wshobson/agents) | [![star](https://img.shields.io/badge/star-34998-f4b400?style=flat-square)](https://github.com/wshobson/agents) | claude-code, plugins, orchestration | 面向 Claude Code 的生产级插件仓库，整合 agents、skills、tools 与多代理工作流编排器。 |
| CLI-Anything | [GitHub](https://github.com/HKUDS/CLI-Anything) | [![star](https://img.shields.io/badge/star-33965-f4b400?style=flat-square)](https://github.com/HKUDS/CLI-Anything) | cli, tool-use, automation | 在代理回路中统一命令行工具使用的 CLI agent 系统。 |
| NanoClaw | [GitHub](https://github.com/qwibitai/nanoclaw) | [![star](https://img.shields.io/badge/star-28700-f4b400?style=flat-square)](https://github.com/qwibitai/nanoclaw) | containers, claude-sdk, scheduling | 基于容器隔离的 Claude 代理 harness，提供多通道路由、定时任务、按群组隔离的记忆，以及小代码库定制能力。 |
| Qwen Code | [GitHub](https://github.com/QwenLM/qwen-code) | [![star](https://img.shields.io/badge/star-24238-f4b400?style=flat-square)](https://github.com/QwenLM/qwen-code) | terminal, coding-agent, cli | 终端原生开源编码代理，面向实际开发循环优化。 |
| SuperClaude Framework | [GitHub](https://github.com/SuperClaude-Org/SuperClaude_Framework) | [![star](https://img.shields.io/badge/star-22656-f4b400?style=flat-square)](https://github.com/SuperClaude-Org/SuperClaude_Framework) | config, personas, workflow | 为编码代理增强命令、角色与方法模板的配置框架。 |
| Devika | [GitHub](https://github.com/stitionai/devika) | [![star](https://img.shields.io/badge/star-19509-f4b400?style=flat-square)](https://github.com/stitionai/devika) | assistant, planning, coding | 开源编码助手系统，支持任务规划与实现。 |
| SWE-agent | [GitHub](https://github.com/SWE-agent/SWE-agent) | [![star](https://img.shields.io/badge/star-19165-f4b400?style=flat-square)](https://github.com/SWE-agent/SWE-agent) | swe, issue-fixing, tooling | 研究级编码代理，通过明确的工具回路自动修复 GitHub issue。 |
| cmux | [GitHub](https://github.com/manaflow-ai/cmux) | [![star](https://img.shields.io/badge/star-16481-f4b400?style=flat-square)](https://github.com/manaflow-ai/cmux) | macos, workspace, browser | 面向 AI 编码代理的原生 macOS 终端与浏览器工作区，提供通知、分屏与可脚本化控制。 |
| Aperant | [GitHub](https://github.com/AndyMik90/Aperant) | [![star](https://img.shields.io/badge/star-14170-f4b400?style=flat-square)](https://github.com/AndyMik90/Aperant) | coding-agent, parallel, memory | 自治多代理编码框架，提供并行执行、隔离工作区、质量校验回路与持久记忆。 |
| Eigent | [GitHub](https://github.com/eigent-ai/eigent) | [![star](https://img.shields.io/badge/star-13929-f4b400?style=flat-square)](https://github.com/eigent-ai/eigent) | desktop, cowork, productivity | 开源桌面协作代理，可执行自治任务并提升开发生产力。 |
| OpenHarness | [GitHub](https://github.com/HKUDS/OpenHarness) | [![star](https://img.shields.io/badge/star-12181-f4b400?style=flat-square)](https://github.com/HKUDS/OpenHarness) | tool-use, memory, multi-agent | 开放式 agent harness 实现，覆盖工具调用、技能、记忆、权限与多代理协作。 |
| IronClaw | [GitHub](https://github.com/nearai/ironclaw) | [![star](https://img.shields.io/badge/star-12172-f4b400?style=flat-square)](https://github.com/nearai/ironclaw) | security, wasm, routines | 安全优先的个人 agent harness，集成 WASM 沙箱、例程调度、工具插件与持久记忆。 |
| Superset | [GitHub](https://github.com/superset-sh/superset) | [![star](https://img.shields.io/badge/star-10495-f4b400?style=flat-square)](https://github.com/superset-sh/superset) | worktrees, desktop, parallel | 基于 worktree 的桌面编排器，可在统一工作区中并行运行并审阅多个 CLI 编码代理。 |
| GitHub Copilot CLI | [GitHub](https://github.com/github/copilot-cli) | [![star](https://img.shields.io/badge/star-10390-f4b400?style=flat-square)](https://github.com/github/copilot-cli) | terminal, coding-agent, mcp | 官方终端编码代理，基于 GitHub Copilot harness，提供 MCP 扩展、审批控制与 GitHub 原生上下文。 |
| Open SWE | [GitHub](https://github.com/langchain-ai/open-swe) | [![star](https://img.shields.io/badge/star-9748-f4b400?style=flat-square)](https://github.com/langchain-ai/open-swe) | async, coding-agent, swe | 面向软件问题流的异步开源编码代理。 |
| Paseo | [GitHub](https://github.com/getpaseo/paseo) | [![star](https://img.shields.io/badge/star-5724-f4b400?style=flat-square)](https://github.com/getpaseo/paseo) | coding-agent, daemon, multi-device | 面向多设备的编码代理守护进程与客户端栈，用于编排本地代理、并行运行与跨模型工作流。 |
| 1Code | [GitHub](https://github.com/21st-dev/1code) | [![star](https://img.shields.io/badge/star-5507-f4b400?style=flat-square)](https://github.com/21st-dev/1code) | coding-agent, orchestration, worktrees | 桌面优先的编码代理编排器，提供 worktree 隔离、后台沙箱、MCP 工具管理与自动化触发。 |
| holaOS | [GitHub](https://github.com/holaboss-ai/holaOS) | [![star](https://img.shields.io/badge/star-5316-f4b400?style=flat-square)](https://github.com/holaboss-ai/holaOS) | long-horizon, desktop, durable-state | 面向长时任务的桌面优先 agent environment，整合运行时、记忆、工具、应用与持久状态。 |
| OSAURUS | [GitHub](https://github.com/osaurus-ai/osaurus) | [![star](https://img.shields.io/badge/star-5203-f4b400?style=flat-square)](https://github.com/osaurus-ai/osaurus) | macos, local-first, memory | 面向 macOS 的本地自治编码代理 harness，支持持久记忆。 |
| HiClaw | [GitHub](https://github.com/agentscope-ai/HiClaw) | [![star](https://img.shields.io/badge/star-4476-f4b400?style=flat-square)](https://github.com/agentscope-ai/HiClaw) | multi-agent, human-in-the-loop, shared-state | 协作式多代理操作系统，通过 Matrix 房间提供管理者-工作者协同、共享状态与人在回路监督。 |
| mini-swe-agent | [GitHub](https://github.com/SWE-agent/mini-swe-agent) | [![star](https://img.shields.io/badge/star-4249-f4b400?style=flat-square)](https://github.com/SWE-agent/mini-swe-agent) | minimal, swe, coding-agent | 极简编码代理实现，同时具备较强基准表现。 |
| oh-my-pi | [GitHub](https://github.com/can1357/oh-my-pi) | [![star](https://img.shields.io/badge/star-4146-f4b400?style=flat-square)](https://github.com/can1357/oh-my-pi) | terminal, lsp, subagents | 终端 AI 编码代理，包含编辑安全、LSP 集成与子代理支持。 |
| TinyAGI | [GitHub](https://github.com/TinyAGI/tinyagi) | [![star](https://img.shields.io/badge/star-3553-f4b400?style=flat-square)](https://github.com/TinyAGI/tinyagi) | team-orchestration, autonomous, workflows | 面向“一人公司”场景的团队化代理编排器。 |
| Devon | [GitHub](https://github.com/entropy-research/Devon) | [![star](https://img.shields.io/badge/star-3447-f4b400?style=flat-square)](https://github.com/entropy-research/Devon) | pair-programming, coding-agent, autonomous | 开源结对编程代理，提供自治编码执行模式。 |
| Open Claude Cowork | [GitHub](https://github.com/DevAgentForge/Open-Claude-Cowork) | [![star](https://img.shields.io/badge/star-3263-f4b400?style=flat-square)](https://github.com/DevAgentForge/Open-Claude-Cowork) | desktop, ui, orchestration | 桌面化协作编码助手，将代理编排能力图形化。 |
| Amazon Bedrock AgentCore Samples | [GitHub](https://github.com/awslabs/agentcore-samples) | [![star](https://img.shields.io/badge/star-2773-f4b400?style=flat-square)](https://github.com/awslabs/agentcore-samples) | aws, runtime, operations | 官方示例套件，覆盖基于 Runtime、Gateway、Memory、可观测、评测与策略层的代理部署与运维。 |
| mini-coding-agent | [GitHub](https://github.com/rasbt/mini-coding-agent) | [![star](https://img.shields.io/badge/star-815-f4b400?style=flat-square)](https://github.com/rasbt/mini-coding-agent) | coding-agent, minimal, approvals | 极简编码 agent harness，实现了审批、记忆、受限委派与持久化转录等核心机制。 |
| AgentPlane | [GitHub](https://github.com/basilisk-labs/agentplane) | [![star](https://img.shields.io/badge/star-46-f4b400?style=flat-square)](https://github.com/basilisk-labs/agentplane) | coding-agent, git-native, workflow-control | 本地优先、Git 原生的编码代理 harness，将任务、计划、验证与收尾记录保存在仓库内。 |

<a id="essential-readings-ecosystem-maps"></a>
### Essential Readings & Ecosystem Maps

| 项目 | 链接 | Stars | 标签 | 简介 |
| --- | --- | --- | --- | --- |
| awesome-claude-code | [GitHub](https://github.com/hesreallyhim/awesome-claude-code) | [![star](https://img.shields.io/badge/star-42966-f4b400?style=flat-square)](https://github.com/hesreallyhim/awesome-claude-code) | awesome-list, claude-code, skills | Claude Code 技能、钩子与编排工具的社区清单。 |
| awesome-agentic-patterns | [GitHub](https://github.com/nibzard/awesome-agentic-patterns) | [![star](https://img.shields.io/badge/star-4483-f4b400?style=flat-square)](https://github.com/nibzard/awesome-agentic-patterns) | awesome-list, patterns, design | 可复用的 agentic 设计模式与实现范式目录。 |
| awesome-mcp-servers | [GitHub](https://github.com/wong2/awesome-mcp-servers) | [![star](https://img.shields.io/badge/star-4047-f4b400?style=flat-square)](https://github.com/wong2/awesome-mcp-servers) | awesome-list, mcp, tools | MCP server 精选索引，便于代理系统进行工具互操作。 |
| awesome-harness-engineering | [GitHub](https://github.com/walkinglabs/awesome-harness-engineering) | [![star](https://img.shields.io/badge/star-2319-f4b400?style=flat-square)](https://github.com/walkinglabs/awesome-harness-engineering) | awesome-list, curation, harness | 聚焦 harness engineering 的精选清单，覆盖文章、基准与实现。 |
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
@misc{awesome-agent-harness,
  title={Awesome Agent Harness},
  howpublished={\url{https://github.com/Picrew/awesome-agent-harness.git}},
  year={2026}
}
```

# Awesome Agent Harness

A curated, implementation-first list of **agent harness engineering** resources, with GitHub projects as the primary focus.

- Total entries: **141**
- GitHub entries: **119 (84.4%)**
- GitHub in project categories (excluding readings): **115/115 (100.0%)**
- Categories: **9**
- Last verified: **2026-04-08**
- Language: [English](./README.md) | [中文](./README_zh.md)

<a id="featured-harness-blogs"></a>
## Featured Harness Blogs

- [Harness engineering (OpenAI)](https://openai.com/index/harness-engineering/): Field report on building reliable agent-first software via harness constraints and verification.
- [Building Effective AI Agents](https://www.anthropic.com/engineering/building-effective-agents): Anthropic's practical guidance on when to use workflows vs. autonomous agents and how to structure them.
- [Writing effective tools for AI agents](https://www.anthropic.com/engineering/writing-tools-for-agents): Best practices for tool interface design so agents call tools safely and reliably.
- [Effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents): Practical guide to maintaining state, resumability, and reliability over long agent runs.
- [Harness design for long-running application development](https://www.anthropic.com/engineering/harness-design-long-running-apps): Follow-up article on improving long-running app generation through harness structure.
- [Improving Deep Agents with harness engineering](https://blog.langchain.com/improving-deep-agents-with-harness-engineering/): Evidence that harness improvements alone can move benchmark performance.
- [Evaluating Deep Agents: Our Learnings](https://blog.langchain.com/evaluating-deep-agents-our-learnings/): LangChain's practical lessons on evaluating stateful and long-horizon agents.
- [Your Agent Needs a Harness, Not a Framework](https://www.inngest.com/blog/your-agent-needs-a-harness-not-a-framework): Argument for reliability-first infrastructure around agents instead of framework-only thinking.
- [Skill Issue: Harness Engineering for Coding Agents](https://www.humanlayer.dev/blog/skill-issue-harness-engineering-for-coding-agents): Practical breakdown of why coding-agent quality depends heavily on harness setup.
- [Harness Engineering (Martin Fowler)](https://martinfowler.com/articles/exploring-gen-ai/harness-engineering.html): Architectural perspective on harness engineering and entropy control.

## Contents

- [Category Overview](#category-overview)
- [Featured Harness Blogs](#featured-harness-blogs)
- [Catalog](#catalog)
  - [Harness Architecture & Orchestration](#harness-architecture-orchestration)
  - [Context & Working-State Engineering](#context-working-state-engineering)
  - [Execution Substrates & Sandboxing](#execution-substrates-sandboxing)
  - [Protocols, Tool Interfaces & Agent Contracts](#protocols-tool-interfaces-agent-contracts)
  - [Evaluation Harnesses & Benchmarks](#evaluation-harnesses-benchmarks)
  - [Observability & Reliability Operations](#observability-reliability-operations)
  - [Guardrails, Security & Governance](#guardrails-security-governance)
  - [Reference Harness Implementations](#reference-harness-implementations)
  - [Essential Readings & Ecosystem Maps](#essential-readings-ecosystem-maps)
- [Maintenance Notes](#maintenance-notes)
- [Citation](#citation)

## Category Overview

| Category | Entries |
| --- | ---: |
| Harness Architecture & Orchestration | 17 |
| Context & Working-State Engineering | 8 |
| Execution Substrates & Sandboxing | 11 |
| Protocols, Tool Interfaces & Agent Contracts | 11 |
| Evaluation Harnesses & Benchmarks | 17 |
| Observability & Reliability Operations | 13 |
| Guardrails, Security & Governance | 11 |
| Reference Harness Implementations | 27 |
| Essential Readings & Ecosystem Maps | 26 |

## Catalog

Notes:
- `Stars` are rendered as badges from snapshot values.
- Repository update dates are tracked in `data/projects.yaml` and validation reports.
- Entries are sorted by stars (descending) within each category.

<a id="harness-architecture-orchestration"></a>
### Harness Architecture & Orchestration

| Project | Link | Stars | Tags | Summary |
| --- | --- | --- | --- | --- |
| DeerFlow | [GitHub](https://github.com/bytedance/deer-flow) | [![star](https://img.shields.io/badge/star-59504-f4b400?style=flat-square)](https://github.com/bytedance/deer-flow) | long-horizon, memory, subagents | Long-horizon super-agent harness integrating memory, tools, subagents, and sandboxes. |
| AutoGen | [GitHub](https://github.com/microsoft/autogen) | [![star](https://img.shields.io/badge/star-56818-f4b400?style=flat-square)](https://github.com/microsoft/autogen) | multi-agent, orchestration, framework | Programming framework for agentic AI with multi-agent interaction and orchestration. |
| Agno | [GitHub](https://github.com/agno-agi/agno) | [![star](https://img.shields.io/badge/star-39254-f4b400?style=flat-square)](https://github.com/agno-agi/agno) | scale, runtime, management | Agent software runtime focused on running and managing agentic systems at scale. |
| LangGraph | [GitHub](https://github.com/langchain-ai/langgraph) | [![star](https://img.shields.io/badge/star-28711-f4b400?style=flat-square)](https://github.com/langchain-ai/langgraph) | graph, workflow, runtime | Graph-based runtime for resilient stateful agents and deterministic workflow control. |
| Semantic Kernel | [GitHub](https://github.com/microsoft/semantic-kernel) | [![star](https://img.shields.io/badge/star-27669-f4b400?style=flat-square)](https://github.com/microsoft/semantic-kernel) | enterprise, orchestration, plugins | Enterprise-grade agentic application framework with orchestration and plugin patterns. |
| OpenAI Agents SDK (Python) | [GitHub](https://github.com/openai/openai-agents-python) | [![star](https://img.shields.io/badge/star-20647-f4b400?style=flat-square)](https://github.com/openai/openai-agents-python) | sdk, handoff, workflows | Lightweight framework for multi-agent workflows, handoffs, and production patterns. |
| deepagents | [GitHub](https://github.com/langchain-ai/deepagents) | [![star](https://img.shields.io/badge/star-19924-f4b400?style=flat-square)](https://github.com/langchain-ai/deepagents) | runtime, orchestration, long-running | Open-source harness for long-running, tool-using agents with planning and subagent patterns. |
| Google ADK (Python) | [GitHub](https://github.com/google/adk-python) | [![star](https://img.shields.io/badge/star-18817-f4b400?style=flat-square)](https://github.com/google/adk-python) | toolkit, deployment, evaluation | Code-first toolkit to build, evaluate, and deploy advanced AI agents. |
| PydanticAI | [GitHub](https://github.com/pydantic/pydantic-ai) | [![star](https://img.shields.io/badge/star-16173-f4b400?style=flat-square)](https://github.com/pydantic/pydantic-ai) | python, typing, schema | Type-safe Python framework for agents with strong schema contracts and tooling. |
| Hive | [GitHub](https://github.com/aden-hive/hive) | [![star](https://img.shields.io/badge/star-10130-f4b400?style=flat-square)](https://github.com/aden-hive/hive) | harness, orchestration, runtime | Outcome-driven agent runtime harness with explicit control loops and orchestration blocks. |
| Microsoft Agent Framework | [GitHub](https://github.com/microsoft/agent-framework) | [![star](https://img.shields.io/badge/star-9147-f4b400?style=flat-square)](https://github.com/microsoft/agent-framework) | multi-agent, workflows, observability | Multi-language framework for building, orchestrating, and deploying AI agents with graph workflows and observability. |
| mcp-agent | [GitHub](https://github.com/lastmile-ai/mcp-agent) | [![star](https://img.shields.io/badge/star-8210-f4b400?style=flat-square)](https://github.com/lastmile-ai/mcp-agent) | mcp, runtime, workflow | Practical agent framework centered on MCP tool ecosystems and workflow composition. |
| VoltAgent | [GitHub](https://github.com/VoltAgent/voltagent) | [![star](https://img.shields.io/badge/star-7584-f4b400?style=flat-square)](https://github.com/VoltAgent/voltagent) | typescript, platform, runtime | TypeScript agent engineering platform built around open runtime abstractions. |
| Yao | [GitHub](https://github.com/YaoApp/yao) | [![star](https://img.shields.io/badge/star-7526-f4b400?style=flat-square)](https://github.com/YaoApp/yao) | single-binary, runtime, autonomous | Single-binary runtime for defining and running autonomous agents. |
| Cloudflare Agents | [GitHub](https://github.com/cloudflare/agents) | [![star](https://img.shields.io/badge/star-4711-f4b400?style=flat-square)](https://github.com/cloudflare/agents) | platform, deployment, runtime | Platform runtime for building and deploying agents with production infrastructure primitives. |
| Docker Agent | [GitHub](https://github.com/docker/docker-agent) | [![star](https://img.shields.io/badge/star-2782-f4b400?style=flat-square)](https://github.com/docker/docker-agent) | docker, runtime, container | Agent builder and runtime stack emphasizing container-native execution. |
| NeMo Agent Toolkit | [GitHub](https://github.com/NVIDIA/NeMo-Agent-Toolkit) | [![star](https://img.shields.io/badge/star-2156-f4b400?style=flat-square)](https://github.com/NVIDIA/NeMo-Agent-Toolkit) | multi-agent, optimization, toolkit | Open toolkit for connecting and optimizing teams of AI agents. |

<a id="context-working-state-engineering"></a>
### Context & Working-State Engineering

| Project | Link | Stars | Tags | Summary |
| --- | --- | --- | --- | --- |
| everything-claude-code | [GitHub](https://github.com/affaan-m/everything-claude-code) | [![star](https://img.shields.io/badge/star-146376-f4b400?style=flat-square)](https://github.com/affaan-m/everything-claude-code) | context, skills, harness-practices | Large open repository of harness practices around memory, skills, and context control for coding agents. |
| claude-mem | [GitHub](https://github.com/thedotmack/claude-mem) | [![star](https://img.shields.io/badge/star-46322-f4b400?style=flat-square)](https://github.com/thedotmack/claude-mem) | memory, context, session | Plugin-style memory layer that captures session history and reinjects relevant context into future coding runs. |
| planning-with-files | [GitHub](https://github.com/OthmanAdi/planning-with-files) | [![star](https://img.shields.io/badge/star-18315-f4b400?style=flat-square)](https://github.com/OthmanAdi/planning-with-files) | planning, skills, persistence | Skill package for persistent file-based planning in coding-agent workflows. |
| Agent Skills for Context Engineering | [GitHub](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering) | [![star](https://img.shields.io/badge/star-14851-f4b400?style=flat-square)](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering) | skills, context, production | Large skill library oriented around context engineering and production agents. |
| Context-Engineering Handbook | [GitHub](https://github.com/davidkimai/Context-Engineering) | [![star](https://img.shields.io/badge/star-8686-f4b400?style=flat-square)](https://github.com/davidkimai/Context-Engineering) | context-engineering, handbook, practices | First-principles handbook focused on practical context engineering for agent systems. |
| Trellis | [GitHub](https://github.com/mindfold-ai/Trellis) | [![star](https://img.shields.io/badge/star-4938-f4b400?style=flat-square)](https://github.com/mindfold-ai/Trellis) | specs, memory, workflow | Multi-platform coding-agent workflow framework with task context, project memory, and spec injection. |
| Awesome Context Engineering | [GitHub](https://github.com/Meirtz/Awesome-Context-Engineering) | [![star](https://img.shields.io/badge/star-3037-f4b400?style=flat-square)](https://github.com/Meirtz/Awesome-Context-Engineering) | awesome-list, context, survey | Survey-style list for context engineering resources and frameworks. |
| context-space | [GitHub](https://github.com/context-space/context-space) | [![star](https://img.shields.io/badge/star-810-f4b400?style=flat-square)](https://github.com/context-space/context-space) | context, infrastructure, mcp | Infrastructure project focused on context engineering building blocks and MCP-centric integrations. |

<a id="execution-substrates-sandboxing"></a>
### Execution Substrates & Sandboxing

| Project | Link | Stars | Tags | Summary |
| --- | --- | --- | --- | --- |
| Daytona | [GitHub](https://github.com/daytonaio/daytona) | [![star](https://img.shields.io/badge/star-71857-f4b400?style=flat-square)](https://github.com/daytonaio/daytona) | sandbox, execution, infra | Secure and elastic sandbox infrastructure for running AI-generated code with file, Git, LSP, and execution APIs. |
| CUA | [GitHub](https://github.com/trycua/cua) | [![star](https://img.shields.io/badge/star-13427-f4b400?style=flat-square)](https://github.com/trycua/cua) | computer-use, sandbox, infra | Infrastructure stack for computer-use agents with sandbox, SDK, and benchmark support. |
| E2B | [GitHub](https://github.com/e2b-dev/E2B) | [![star](https://img.shields.io/badge/star-11628-f4b400?style=flat-square)](https://github.com/e2b-dev/E2B) | cloud-sandbox, execution, enterprise | Secure cloud environments with real tools for production-grade agent execution. |
| OpenSandbox | [GitHub](https://github.com/alibaba/OpenSandbox) | [![star](https://img.shields.io/badge/star-9836-f4b400?style=flat-square)](https://github.com/alibaba/OpenSandbox) | sandbox, security, runtime | Secure and extensible sandbox runtime built for agent workloads. |
| agent-infra sandbox | [GitHub](https://github.com/agent-infra/sandbox) | [![star](https://img.shields.io/badge/star-4135-f4b400?style=flat-square)](https://github.com/agent-infra/sandbox) | all-in-one, browser, shell | All-in-one sandbox combining browser, shell, files, MCP, and IDE server. |
| Judge0 | [GitHub](https://github.com/judge0/judge0) | [![star](https://img.shields.io/badge/star-4074-f4b400?style=flat-square)](https://github.com/judge0/judge0) | code-execution, sandbox, backend | Scalable sandboxed code execution system usable as an agent execution backend. |
| OSS-Fuzz Gen | [GitHub](https://github.com/google/oss-fuzz-gen) | [![star](https://img.shields.io/badge/star-1381-f4b400?style=flat-square)](https://github.com/google/oss-fuzz-gen) | fuzzing, security, execution | LLM-powered fuzzing workflows integrated with controlled execution contexts. |
| stakpak/agent | [GitHub](https://github.com/stakpak/agent) | [![star](https://img.shields.io/badge/star-1303-f4b400?style=flat-square)](https://github.com/stakpak/agent) | always-on, autonomous, ops | Always-on open agent that runs on your machines with autonomous operational loops. |
| SWE-ReX | [GitHub](https://github.com/SWE-agent/SWE-ReX) | [![star](https://img.shields.io/badge/star-472-f4b400?style=flat-square)](https://github.com/SWE-agent/SWE-ReX) | sandbox, execution, coding-agent | Sandboxed execution infrastructure for AI coding agents at local and cloud scale. |
| sandboxed.sh | [GitHub](https://github.com/Th0rgal/sandboxed.sh) | [![star](https://img.shields.io/badge/star-367-f4b400?style=flat-square)](https://github.com/Th0rgal/sandboxed.sh) | self-hosted, isolation, orchestrator | Self-hosted orchestrator running coding agents inside isolated Linux workspaces. |
| terminal-bench-env | [GitHub](https://github.com/ucsb-mlsec/terminal-bench-env) | [![star](https://img.shields.io/badge/star-89-f4b400?style=flat-square)](https://github.com/ucsb-mlsec/terminal-bench-env) | terminal, benchmark-env, sandbox | Environment layer for terminal-agent benchmark execution. |

<a id="protocols-tool-interfaces-agent-contracts"></a>
### Protocols, Tool Interfaces & Agent Contracts

| Project | Link | Stars | Tags | Summary |
| --- | --- | --- | --- | --- |
| GitHub Spec Kit | [GitHub](https://github.com/github/spec-kit) | [![star](https://img.shields.io/badge/star-86218-f4b400?style=flat-square)](https://github.com/github/spec-kit) | spec-driven, workflows, tooling | Toolkit for spec-driven development to guide deterministic agent execution. |
| MCP Servers | [GitHub](https://github.com/modelcontextprotocol/servers) | [![star](https://img.shields.io/badge/star-83234-f4b400?style=flat-square)](https://github.com/modelcontextprotocol/servers) | mcp, servers, implementations | Official collection of MCP server implementations across tools and domains. |
| AGENTS.md | [GitHub](https://github.com/agentsmd/agents.md) | [![star](https://img.shields.io/badge/star-19880-f4b400?style=flat-square)](https://github.com/agentsmd/agents.md) | spec, agent-file, instructions | Open format for repository-local instructions that coding agents can follow. |
| Model Context Protocol | [GitHub](https://github.com/modelcontextprotocol/modelcontextprotocol) | [![star](https://img.shields.io/badge/star-7750-f4b400?style=flat-square)](https://github.com/modelcontextprotocol/modelcontextprotocol) | mcp, protocol, interoperability | Core specification and docs for MCP-based tool and context interoperability. |
| directories (rules and MCP indexes) | [GitHub](https://github.com/leerob/directories) | [![star](https://img.shields.io/badge/star-3917-f4b400?style=flat-square)](https://github.com/leerob/directories) | directories, mcp, rules | Curated directories of agent rules and MCP servers for tool discovery. |
| LangChain MCP Adapters | [GitHub](https://github.com/langchain-ai/langchain-mcp-adapters) | [![star](https://img.shields.io/badge/star-3475-f4b400?style=flat-square)](https://github.com/langchain-ai/langchain-mcp-adapters) | mcp, adapters, integration | Adapters connecting LangChain components with MCP servers. |
| Microsoft MCP Servers | [GitHub](https://github.com/microsoft/mcp) | [![star](https://img.shields.io/badge/star-2928-f4b400?style=flat-square)](https://github.com/microsoft/mcp) | mcp, enterprise, servers | Microsoft's official MCP server catalog for enterprise data and tools. |
| ACPX | [GitHub](https://github.com/openclaw/acpx) | [![star](https://img.shields.io/badge/star-2029-f4b400?style=flat-square)](https://github.com/openclaw/acpx) | acp, client, sessions | Headless CLI client for stateful Agent Client Protocol sessions. |
| Microsoft Learn MCP | [GitHub](https://github.com/MicrosoftDocs/mcp) | [![star](https://img.shields.io/badge/star-1528-f4b400?style=flat-square)](https://github.com/MicrosoftDocs/mcp) | mcp, docs, grounding | MCP server and CLI for grounding agents with Microsoft documentation sources. |
| IBM MCP | [GitHub](https://github.com/IBM/mcp) | [![star](https://img.shields.io/badge/star-362-f4b400?style=flat-square)](https://github.com/IBM/mcp) | mcp, clients, tooling | IBM collection of MCP servers, clients, and developer tooling. |
| AGENT.md | [GitHub](https://github.com/agentmd/agent.md) | [![star](https://img.shields.io/badge/star-72-f4b400?style=flat-square)](https://github.com/agentmd/agent.md) | standard, agent-file, interoperability | Standardized machine-readable file format for agentic coding tools. |

<a id="evaluation-harnesses-benchmarks"></a>
### Evaluation Harnesses & Benchmarks

| Project | Link | Stars | Tags | Summary |
| --- | --- | --- | --- | --- |
| Promptfoo | [GitHub](https://github.com/promptfoo/promptfoo) | [![star](https://img.shields.io/badge/star-19753-f4b400?style=flat-square)](https://github.com/promptfoo/promptfoo) | eval, red-team, ci | Config-driven prompt/agent/RAG testing, comparison, and red-team evaluation tool. |
| DeepEval | [GitHub](https://github.com/confident-ai/deepeval) | [![star](https://img.shields.io/badge/star-14618-f4b400?style=flat-square)](https://github.com/confident-ai/deepeval) | evaluation, framework, testing | LLM evaluation framework supporting agent and workflow quality testing. |
| RAGAS | [GitHub](https://github.com/vibrantlabsai/ragas) | [![star](https://img.shields.io/badge/star-13281-f4b400?style=flat-square)](https://github.com/vibrantlabsai/ragas) | rag, metrics, evaluation | Open evaluation toolkit for LLM and RAG quality metrics. |
| lm-evaluation-harness | [GitHub](https://github.com/EleutherAI/lm-evaluation-harness) | [![star](https://img.shields.io/badge/star-12057-f4b400?style=flat-square)](https://github.com/EleutherAI/lm-evaluation-harness) | benchmark, harness, llm | Popular benchmark harness for consistent LLM evaluation across tasks. |
| SWE-bench | [GitHub](https://github.com/SWE-bench/SWE-bench) | [![star](https://img.shields.io/badge/star-4648-f4b400?style=flat-square)](https://github.com/SWE-bench/SWE-bench) | benchmark, swe, evaluation | Standard benchmark for evaluating issue-fixing software engineering agents. |
| verifiers | [GitHub](https://github.com/PrimeIntellect-ai/verifiers) | [![star](https://img.shields.io/badge/star-3985-f4b400?style=flat-square)](https://github.com/PrimeIntellect-ai/verifiers) | verifier, rl, evaluation | Library for RL environments and verifier-based evaluation loops. |
| AgentBench | [GitHub](https://github.com/THUDM/AgentBench) | [![star](https://img.shields.io/badge/star-3310-f4b400?style=flat-square)](https://github.com/THUDM/AgentBench) | benchmark, cross-domain, agent | Cross-environment benchmark for evaluating LLM agents as tool-using systems. |
| LangWatch | [GitHub](https://github.com/langwatch/langwatch) | [![star](https://img.shields.io/badge/star-3187-f4b400?style=flat-square)](https://github.com/langwatch/langwatch) | simulation, evaluation, testing | End-to-end platform for agent simulations, evaluation loops, and production testing. |
| EvalScope | [GitHub](https://github.com/modelscope/evalscope) | [![star](https://img.shields.io/badge/star-2626-f4b400?style=flat-square)](https://github.com/modelscope/evalscope) | benchmark, framework, llm | Customizable framework for large-model benchmarking and performance evaluation. |
| Terminal-Bench | [GitHub](https://github.com/harbor-framework/terminal-bench) | [![star](https://img.shields.io/badge/star-1931-f4b400?style=flat-square)](https://github.com/harbor-framework/terminal-bench) | terminal, benchmark, long-horizon | Terminal-native benchmark suite for long-horizon, verification-heavy agent tasks. |
| Harbor | [GitHub](https://github.com/harbor-framework/harbor) | [![star](https://img.shields.io/badge/star-1370-f4b400?style=flat-square)](https://github.com/harbor-framework/harbor) | evaluation, harness, rl-env | Framework for running agent evaluations and constructing RL-style environments. |
| tau2-bench | [GitHub](https://github.com/sierra-research/tau2-bench) | [![star](https://img.shields.io/badge/star-975-f4b400?style=flat-square)](https://github.com/sierra-research/tau2-bench) | tool-use, interaction, benchmark | Tool-agent-user interaction benchmark emphasizing multi-step execution quality. |
| NeMo Gym | [GitHub](https://github.com/NVIDIA-NeMo/Gym) | [![star](https://img.shields.io/badge/star-805-f4b400?style=flat-square)](https://github.com/NVIDIA-NeMo/Gym) | rl-env, training, evaluation | Toolkit for building RL environments suitable for LLM/agent training and eval. |
| Inspect Evals | [GitHub](https://github.com/UKGovernmentBEIS/inspect_evals) | [![star](https://img.shields.io/badge/star-428-f4b400?style=flat-square)](https://github.com/UKGovernmentBEIS/inspect_evals) | inspect, eval-suite, reproducibility | Evaluation suite collection for Inspect AI workflows. |
| WorkArena | [GitHub](https://github.com/ServiceNow/WorkArena) | [![star](https://img.shields.io/badge/star-242-f4b400?style=flat-square)](https://github.com/ServiceNow/WorkArena) | browser, benchmark, enterprise | Browser benchmark for practical enterprise-like knowledge work tasks. |
| OpenHands Benchmarks | [GitHub](https://github.com/OpenHands/benchmarks) | [![star](https://img.shields.io/badge/star-63-f4b400?style=flat-square)](https://github.com/OpenHands/benchmarks) | openhands, eval, harness | Evaluation harness and benchmark definitions for OpenHands systems. |
| WebArena-Verified | [GitHub](https://github.com/ServiceNow/webarena-verified) | [![star](https://img.shields.io/badge/star-34-f4b400?style=flat-square)](https://github.com/ServiceNow/webarena-verified) | web-agent, benchmark, deterministic | Verified web-agent benchmark with deterministic evaluators. |

<a id="observability-reliability-operations"></a>
### Observability & Reliability Operations

| Project | Link | Stars | Tags | Summary |
| --- | --- | --- | --- | --- |
| MLflow | [GitHub](https://github.com/mlflow/mlflow) | [![star](https://img.shields.io/badge/star-25211-f4b400?style=flat-square)](https://github.com/mlflow/mlflow) | platform, monitoring, evaluation | Broad AI engineering platform with monitoring and evaluation support for agents. |
| Langfuse | [GitHub](https://github.com/langfuse/langfuse) | [![star](https://img.shields.io/badge/star-24557-f4b400?style=flat-square)](https://github.com/langfuse/langfuse) | llmops, tracing, metrics | Open-source LLM engineering platform for traces, metrics, prompts, and evals. |
| Opik | [GitHub](https://github.com/comet-ml/opik) | [![star](https://img.shields.io/badge/star-18716-f4b400?style=flat-square)](https://github.com/comet-ml/opik) | monitoring, eval, tracing | End-to-end debug/eval/monitoring stack for LLM apps and agent workflows. |
| RagaAI Catalyst | [GitHub](https://github.com/raga-ai-hub/RagaAI-Catalyst) | [![star](https://img.shields.io/badge/star-16126-f4b400?style=flat-square)](https://github.com/raga-ai-hub/RagaAI-Catalyst) | agentops, analytics, monitoring | Agent observability and monitoring framework with timeline and graph analytics. |
| TensorZero | [GitHub](https://github.com/tensorzero/tensorzero) | [![star](https://img.shields.io/badge/star-11189-f4b400?style=flat-square)](https://github.com/tensorzero/tensorzero) | llmops, gateway, optimization | Open LLMOps stack unifying gateway, observability, evaluation, and optimization. |
| Arize Phoenix | [GitHub](https://github.com/Arize-ai/phoenix) | [![star](https://img.shields.io/badge/star-9205-f4b400?style=flat-square)](https://github.com/Arize-ai/phoenix) | observability, tracing, evaluation | Open platform for AI observability, tracing, and evaluation analytics. |
| OpenLLMetry | [GitHub](https://github.com/traceloop/openllmetry) | [![star](https://img.shields.io/badge/star-6987-f4b400?style=flat-square)](https://github.com/traceloop/openllmetry) | opentelemetry, instrumentation, tracing | OpenTelemetry-based instrumentation for GenAI and LLM applications. |
| Helicone | [GitHub](https://github.com/Helicone/helicone) | [![star](https://img.shields.io/badge/star-5463-f4b400?style=flat-square)](https://github.com/Helicone/helicone) | monitoring, traffic, production | Lightweight platform for monitoring and evaluating LLM traffic in production. |
| AgentOps SDK | [GitHub](https://github.com/AgentOps-AI/agentops) | [![star](https://img.shields.io/badge/star-5445-f4b400?style=flat-square)](https://github.com/AgentOps-AI/agentops) | agentops, monitoring, cost | Monitoring and benchmarking SDK for agent workflows with cost and trace tracking. |
| Latitude | [GitHub](https://github.com/latitude-dev/latitude-llm) | [![star](https://img.shields.io/badge/star-3948-f4b400?style=flat-square)](https://github.com/latitude-dev/latitude-llm) | platform, eval, observability | Open-source agent engineering platform with eval and observability capabilities. |
| Laminar | [GitHub](https://github.com/lmnr-ai/lmnr) | [![star](https://img.shields.io/badge/star-2769-f4b400?style=flat-square)](https://github.com/lmnr-ai/lmnr) | observability, tracing, evals | Agent-focused observability stack with tracing, evaluation runs, monitoring, and dashboards. |
| claude-code-reverse | [GitHub](https://github.com/Yuyz0112/claude-code-reverse) | [![star](https://img.shields.io/badge/star-2338-f4b400?style=flat-square)](https://github.com/Yuyz0112/claude-code-reverse) | trace, visualization, debugging | Tooling to visualize and inspect Claude Code LLM interaction traces. |
| OpenInference | [GitHub](https://github.com/Arize-ai/openinference) | [![star](https://img.shields.io/badge/star-913-f4b400?style=flat-square)](https://github.com/Arize-ai/openinference) | spec, instrumentation, observability | Open instrumentation specification and tooling for AI observability. |

<a id="guardrails-security-governance"></a>
### Guardrails, Security & Governance

| Project | Link | Stars | Tags | Summary |
| --- | --- | --- | --- | --- |
| Kong | [GitHub](https://github.com/Kong/kong) | [![star](https://img.shields.io/badge/star-43136-f4b400?style=flat-square)](https://github.com/Kong/kong) | gateway, policy, infra | API and AI gateway infrastructure useful for policy enforcement in agent systems. |
| LiteLLM | [GitHub](https://github.com/BerriAI/litellm) | [![star](https://img.shields.io/badge/star-42570-f4b400?style=flat-square)](https://github.com/BerriAI/litellm) | gateway, proxy, guardrails | Unified LLM gateway/proxy with cost tracking, load balancing, and guardrails. |
| Portkey Gateway | [GitHub](https://github.com/Portkey-AI/gateway) | [![star](https://img.shields.io/badge/star-11245-f4b400?style=flat-square)](https://github.com/Portkey-AI/gateway) | gateway, guardrails, routing | AI gateway with routing and guardrails for multi-model production traffic. |
| CAI (Cybersecurity AI) | [GitHub](https://github.com/aliasrobotics/cai) | [![star](https://img.shields.io/badge/star-7895-f4b400?style=flat-square)](https://github.com/aliasrobotics/cai) | security, governance, framework | Security-focused agent framework for offensive/defensive AI workflows. |
| OpenAI Realtime Agents | [GitHub](https://github.com/openai/openai-realtime-agents) | [![star](https://img.shields.io/badge/star-6819-f4b400?style=flat-square)](https://github.com/openai/openai-realtime-agents) | realtime, orchestration, control | Advanced agentic realtime patterns with structured control and interaction loops. |
| Plano | [GitHub](https://github.com/katanemo/plano) | [![star](https://img.shields.io/badge/star-6233-f4b400?style=flat-square)](https://github.com/katanemo/plano) | proxy, safety, data-plane | AI-native proxy and data plane with orchestration, safety, and observability. |
| OpenAI CS Agents Demo | [GitHub](https://github.com/openai/openai-cs-agents-demo) | [![star](https://img.shields.io/badge/star-5954-f4b400?style=flat-square)](https://github.com/openai/openai-cs-agents-demo) | demo, handoffs, governance | Customer-service multi-agent demo highlighting handoffs and guardrail-like control points. |
| Tracecat | [GitHub](https://github.com/TracecatHQ/tracecat) | [![star](https://img.shields.io/badge/star-3545-f4b400?style=flat-square)](https://github.com/TracecatHQ/tracecat) | security, automation, policy | AI automation platform for security teams with policy and workflow controls. |
| Archestra | [GitHub](https://github.com/archestra-ai/archestra) | [![star](https://img.shields.io/badge/star-3539-f4b400?style=flat-square)](https://github.com/archestra-ai/archestra) | enterprise, guardrails, governance | Enterprise AI platform with guardrails, MCP registry, and orchestration services. |
| ContextForge | [GitHub](https://github.com/IBM/mcp-context-forge) | [![star](https://img.shields.io/badge/star-3539-f4b400?style=flat-square)](https://github.com/IBM/mcp-context-forge) | gateway, governance, observability | Registry and proxy layer that unifies MCP, A2A, and REST/gRPC endpoints with centralized governance and observability. |
| AgentGateway | [GitHub](https://github.com/agentgateway/agentgateway) | [![star](https://img.shields.io/badge/star-2319-f4b400?style=flat-square)](https://github.com/agentgateway/agentgateway) | gateway, mcp, proxy | Agentic proxy gateway for AI agents and MCP server ecosystems. |

<a id="reference-harness-implementations"></a>
### Reference Harness Implementations

| Project | Link | Stars | Tags | Summary |
| --- | --- | --- | --- | --- |
| OpenCode | [GitHub](https://github.com/anomalyco/opencode) | [![star](https://img.shields.io/badge/star-139654-f4b400?style=flat-square)](https://github.com/anomalyco/opencode) | terminal, coding-agent, subagents | Open-source coding agent with built-in plan/build roles, subagents, LSP support, and a client-server runtime. |
| Claude Code | [GitHub](https://github.com/anthropics/claude-code) | [![star](https://img.shields.io/badge/star-111064-f4b400?style=flat-square)](https://github.com/anthropics/claude-code) | terminal, coding-agent, git-workflows | Official terminal coding agent that understands codebases and executes editing, debugging, and Git workflows through natural language. |
| Gemini CLI | [GitHub](https://github.com/google-gemini/gemini-cli) | [![star](https://img.shields.io/badge/star-100614-f4b400?style=flat-square)](https://github.com/google-gemini/gemini-cli) | terminal, coding-agent, mcp | Open-source terminal agent with built-in tools, MCP support, checkpointing, and sandboxing controls. |
| Codex CLI | [GitHub](https://github.com/openai/codex) | [![star](https://img.shields.io/badge/star-73908-f4b400?style=flat-square)](https://github.com/openai/codex) | terminal, coding-agent, local-execution | Terminal-native coding agent that runs locally and exposes practical agent workflows for software tasks. |
| OpenHands | [GitHub](https://github.com/OpenHands/OpenHands) | [![star](https://img.shields.io/badge/star-70823-f4b400?style=flat-square)](https://github.com/OpenHands/OpenHands) | coding-agent, software-engineering, repo | Open-source AI software engineer focused on repo-level coding task execution. |
| OpenManus | [GitHub](https://github.com/FoundationAgents/OpenManus) | [![star](https://img.shields.io/badge/star-55656-f4b400?style=flat-square)](https://github.com/FoundationAgents/OpenManus) | general-agent, autonomy, workflows | Open foundation for broad autonomous agent workflows with coding-heavy use cases. |
| learn-claude-code | [GitHub](https://github.com/shareAI-lab/learn-claude-code) | [![star](https://img.shields.io/badge/star-50187-f4b400?style=flat-square)](https://github.com/shareAI-lab/learn-claude-code) | tutorial, harness, claude-code | Hands-on harness tutorial for building Claude Code-like systems from scratch. |
| aider | [GitHub](https://github.com/Aider-AI/aider) | [![star](https://img.shields.io/badge/star-43006-f4b400?style=flat-square)](https://github.com/Aider-AI/aider) | terminal, repo-map, testing | Terminal coding assistant with repo mapping, git-aware edits, and built-in lint/test feedback loops. |
| Claude Code Plugins: Orchestration and Automation | [GitHub](https://github.com/wshobson/agents) | [![star](https://img.shields.io/badge/star-33171-f4b400?style=flat-square)](https://github.com/wshobson/agents) | claude-code, plugins, orchestration | Production-ready Claude Code plugin marketplace bundling agents, skills, tools, and multi-agent workflow orchestrators. |
| CLI-Anything | [GitHub](https://github.com/HKUDS/CLI-Anything) | [![star](https://img.shields.io/badge/star-29375-f4b400?style=flat-square)](https://github.com/HKUDS/CLI-Anything) | cli, tool-use, automation | CLI agent system that unifies command-line tool usage in agent loops. |
| SuperClaude Framework | [GitHub](https://github.com/SuperClaude-Org/SuperClaude_Framework) | [![star](https://img.shields.io/badge/star-22205-f4b400?style=flat-square)](https://github.com/SuperClaude-Org/SuperClaude_Framework) | config, personas, workflow | Configuration framework adding commands, personas, and method templates to coding agents. |
| Qwen Code | [GitHub](https://github.com/QwenLM/qwen-code) | [![star](https://img.shields.io/badge/star-22130-f4b400?style=flat-square)](https://github.com/QwenLM/qwen-code) | terminal, coding-agent, cli | Terminal-native open-source coding agent tuned for practical dev loops. |
| Devika | [GitHub](https://github.com/stitionai/devika) | [![star](https://img.shields.io/badge/star-19499-f4b400?style=flat-square)](https://github.com/stitionai/devika) | assistant, planning, coding | Open-source coding assistant system for planning and implementing development tasks. |
| SWE-agent | [GitHub](https://github.com/SWE-agent/SWE-agent) | [![star](https://img.shields.io/badge/star-18951-f4b400?style=flat-square)](https://github.com/SWE-agent/SWE-agent) | swe, issue-fixing, tooling | Research-grade coding agent that resolves GitHub issues with explicit tooling loops. |
| Aperant | [GitHub](https://github.com/AndyMik90/Aperant) | [![star](https://img.shields.io/badge/star-13866-f4b400?style=flat-square)](https://github.com/AndyMik90/Aperant) | coding-agent, parallel, memory | Autonomous multi-agent coding framework with parallel execution, isolated workspaces, QA loops, and persistent memory. |
| Eigent | [GitHub](https://github.com/eigent-ai/eigent) | [![star](https://img.shields.io/badge/star-13484-f4b400?style=flat-square)](https://github.com/eigent-ai/eigent) | desktop, cowork, productivity | Open-source desktop cowork agent for autonomous task execution and productivity. |
| GitHub Copilot CLI | [GitHub](https://github.com/github/copilot-cli) | [![star](https://img.shields.io/badge/star-9899-f4b400?style=flat-square)](https://github.com/github/copilot-cli) | terminal, coding-agent, mcp | Official terminal coding agent built on GitHub's Copilot harness with MCP extensibility, approval controls, and GitHub-native context. |
| Open SWE | [GitHub](https://github.com/langchain-ai/open-swe) | [![star](https://img.shields.io/badge/star-9315-f4b400?style=flat-square)](https://github.com/langchain-ai/open-swe) | async, coding-agent, swe | Asynchronous open-source coding agent focused on software issue workflows. |
| OpenHarness | [GitHub](https://github.com/HKUDS/OpenHarness) | [![star](https://img.shields.io/badge/star-7637-f4b400?style=flat-square)](https://github.com/HKUDS/OpenHarness) | tool-use, memory, multi-agent | Open agent harness implementation covering tool use, skills, memory, permissions, and multi-agent coordination. |
| OSAURUS | [GitHub](https://github.com/osaurus-ai/osaurus) | [![star](https://img.shields.io/badge/star-4675-f4b400?style=flat-square)](https://github.com/osaurus-ai/osaurus) | macos, local-first, memory | Native macOS harness for autonomous coding agents with persistent memory. |
| HiClaw | [GitHub](https://github.com/agentscope-ai/HiClaw) | [![star](https://img.shields.io/badge/star-3975-f4b400?style=flat-square)](https://github.com/agentscope-ai/HiClaw) | multi-agent, human-in-the-loop, shared-state | Collaborative multi-agent OS with manager-worker coordination, shared state, and human-in-the-loop oversight via Matrix rooms. |
| mini-swe-agent | [GitHub](https://github.com/SWE-agent/mini-swe-agent) | [![star](https://img.shields.io/badge/star-3721-f4b400?style=flat-square)](https://github.com/SWE-agent/mini-swe-agent) | minimal, swe, coding-agent | Minimal coding agent implementation with strong benchmark competitiveness. |
| TinyAGI | [GitHub](https://github.com/TinyAGI/tinyagi) | [![star](https://img.shields.io/badge/star-3491-f4b400?style=flat-square)](https://github.com/TinyAGI/tinyagi) | team-orchestration, autonomous, workflows | Team-style agent orchestrator for one-person-company style autonomous workflows. |
| Devon | [GitHub](https://github.com/entropy-research/Devon) | [![star](https://img.shields.io/badge/star-3450-f4b400?style=flat-square)](https://github.com/entropy-research/Devon) | pair-programming, coding-agent, autonomous | Open-source pair programmer agent with autonomous coding execution patterns. |
| Open Claude Cowork | [GitHub](https://github.com/DevAgentForge/Open-Claude-Cowork) | [![star](https://img.shields.io/badge/star-3159-f4b400?style=flat-square)](https://github.com/DevAgentForge/Open-Claude-Cowork) | desktop, ui, orchestration | Desktop coding cowork assistant that turns agent orchestration into GUI workflows. |
| oh-my-pi | [GitHub](https://github.com/can1357/oh-my-pi) | [![star](https://img.shields.io/badge/star-2764-f4b400?style=flat-square)](https://github.com/can1357/oh-my-pi) | terminal, lsp, subagents | Terminal AI coding agent with edit safety, LSP integration, and subagent support. |
| Amazon Bedrock AgentCore Samples | [GitHub](https://github.com/awslabs/agentcore-samples) | [![star](https://img.shields.io/badge/star-2586-f4b400?style=flat-square)](https://github.com/awslabs/agentcore-samples) | aws, runtime, operations | Official sample suite for deploying and operating agents with runtime, gateway, memory, observability, evaluation, and policy layers. |
| Uni-CLI | [GitHub](https://github.com/olo-dot-io/Uni-CLI) | [![star](https://img.shields.io/github/stars/olo-dot-io/Uni-CLI?style=flat-square&label=star&color=f4b400)](https://github.com/olo-dot-io/Uni-CLI) | cli-hub, mcp-gateway, self-repair | Universal CLI hub connecting agents to 134 sites and desktop apps via 711 declarative YAML pipelines. Ships an 8-phase Karpathy-style self-repair loop, eval harness catalog, per-call cost ledger, sensitive-path deny list, and `unicli mcp serve` that auto-registers one MCP tool per adapter. |

<a id="essential-readings-ecosystem-maps"></a>
### Essential Readings & Ecosystem Maps

| Project | Link | Stars | Tags | Summary |
| --- | --- | --- | --- | --- |
| awesome-claude-code | [GitHub](https://github.com/hesreallyhim/awesome-claude-code) | [![star](https://img.shields.io/badge/star-37460-f4b400?style=flat-square)](https://github.com/hesreallyhim/awesome-claude-code) | awesome-list, claude-code, skills | Community collection of Claude Code skills, hooks, and orchestrator tooling. |
| awesome-agentic-patterns | [GitHub](https://github.com/nibzard/awesome-agentic-patterns) | [![star](https://img.shields.io/badge/star-4239-f4b400?style=flat-square)](https://github.com/nibzard/awesome-agentic-patterns) | awesome-list, patterns, design | Catalog of reusable agentic design patterns and implementation motifs. |
| awesome-mcp-servers | [GitHub](https://github.com/wong2/awesome-mcp-servers) | [![star](https://img.shields.io/badge/star-3884-f4b400?style=flat-square)](https://github.com/wong2/awesome-mcp-servers) | awesome-list, mcp, tools | Curated MCP server index for tool interoperability in agent systems. |
| awesome-harness-engineering | [GitHub](https://github.com/walkinglabs/awesome-harness-engineering) | [![star](https://img.shields.io/badge/star-1440-f4b400?style=flat-square)](https://github.com/walkinglabs/awesome-harness-engineering) | awesome-list, curation, harness | Curated list focused on harness engineering articles, benchmarks, and implementations. |
| 12 Factor Agents | [Reference](https://www.humanlayer.dev/blog/12-factor-agents) | - | reading, operations, principles | Operations-oriented principles for building maintainable production agents. |
| Agent Frameworks, Runtimes, and Harnesses, oh my! | [Reference](https://blog.langchain.com/agent-frameworks-runtimes-and-harnesses-oh-my/) | - | reading, langchain, architecture | Clear decomposition of framework vs runtime vs harness responsibilities. |
| Building agents with the Claude Agent SDK | [Reference](https://claude.com/blog/building-agents-with-the-claude-agent-sdk) | - | reading, claude, sdk | Claude blog on production-oriented SDK usage for sessions, tools, and orchestration. |
| Building Effective AI Agents | [Reference](https://www.anthropic.com/engineering/building-effective-agents) | - | reading, anthropic, agents | Anthropic's practical guidance on when to use workflows vs. autonomous agents and how to structure them. |
| Claude Code sandboxing | [Reference](https://www.anthropic.com/engineering/claude-code-sandboxing) | - | reading, anthropic, sandboxing | How sandbox policy design improves autonomy while preserving security constraints. |
| Code execution with MCP | [Reference](https://www.anthropic.com/engineering/code-execution-with-mcp) | - | reading, anthropic, mcp | Anthropic's design notes on controlled code execution via MCP boundaries. |
| Demystifying Evals for AI Agents | [Reference](https://www.anthropic.com/engineering/demystifying-evals-for-ai-agents) | - | reading, evals, anthropic | Methodology for designing robust agent evals in non-deterministic trajectories. |
| Effective context engineering for AI agents | [Reference](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) | - | reading, context, anthropic | Guidance on context-window budgeting and working-state management for agents. |
| Effective harnesses for long-running agents | [Reference](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents) | - | reading, long-running, anthropic | Practical guide to maintaining state, resumability, and reliability over long agent runs. |
| Evaluating Deep Agents: Our Learnings | [Reference](https://blog.langchain.com/evaluating-deep-agents-our-learnings/) | - | reading, langchain, evaluation | LangChain's practical lessons on evaluating stateful and long-horizon agents. |
| Harness design for long-running application development | [Reference](https://www.anthropic.com/engineering/harness-design-long-running-apps) | - | reading, app-dev, anthropic | Follow-up article on improving long-running app generation through harness structure. |
| Harness Engineering (Martin Fowler) | [Reference](https://martinfowler.com/articles/exploring-gen-ai/harness-engineering.html) | - | reading, architecture, fowler | Architectural perspective on harness engineering and entropy control. |
| Harness engineering (OpenAI) | [Reference](https://openai.com/index/harness-engineering/) | - | reading, methodology, openai | Field report on building reliable agent-first software via harness constraints and verification. |
| How we built our multi-agent research system | [Reference](https://www.anthropic.com/engineering/multi-agent-research-system) | - | reading, anthropic, multi-agent | Anthropic architecture write-up on role separation and coordination in multi-agent systems. |
| Improving Deep Agents with harness engineering | [Reference](https://blog.langchain.com/improving-deep-agents-with-harness-engineering/) | - | reading, langchain, harness | Evidence that harness improvements alone can move benchmark performance. |
| Quantifying infrastructure noise in agentic coding evals | [Reference](https://www.anthropic.com/engineering/infrastructure-noise) | - | reading, anthropic, evaluation | Analysis of how infrastructure choices impact coding-agent benchmark outcomes. |
| Skill Issue: Harness Engineering for Coding Agents | [Reference](https://www.humanlayer.dev/blog/skill-issue-harness-engineering-for-coding-agents) | - | reading, humanlayer, coding-agents | Practical breakdown of why coding-agent quality depends heavily on harness setup. |
| Testing Agent Skills Systematically with Evals | [Reference](https://developers.openai.com/blog/eval-skills) | - | reading, openai, evals | OpenAI Developers guide for turning agent traces into repeatable skill evaluations. |
| The Anatomy of an Agent Harness | [Reference](https://blog.langchain.com/the-anatomy-of-an-agent-harness/) | - | reading, architecture, langchain | Conceptual decomposition of agent harness components and their responsibilities. |
| Unrolling the Codex agent loop | [Reference](https://openai.com/index/unrolling-the-codex-agent-loop/) | - | reading, openai, architecture | OpenAI engineering deep dive into the Codex harness loop, prompt growth, tool-call replay, and stateless execution tradeoffs. |
| Writing effective tools for AI agents | [Reference](https://www.anthropic.com/engineering/writing-tools-for-agents) | - | reading, anthropic, tools | Best practices for tool interface design so agents call tools safely and reliably. |
| Your Agent Needs a Harness, Not a Framework | [Reference](https://www.inngest.com/blog/your-agent-needs-a-harness-not-a-framework) | - | reading, inngest, reliability | Argument for reliability-first infrastructure around agents instead of framework-only thinking. |

## Maintenance Notes

- Source of truth: `data/projects.yaml`
- Regenerate README files: `python3 scripts/render_readme.py`
- Verify catalog and links: `python3 scripts/verify_catalog.py`

## Citation

```bibtex
@misc{awesome-agent-harness,
  title={Awesome Agent Harness},
  howpublished={\url{https://github.com/Picrew/awesome-agent-harness.git}},
  year={2026}
}
```

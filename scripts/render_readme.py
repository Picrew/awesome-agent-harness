#!/usr/bin/env python3
from __future__ import annotations

import argparse
from collections import OrderedDict, defaultdict
from pathlib import Path
from typing import Any

import yaml

ROOT = Path(__file__).resolve().parents[1]
DATA_FILE = ROOT / "data" / "projects.yaml"
README_EN = ROOT / "README.md"
README_ZH = ROOT / "README_zh.md"

AGENT_HARNESS_CITATION = [
    "@misc{li2026agentharness,",
    "  title={Agent Harness Engineering: A Survey},",
    "  author={Li, Junjie and Xiao, Xi and Zhang, Yunbei and Liu, Chen and Zhao, Lin and Liao, Xiaoying and Ji, Yingrui and Wang, Janet and Gu, Jianyang and Ge, Yingqiang and Xu, Weijie and Fang, Xi and Xu, Xiang and Zhao, Tianchen and Kim, Youngeun and Wang, Tianyang and Hamm, Jihun and Krishnaswamy, Smita and Huan, Jun and Reddy, Chandan},",
    "  url={https://openreview.net/pdf?id=eONq7FdiHa},",
    "  year={2026}",
    "}",
]

REQUIRED_ENTRY_FIELDS = [
    "name",
    "repo_url",
    "category",
    "summary_en",
    "summary_zh",
    "tags",
    "stars_snapshot",
    "updated_at",
    "why_included",
]
READINGS_CATEGORY = "Essential Readings & Ecosystem Maps"
FEATURED_READING_NAMES = [
    "Scaling Managed Agents: Decoupling the brain from the hands",
    "What We Learned Building Cloud Agents",
    "Claude Code auto mode",
    "Harness engineering (OpenAI)",
    "The next evolution of the Agents SDK",
    "Building Effective AI Agents",
    "Writing effective tools for AI agents",
    "Effective harnesses for long-running agents",
    "Harness design for long-running application development",
    "Improving Deep Agents with harness engineering",
    "Evaluating Deep Agents: Our Learnings",
    "Your Agent Needs a Harness, Not a Framework",
    "How GPT-5.6 fuses frontier intelligence with frontier efficiency",
    "How we contain Claude across products",
    "Introducing Agent Executor, Google’s distributed Agent Runtime",
    "Building a safe, effective sandbox to enable Codex on Windows",
    "Running Codex safely at OpenAI",
    "Skill Issue: Harness Engineering for Coding Agents",
    "Harness Engineering (Martin Fowler)",
]


def load_catalog(path: Path = DATA_FILE) -> dict[str, Any]:
    with path.open("r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    if not isinstance(data, dict):
        raise ValueError("Catalog file must be a mapping.")
    return data


def escape_md(text: Any) -> str:
    raw = str(text)
    return raw.replace("|", "\\|").replace("\n", " ").strip()


def github_ratio(entries: list[dict[str, Any]]) -> tuple[int, int, float]:
    total = len(entries)
    gh = sum(1 for e in entries if "github.com/" in str(e.get("repo_url", "")).lower())
    ratio = (gh / total * 100.0) if total else 0.0
    return gh, total, ratio


def sorted_entries(
    entries: list[dict[str, Any]], categories: list[dict[str, str]]
) -> OrderedDict[str, list[dict[str, Any]]]:
    order = [c["name_en"] for c in categories]
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for entry in entries:
        grouped[entry["category"]].append(entry)

    output: OrderedDict[str, list[dict[str, Any]]] = OrderedDict()
    for category in order:
        rows = grouped.get(category, [])
        rows.sort(key=lambda x: (-int(x.get("stars_snapshot", 0)), x.get("name", "").lower()))
        output[category] = rows
    return output


def featured_readings(entries: list[dict[str, Any]], limit: int = 10) -> list[dict[str, Any]]:
    priority = {name.lower(): idx for idx, name in enumerate(FEATURED_READING_NAMES)}
    candidates = [
        e
        for e in entries
        if str(e.get("category", "")) == READINGS_CATEGORY
        and "github.com/" not in str(e.get("repo_url", "")).lower()
    ]
    candidates.sort(key=lambda e: (priority.get(str(e.get("name", "")).lower(), 999), str(e.get("name", "")).lower()))
    return candidates[:limit]


def row_link(url: str) -> str:
    label = "GitHub" if "github.com/" in url.lower() else "Reference"
    return f"[{label}]({url})"


def star_badge(url: str, stars: Any) -> str:
    if "github.com/" not in url.lower():
        return "-"
    try:
        value = int(stars)
    except Exception:
        return "-"
    if value <= 0:
        return "-"
    return f"[![star](https://img.shields.io/badge/star-{value}-f4b400?style=flat-square)]({url})"


def render_readmes(catalog: dict[str, Any]) -> tuple[str, str]:
    categories: list[dict[str, str]] = catalog["categories"]
    entries: list[dict[str, Any]] = catalog["entries"]
    by_category = sorted_entries(entries, categories)
    gh_count, total_count, ratio = github_ratio(entries)
    project_entries = [e for e in entries if e.get("category") != READINGS_CATEGORY]
    project_gh_count, project_total_count, project_ratio = github_ratio(project_entries)
    featured = featured_readings(entries, limit=17)
    verified = catalog["catalog"]["last_verified"]

    # English README
    en: list[str] = []
    en.append("# Awesome Agent Harness")
    en.append("")
    en.append(
        "A curated, implementation-first list of **agent harness engineering** resources, with GitHub projects as the primary focus."
    )
    en.append("")
    en.append(f"- Total entries: **{total_count}**")
    en.append(f"- GitHub entries: **{gh_count} ({ratio:.1f}%)**")
    en.append(
        f"- GitHub in project categories (excluding readings): **{project_gh_count}/{project_total_count} ({project_ratio:.1f}%)**"
    )
    en.append(f"- Categories: **{len(categories)}**")
    en.append(f"- Last verified: **{verified}**")
    en.append("- Language: [English](./README.md) | [中文](./README_zh.md)")
    en.append("")
    en.append("<a id=\"featured-harness-blogs\"></a>")
    en.append("## Featured Harness Blogs")
    en.append("")
    for e in featured:
        en.append(f"- [{e['name']}]({e['repo_url']}): {e['summary_en']}")
    en.append("")
    en.append("## Contents")
    en.append("")
    en.append("- [Category Overview](#category-overview)")
    en.append("- [Featured Harness Blogs](#featured-harness-blogs)")
    en.append("- [Catalog](#catalog)")
    for c in categories:
        en.append(f"  - [{c['name_en']}](#{c['anchor']})")
    en.append("- [Maintenance Notes](#maintenance-notes)")
    en.append("- [Citation](#citation)")
    en.append("")
    en.append("## Category Overview")
    en.append("")
    en.append("| Category | Entries |")
    en.append("| --- | ---: |")
    for c in categories:
        en.append(f"| {c['name_en']} | {len(by_category[c['name_en']])} |")
    en.append("")
    en.append("## Catalog")
    en.append("")
    en.append("Notes:")
    en.append("- `Stars` are rendered as badges from snapshot values.")
    en.append("- Repository update dates are tracked in `data/projects.yaml` and validation reports.")
    en.append("- Entries are sorted by stars (descending) within each category.")
    en.append("")
    for c in categories:
        cname = c["name_en"]
        en.append(f"<a id=\"{c['anchor']}\"></a>")
        en.append(f"### {cname}")
        en.append("")
        en.append("| Project | Link | Stars | Tags | Summary |")
        en.append("| --- | --- | --- | --- | --- |")
        for e in by_category[cname]:
            tags = ", ".join(e.get("tags", []))
            url = str(e["repo_url"])
            en.append(
                "| "
                + " | ".join(
                    [
                        escape_md(e["name"]),
                        row_link(url),
                        star_badge(url, e.get("stars_snapshot", 0)),
                        escape_md(tags),
                        escape_md(e["summary_en"]),
                    ]
                )
                + " |"
            )
        en.append("")
    en.append("## Maintenance Notes")
    en.append("")
    en.append("- Source of truth: `data/projects.yaml`")
    en.append("- Regenerate README files: `python3 scripts/render_readme.py`")
    en.append("- Verify catalog and links: `python3 scripts/verify_catalog.py`")
    en.append("")
    en.append("## Citation")
    en.append("")
    en.append("```bibtex")
    en.extend(AGENT_HARNESS_CITATION)
    en.append("```")
    en.append("")

    # Chinese README
    zh: list[str] = []
    zh.append("# Awesome Agent Harness")
    zh.append("")
    zh.append("一个面向 **Agent Harness Engineering** 的工程实践清单，优先收录可直接落地的 GitHub 项目。")
    zh.append("")
    zh.append(f"- 当前条目数: **{total_count}**")
    zh.append(f"- GitHub 条目: **{gh_count} ({ratio:.1f}%)**")
    zh.append(
        f"- 项目分类 GitHub 占比（不含阅读类）: **{project_gh_count}/{project_total_count} ({project_ratio:.1f}%)**"
    )
    zh.append(f"- 分类数量: **{len(categories)}**")
    zh.append(f"- 最近核对日期: **{verified}**")
    zh.append("- 语言: [English](./README.md) | [中文](./README_zh.md)")
    zh.append("")
    zh.append("<a id=\"featured-harness-blogs\"></a>")
    zh.append("## 精选 Harness 博客")
    zh.append("")
    for e in featured:
        zh.append(f"- [{e['name']}]({e['repo_url']}): {e['summary_zh']}")
    zh.append("")
    zh.append("## 目录")
    zh.append("")
    zh.append("- [分类总览](#分类总览)")
    zh.append("- [精选 Harness 博客](#featured-harness-blogs)")
    zh.append("- [项目清单](#项目清单)")
    for c in categories:
        zh.append(f"  - [{c['name_en']}](#{c['anchor']})")
    zh.append("- [维护说明](#维护说明)")
    zh.append("- [引用](#引用)")
    zh.append("")
    zh.append("## 分类总览")
    zh.append("")
    zh.append("| 分类 | 条目数 |")
    zh.append("| --- | ---: |")
    for c in categories:
        zh.append(f"| {c['name_en']} | {len(by_category[c['name_en']])} |")
    zh.append("")
    zh.append("## 项目清单")
    zh.append("")
    zh.append("说明：")
    zh.append("- `Stars` 使用徽章展示（来自快照值）。")
    zh.append("- 仓库更新时间统一记录在 `data/projects.yaml` 与验证报告中。")
    zh.append("- 每个分类内按 Stars 降序排序。")
    zh.append("")
    for c in categories:
        cname = c["name_en"]
        zh.append(f"<a id=\"{c['anchor']}\"></a>")
        zh.append(f"### {cname}")
        zh.append("")
        zh.append("| 项目 | 链接 | Stars | 标签 | 简介 |")
        zh.append("| --- | --- | --- | --- | --- |")
        for e in by_category[cname]:
            tags = ", ".join(e.get("tags", []))
            url = str(e["repo_url"])
            zh.append(
                "| "
                + " | ".join(
                    [
                        escape_md(e["name"]),
                        row_link(url),
                        star_badge(url, e.get("stars_snapshot", 0)),
                        escape_md(tags),
                        escape_md(e["summary_zh"]),
                    ]
                )
                + " |"
            )
        zh.append("")
    zh.append("## 维护说明")
    zh.append("")
    zh.append("- 单一数据源: `data/projects.yaml`")
    zh.append("- 重新生成 README: `python3 scripts/render_readme.py`")
    zh.append("- 校验条目与链接: `python3 scripts/verify_catalog.py`")
    zh.append("")
    zh.append("## 引用")
    zh.append("")
    zh.append("```bibtex")
    zh.extend(AGENT_HARNESS_CITATION)
    zh.append("```")
    zh.append("")

    return "\n".join(en), "\n".join(zh)


def validate_contract(catalog: dict[str, Any]) -> None:
    if "catalog" not in catalog or "categories" not in catalog or "entries" not in catalog:
        raise ValueError("Catalog must contain: catalog, categories, entries")
    for entry in catalog["entries"]:
        missing = [f for f in REQUIRED_ENTRY_FIELDS if f not in entry]
        if missing:
            raise ValueError(f"Entry `{entry.get('name', '<unknown>')}` missing fields: {missing}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Render README.md and README_zh.md from data/projects.yaml")
    parser.add_argument("--check", action="store_true", help="Only check whether README files are up to date")
    args = parser.parse_args()

    catalog = load_catalog(DATA_FILE)
    validate_contract(catalog)
    en, zh = render_readmes(catalog)

    if args.check:
        current_en = README_EN.read_text(encoding="utf-8") if README_EN.exists() else ""
        current_zh = README_ZH.read_text(encoding="utf-8") if README_ZH.exists() else ""
        if current_en != en or current_zh != zh:
            raise SystemExit("README files are not up-to-date. Run: python3 scripts/render_readme.py")
        print("README files are up-to-date.")
        return

    README_EN.write_text(en, encoding="utf-8")
    README_ZH.write_text(zh, encoding="utf-8")
    print(f"Rendered: {README_EN}")
    print(f"Rendered: {README_ZH}")


if __name__ == "__main__":
    main()

---
id: 20260513-anthropic-financial-services
title: Anthropic Financial Services
type: reference
category: ai-financial-agents
status: active
created: 2026-05-13
updated: 2026-05-13
tags:
  - domain/financial-services
  - domain/investing
  - tool/claude
  - framework/agent
  - framework/mcp
aliases:
  - Claude for Financial Services
  - financial-services
  - Anthropic FSI plugins
source: external
sources:
  - url: https://github.com/anthropics/financial-services
    captured: 2026-05-13
  - url: https://www.anthropic.com/news/finance-agents
    captured: 2026-05-13
provenance:
  - repo: https://github.com/anthropics/financial-services
    commit: 853f755a61f7bbb045c681327f46b354419030a1
    captured: 2026-05-13
    method: shallow sparse clone to local temp directory for read-only inspection
  - files_read:
      - README.md
      - CLAUDE.md
      - .claude-plugin/marketplace.json
      - plugins/vertical-plugins/financial-analysis/.mcp.json
      - plugins/vertical-plugins/financial-analysis/skills/comps-analysis/SKILL.md
      - plugins/vertical-plugins/financial-analysis/skills/xlsx-author/SKILL.md
      - plugins/agent-plugins/pitch-agent/agents/pitch-agent.md
      - plugins/agent-plugins/market-researcher/agents/market-researcher.md
      - plugins/agent-plugins/gl-reconciler/agents/gl-reconciler.md
      - managed-agent-cookbooks/README.md
      - managed-agent-cookbooks/pitch-agent/agent.yaml
      - managed-agent-cookbooks/pitch-agent/README.md
      - managed-agent-cookbooks/gl-reconciler/agent.yaml
confidence:
  base: high
  notes: README, CLAUDE.md, marketplace manifest, representative agent prompts, skills, MCP config, and Managed Agent cookbooks were read from commit 853f755. Availability of external MCP providers and current marketplace naming should be verified before use.
lifecycle:
  stage: active
  review: quarterly
summary: Anthropic reference repository for Claude financial-services agents, vertical skills, MCP data connectors, and Managed Agent deployment templates.
links:
  synthesis:
    - synthesis/financial-services-agent-architecture
  concepts:
    - concepts/stock-recommendation-framework
    - concepts/a-share-sentiment-market
  projects:
    - projects/proj2-stock-recommendation
---

# Anthropic Financial Services

## Source

- Repository: https://github.com/anthropics/financial-services
- Public announcement: https://www.anthropic.com/news/finance-agents
- Local verification commit: `853f755a61f7bbb045c681327f46b354419030a1`
- License: Apache License 2.0

The repository title is **Claude for Financial Services**. It provides reference agents, skills, and data connectors for common financial-services workflows: investment banking, equity research, private equity, wealth management, fund administration, and operations.

The README states that these workflows are available **two ways from one source**:

1. Install as Claude Cowork / Claude Code plugins.
2. Deploy through the Claude Managed Agents API behind a firm's workflow engine.

## Key points

### Boundary and compliance posture

The repo explicitly says it is not investment, legal, tax, or accounting advice. The agents draft analyst work product for review by qualified professionals. They do not make investment recommendations, execute transactions, bind risk, post to a ledger, approve onboarding, publish research, or distribute external communications. Outputs are staged for human sign-off.

This boundary is important for any reuse in [[projects/proj2-stock-recommendation]]: decisive analysis can be produced, but execution and regulated approvals stay outside the agent.

### Repository structure

```text
plugins/
  agent-plugins/               # named workflow agents; self-contained plugins
  vertical-plugins/            # source skills, slash commands, and MCP connectors by vertical
  partner-built/               # partner plugins such as LSEG and S&P Global
managed-agent-cookbooks/       # Claude Managed Agent templates, one directory per named agent
claude-for-msft-365-install/   # Microsoft 365 add-in provisioning tooling
scripts/                       # deploy, lint, validate, orchestrate, sync skills
```

Important implementation files:

- `plugins/agent-plugins/<slug>/.claude-plugin/plugin.json` — plugin metadata.
- `plugins/agent-plugins/<slug>/agents/<slug>.md` — canonical system prompt for a named agent.
- `plugins/agent-plugins/<slug>/skills/` — bundled skill copies for self-contained install.
- `plugins/vertical-plugins/<vertical>/skills/` — source of truth for reusable skills.
- `plugins/vertical-plugins/<vertical>/commands/` — slash commands.
- `plugins/vertical-plugins/financial-analysis/.mcp.json` — centralized MCP connector config.
- `managed-agent-cookbooks/<slug>/agent.yaml` — Managed Agent manifest referencing the same prompt and skills.
- `managed-agent-cookbooks/<slug>/subagents/*.yaml` — depth-1 leaf workers.
- `managed-agent-cookbooks/<slug>/steering-examples.json` — example steering events.

### Named agents

| Function | Agent | Output |
|---|---|---|
| Coverage and advisory | `pitch-agent` | Comps, precedents, LBO, valuation workbook, branded pitch deck |
| Coverage and advisory | `meeting-prep-agent` | Client meeting briefing pack |
| Research and modeling | `market-researcher` | Sector/theme overview, landscape, peer comps, ideas shortlist |
| Research and modeling | `earnings-reviewer` | Earnings call and filings to model update and note draft |
| Research and modeling | `model-builder` | DCF, LBO, 3-statement, comps in Excel/file form |
| Fund admin and finance ops | `valuation-reviewer` | GP package ingestion, valuation template, LP reporting staging |
| Fund admin and finance ops | `gl-reconciler` | Break list, root-cause trace, exception report |
| Fund admin and finance ops | `month-end-closer` | Accruals, roll-forwards, variance commentary |
| Fund admin and finance ops | `statement-auditor` | LP statement audit before distribution |
| Operations and onboarding | `kyc-screener` | Onboarding doc parsing, rules-grid evaluation, gap flags |

### Vertical plugins

The repo separates workflow agents from reusable vertical capabilities.

| Plugin | Adds |
|---|---|
| `financial-analysis` | Core modeling skills: comps, DCF, LBO, 3-statement, deck QC, Excel audit, artifact writers, and all data connectors |
| `investment-banking` | CIMs, teasers, buyer lists, process letters, merger models, deal tracking |
| `equity-research` | Earnings notes, initiations, model updates, thesis/catalyst tracking, idea generation |
| `private-equity` | Sourcing, screening, diligence, IC memos, portfolio monitoring, value-creation plans |
| `wealth-management` | Client reviews, financial plans, portfolio rebalancing, reporting, tax-loss harvesting |
| `fund-admin` | GL reconciliation, break tracing, accruals, roll-forwards, NAV tie-out |
| `operations` | KYC parsing and rules-grid evaluation |
| `lseg` | Partner plugin for LSEG financial data and analytics |
| `sp-global` | Partner plugin for S&P Global / Capital IQ workflows |

### MCP integrations

`financial-analysis/.mcp.json` centralizes data connectors. The verified provider list includes Daloopa, Morningstar, S&P Global, FactSet, Moody's, MT Newswires, Aiera, LSEG, PitchBook, Chronograph, and Egnyte.

The README notes that MCP access may require a provider subscription or API key.

### Setup and deployment pattern

Claude Code plugin installation from README:

```bash
claude plugin marketplace add anthropics/claude-for-financial-services
claude plugin install financial-analysis@claude-for-financial-services
claude plugin install pitch-agent@claude-for-financial-services
claude plugin install gl-reconciler@claude-for-financial-services
claude plugin install market-researcher@claude-for-financial-services
claude plugin install investment-banking@claude-for-financial-services
claude plugin install equity-research@claude-for-financial-services
```

The current GitHub repository is `anthropics/financial-services`, while the marketplace manifest name and README commands use `claude-for-financial-services`. Verify the current marketplace path before installing.

Managed Agent deployment pattern:

```bash
export ANTHROPIC_API_KEY=...
scripts/deploy-managed-agent.sh gl-reconciler
```

Managed Agent cookbooks reference the same canonical agent prompt and skills as the plugin version, then add headless execution instructions such as writing artifacts to `./out/` instead of assuming an open Office document.

## Useful implementation patterns

### One source, two wrappers

The same agent prompt and skills serve both interactive plugin use and headless Managed Agent deployment. This avoids divergent logic between local analyst workflows and production orchestration.

### Skills are authored once, then bundled

Source skills live under `plugins/vertical-plugins/<vertical>/skills/`. Agent plugins bundle synced copies under `plugins/agent-plugins/<slug>/skills/` so that each named agent is self-contained. `scripts/sync-agent-skills.py` propagates changes from vertical sources to bundled copies.

### Validation is file-reference focused

`scripts/check.py` validates JSON/YAML manifests, agent prompt frontmatter, `system.file`, `skills.path`, `callable_agents.manifest`, marketplace source paths, required cookbook files, and bundled-skill drift from vertical sources.

### Data source hierarchy matters

`comps-analysis` says to prefer institutional MCP sources such as S&P Kensho, FactSet, or Daloopa when available, and not to use web search as the primary source for financial/trading information. The skill also requires source comments or assumption explanations for hardcoded inputs.

### Artifact contracts are explicit

`xlsx-author` requires writing output to `./out/<name>.xlsx` in headless mode and returning the relative path so an orchestration layer can collect it. Spreadsheet conventions mirror `audit-xls`: blue hardcoded inputs, black formulas, green links, no hardcodes in calculation cells, named ranges, balance checks, and a Checks tab.

### Multi-agent safety uses tool isolation

Managed Agent cookbooks split work into an orchestrator and depth-1 leaf workers. `managed-agent-cookbooks/README.md` notes that the bold leaf worker is the only one with `Write`. Examples:

- `pitch-agent`: `researcher`, `modeler`, `deck-writer`; only `deck-writer` writes.
- `gl-reconciler`: orchestrator has read-only GL/subledger MCP access; resolver writes the final exception report.

### External documents are untrusted data

`market-researcher` instructs the agent to treat third-party reports and issuer materials as data to extract, not as instructions to follow. `gl-reconciler` isolates custodian/counterparty statements from MCP and write access.

## My interpretation

This repo is less an alpha model and more an **operating system for analyst work products**: it turns financial workflows into reusable prompts, skills, connectors, artifact contracts, and human approval checkpoints.

For this project, the most reusable ideas are:

- split stock-research work into specialist steps rather than one monolithic prompt;
- treat data provenance and citation as first-class outputs;
- distinguish analysis artifacts from trading or publishing authority;
- make generated Excel/PowerPoint/report artifacts auditable;
- use a single source of truth for reusable skills, then wrap them for different runtime surfaces.

## Reliability / caveats

- The repo is a reference implementation, not a production-ready financial-advice system.
- MCP provider access may require subscriptions, API keys, and firm-specific compliance review.
- The examples are mostly institutional US/IB/PE workflows; A-share short-term recommendations need different data sources and market microstructure logic.
- The repository URL and marketplace name differ: GitHub is `anthropics/financial-services`; marketplace manifest name is `claude-for-financial-services`.
- `callable_agents` is marked as a research preview with one delegation level in the Managed Agent cookbook.

## Links

- Related synthesis: [[synthesis/financial-services-agent-architecture]]
- Related concepts:
  - [[concepts/stock-recommendation-framework]]
  - [[concepts/a-share-sentiment-market]]
- Related project: [[projects/proj2-stock-recommendation]]

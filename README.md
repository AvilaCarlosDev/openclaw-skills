# OpenClaw Skills — curated collection

> Skills for [OpenClaw](https://openclaw.ai), gathered, tested and organized in one place. [Leer en espanol](README.es.md).

**This repository is a curation, not authorship**, for most of the skills. Most of them were written by other people and published on [ClawHub / clawic.com](https://clawic.com). What this repo adds is selection, real-use testing, category organization and bilingual documentation. Each skill keeps its original frontmatter with its `homepage` and authorship.

If a skill is useful to you, go to its original page and support whoever wrote it.

---

## Community skills

Published on ClawHub by their respective authors. Only selected and documented here.

| Skill | What it does | Original source |
|---|---|---|
| `arch-improver` | Detects coupling and layer violations in the codebase | [Architecture Improver](https://clawic.com/skills/arch-improver) |
| `chat-to-prd` | Converts the current conversation into a PRD and opens it as an issue | [Chat to PRD](https://clawic.com/skills/chat-to-prd) |
| `code-context` | Understands unfamiliar code in the context of the whole system | [Code Context](https://clawic.com/skills/code-context) |
| `compressed-mode` | Compressed response mode, ~75% fewer tokens | [Compressed Mode](https://clawic.com/skills/compressed-mode) |
| `content-marketing` | Editorial calendars, funnel and content repurposing | [Content Marketing](https://clawic.com/skills/content-marketing) |
| `cybersecurity` | Security triage, threat modeling and incident reporting | [Cybersecurity](https://clawic.com/skills/cybersecurity) |
| `debug-diagnose` | Disciplined loop: reproduce, minimize, hypothesize, verify | [Debug Diagnose](https://clawic.com/skills/debug-diagnose) |
| `git-guardrails` | Hooks that block push --force, reset --hard and clean | [Git Guardrails](https://clawic.com/skills/git-guardrails) |
| `graphic-design` | Prototypes, design systems and UI/UX work | [Graphic Design Pro](https://clawic.com/skills/graphic-design-pro) |
| `grill-me` | Relentless interview about a plan until every decision is closed | [Grill Me](https://clawic.com/skills/grill-me) |
| `grill-with-docs` | Same as Grill Me, checked against the domain model | [Grill With Docs](https://clawic.com/skills/grill-with-docs) |
| `issue-triage` | Issue triage with a state machine, labels and routing | [Issue Triage](https://clawic.com/skills/issue-triage) |
| `plan-to-issues` | Splits a plan or PRD into independent issues by vertical slice | [Plan to Issues](https://clawic.com/skills/plan-to-issues) |
| `programming` | General development, debugging and code review skill | [Programming](https://clawic.com/skills/programming) |
| `quick-prototype` | Throwaway prototypes to explore design | [Quick Prototype](https://clawic.com/skills/quick-prototype) |
| `refero-styles` | Extracts color, typography and spacing from a website | [Refero Styles](https://clawic.com/skills/refero-styles) |
| `seo` | Site audit, copywriting and competitor analysis | [SEO](https://clawic.com/skills/seo) |
| `tdd-helper` | Red-green-refactor cycle by vertical slice | [TDD Helper](https://clawic.com/skills/tdd-helper) |
| `ai-meeting-notes` | Turns meeting notes into action items | [jeffjhunter.com](https://jeffjhunter.com) |
| `meeting-notes` | Structures meeting notes | Published on ClawHub |
| `safe-web` | Web browsing with prompt-injection protection | Published on ClawHub |

### Language and infrastructure skills, by [ivangdavila](https://clawhub.ai/ivangdavila)

Nine detailed "use when X breaks" skills from the same author, added because they match this repo's stack (Next.js/TypeScript/React) and its focus on avoiding real, specific failure modes rather than generic tutorials.

| Skill | What it does | Original source |
|---|---|---|
| `typescript` | Type errors, narrowing, generics, tsconfig, declaration files | [TypeScript](https://clawic.com/skills/typescript) |
| `nextjs` | App Router, server components, caching, Server Actions, deploy | [NextJS](https://clawic.com/skills/nextjs) |
| `react` | Hooks, state, re-renders, hydration mismatches, testing | [React](https://clawic.com/skills/react) |
| `sql` | Slow queries, JOIN bugs, migrations, indexing, schema design | [SQL](https://clawic.com/skills/sql) |
| `git` | Conflicts, rebases, lost history, hooks, worktrees | [Git](https://clawic.com/skills/git) |
| `nginx` | Reverse proxy, SSL termination, 502/504s, WebSockets through proxy | [Nginx](https://clawic.com/skills/nginx) |
| `devops` | CI/CD pipelines, rollout strategy, on-call, SLOs, DORA metrics | [DevOps](https://clawic.com/skills/devops) |
| `terraform` | HCL, plan/apply failures, state surgery, drift, provider pinning | [Terraform](https://clawic.com/skills/terraform) |
| `playwright` | Flaky tests, locators, traces, CI runs, MCP browser control | [Playwright](https://clawic.com/skills/playwright) |

---

## Own skills

Written for this repository:

| Skill | What it does |
|---|---|
| `safe_search` | Web search with prompt-injection protection |
| `safe_fetch` | Page fetching with prompt-injection protection |

### Spanish-original skills

[Carlos Avila](https://github.com/AvilaCarlosDev) also writes original skills directly in Spanish, kept under `skills-es/`. They are not translations of the table above — independent work, documented in [README.es.md](README.es.md#skills-propias-en-espanol).

| Skill | Command | What it does |
|---|---|---|
| [`skills-es/engineering/diagnostico`](skills-es/engineering/diagnostico/SKILL.md) | `/diagnostico` | Structured bug debugging: reproduce, minimize, hypothesize, instrument, fix, regression-check |
| [`skills-es/engineering/tdd`](skills-es/engineering/tdd/SKILL.md) | `/tdd` | Test-driven development, Red-Green-Refactor cycle |
| [`skills-es/github/contribucion`](skills-es/github/contribucion/SKILL.md) | `/contribucion` | Preparing open-source contributions: finding an issue, fixing, testing, PR |
| [`skills-es/landings/diseno-profesional`](skills-es/landings/diseno-profesional/SKILL.md) | `/diseno-profesional` | Applying Refero.design principles to pages and components |
| [`skills-es/ventas/pitch`](skills-es/ventas/pitch/SKILL.md) | `/pitch` | Personalized sales emails for landing pages, without sounding like spam |

---

## How to use a skill

```bash
# from ClawHub, the recommended way, keeps the skill up to date
clawhub install <skill-name>

# or by copying the SKILL.md into your workspace
cp <name>/SKILL.md ~/.openclaw/workspace/skills/<name>/
# Spanish skills use the same relative path: skills-es/<category>/<name>/SKILL.md
```

Skills activate on their own when a task matches their description, or you can invoke them with `/use <name> <task>`.

---

## License and credits

Each community-section skill belongs to whoever wrote it and follows the terms of its original ClawHub publication. **This repository does not claim authorship over them.**

The `skills-es/` skills, plus the curation and documentation, are by [Carlos Avila](https://github.com/AvilaCarlosDev), under MIT.

If you authored a skill included here and want it removed or credited differently, [open an issue](https://github.com/AvilaCarlosDev/openclaw-skills/issues) and it gets resolved right away.

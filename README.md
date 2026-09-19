# OpenClaw Skills — curated collection

> Skills for [OpenClaw](https://openclaw.ai), gathered, tested and organized in one place. [Leer en español](README.es.md).

This repository has **three kinds of skills, and each one is labelled for what it really is**:

1. **Community skills**: files published on [ClawHub](https://clawhub.ai) by other authors, copied here byte for byte. ClawHub publishes every skill under [MIT-0](https://github.com/openclaw/clawhub/blob/main/docs/skill-format.md#license), which allows use, modification and redistribution, including commercial use, without requiring attribution. They are credited anyway, with a link to the author.
2. **Derived skills**: a ClawHub skill that was modified here. The modification is stated.
3. **Own skills**: written for this repository. Some adapt the *concept* of a skill from [mattpocock/skills](https://github.com/mattpocock/skills) (MIT); the texts were rewritten and translated, no file is copied, and each one says so.

Where every skill comes from lives in [`procedencia.json`](procedencia.json), and CI checks it (see [Provenance and verification](#provenance-and-verification)). Verified on 2026-09-19.

If a skill is useful to you, go to its author's page and support them.

---

## Community skills (copied unchanged from ClawHub)

### Various authors

| Skill | What it does | Author | Original | Version |
|---|---|---|---|---|
| `ai-meeting-notes` | Turns meeting notes into action items | [jeffjhunter](https://clawhub.ai/jeffjhunter) | [ai-meeting-notes](https://clawhub.ai/jeffjhunter/skills/ai-meeting-notes) | 1.0.3 |
| `meeting-notes` | Structures meeting notes | [tinadu-ai](https://clawhub.ai/tinadu-ai) | [meeting-notes](https://clawhub.ai/tinadu-ai/skills/meeting-notes) | 1.0.1 |
| `safe-web` | Web browsing with prompt-injection protection | [adamnaghs](https://clawhub.ai/adamnaghs) | [safe-web](https://clawhub.ai/adamnaghs/skills/safe-web) | 1.0.8 |

### Language and infrastructure skills, by [ivangdavila](https://clawhub.ai/ivangdavila)

| Skill | What it does | Author | Original | Version |
|---|---|---|---|---|
| `content-marketing` | Editorial calendars, funnel and content repurposing | [ivangdavila](https://clawhub.ai/ivangdavila) | [content-marketing](https://clawhub.ai/ivangdavila/skills/content-marketing) | 1.0.0 |
| `cybersecurity` | Security triage, threat modeling and incident reporting | [ivangdavila](https://clawhub.ai/ivangdavila) | [cybersecurity](https://clawhub.ai/ivangdavila/skills/cybersecurity) | 1.0.0 |
| `devops` | CI/CD pipelines, rollout strategy, on-call, SLOs, DORA metrics | [ivangdavila](https://clawhub.ai/ivangdavila) | [devops](https://clawhub.ai/ivangdavila/skills/devops) | 1.0.2 |
| `git` | Conflicts, rebases, lost history, hooks, worktrees | [ivangdavila](https://clawhub.ai/ivangdavila) | [git](https://clawhub.ai/ivangdavila/skills/git) | 1.0.12 |
| `nextjs` | App Router, server components, caching, Server Actions, deploy | [ivangdavila](https://clawhub.ai/ivangdavila) | [nextjs](https://clawhub.ai/ivangdavila/skills/nextjs) | 1.1.2 |
| `nginx` | Reverse proxy, SSL termination, 502/504s, WebSockets through proxy | [ivangdavila](https://clawhub.ai/ivangdavila) | [nginx](https://clawhub.ai/ivangdavila/skills/nginx) | 1.0.5 |
| `playwright` | Flaky tests, locators, traces, CI runs, MCP browser control | [ivangdavila](https://clawhub.ai/ivangdavila) | [playwright](https://clawhub.ai/ivangdavila/skills/playwright) | 1.0.4 |
| `react` | Hooks, state, re-renders, hydration mismatches, testing | [ivangdavila](https://clawhub.ai/ivangdavila) | [react](https://clawhub.ai/ivangdavila/skills/react) | 1.0.7 |
| `seo` | Site audit, copywriting and competitor analysis | [ivangdavila](https://clawhub.ai/ivangdavila) | [seo](https://clawhub.ai/ivangdavila/skills/seo) | 1.0.3 |
| `sql` | Slow queries, JOIN bugs, migrations, indexing, schema design | [ivangdavila](https://clawhub.ai/ivangdavila) | [sql](https://clawhub.ai/ivangdavila/skills/sql) | 1.0.4 |
| `terraform` | HCL, plan/apply failures, state surgery, drift, provider pinning | [ivangdavila](https://clawhub.ai/ivangdavila) | [terraform](https://clawhub.ai/ivangdavila/skills/terraform) | 1.0.4 |
| `typescript` | Type errors, narrowing, generics, tsconfig, declaration files | [ivangdavila](https://clawhub.ai/ivangdavila) | [typescript](https://clawhub.ai/ivangdavila/skills/typescript) | 1.0.5 |

---

## Derived skills (modified here)

| Skill | What it does | Based on | What changed |
|---|---|---|---|
| `graphic-design` | Prototypes, design systems and UI/UX work | [ivangdavila/graphic-design@1.0.0](https://clawhub.ai/ivangdavila/skills/graphic-design) | Rewritten as v2.0.0 with Claude Design capabilities. |
| `programming` | General development, debugging and code review skill | [leowing/programming@1.0.0](https://clawhub.ai/leowing/skills/programming) | `SKILL.md` rewritten in Spanish; every other file is the original. |

---

## Own skills

Written for this repository by [Carlos Avila](https://github.com/AvilaCarlosDev), under MIT. They do **not** come from ClawHub. Where a concept matches a skill in another public repository, it is credited.

| Skill | What it does | Concept |
|---|---|---|
| `arch-improver` | Detects coupling and layer violations in the codebase | Concept adapted from [mattpocock/skills · improve-codebase-architecture](https://github.com/mattpocock/skills/tree/main/skills/engineering/improve-codebase-architecture) (MIT) |
| `chat-to-prd` | Converts the current conversation into a PRD and opens it as an issue | Concept adapted from [mattpocock/skills · to-spec](https://github.com/mattpocock/skills/tree/main/skills/engineering/to-spec) (MIT) |
| `code-context` | Understands unfamiliar code in the context of the whole system | — |
| `compressed-mode` | Compressed response mode, ~75% fewer tokens | — |
| `debug-diagnose` | Disciplined loop: reproduce, minimize, hypothesize, verify | Concept adapted from [mattpocock/skills · diagnosing-bugs](https://github.com/mattpocock/skills/tree/main/skills/engineering/diagnosing-bugs) (MIT) |
| `git-guardrails` | Hooks that block push --force, reset --hard and clean | Concept adapted from [mattpocock/skills · git-guardrails-claude-code](https://github.com/mattpocock/skills/tree/main/skills/misc/git-guardrails-claude-code) (MIT) |
| `grill-me` | Relentless interview about a plan until every decision is closed | Concept adapted from [mattpocock/skills · grill-me](https://github.com/mattpocock/skills/tree/main/skills/productivity/grill-me) (MIT) |
| `grill-with-docs` | Same as Grill Me, checked against the domain model | Concept adapted from [mattpocock/skills · grill-with-docs](https://github.com/mattpocock/skills/tree/main/skills/engineering/grill-with-docs) (MIT) |
| `issue-triage` | Issue triage with a state machine, labels and routing | Concept adapted from [mattpocock/skills · triage](https://github.com/mattpocock/skills/tree/main/skills/engineering/triage) (MIT) |
| `plan-to-issues` | Splits a plan or PRD into independent issues by vertical slice | Concept adapted from [mattpocock/skills · to-tickets](https://github.com/mattpocock/skills/tree/main/skills/engineering/to-tickets) (MIT) |
| `quick-prototype` | Throwaway prototypes to explore design | Concept adapted from [mattpocock/skills · prototype](https://github.com/mattpocock/skills/tree/main/skills/engineering/prototype) (MIT) |
| `refero-styles` | Extracts color, typography and spacing from a website | Idea inspired by [Refero Styles](https://refero.design) |
| `safe_fetch` | Page fetching with prompt-injection protection | — |
| `safe_search` | Web search with prompt-injection protection | — |
| `tdd-helper` | Red-green-refactor cycle by vertical slice | Concept adapted from [mattpocock/skills · tdd](https://github.com/mattpocock/skills/tree/main/skills/engineering/tdd) (MIT) |

### Spanish-original skills

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
# from ClawHub, the recommended way for community skills, keeps them up to date
clawhub install <skill-name>

# or by copying the SKILL.md (and the rest of the folder) into your workspace
cp -r <name> ~/.openclaw/workspace/skills/
# Spanish skills use the same relative path: skills-es/<category>/<name>/
```

Skills activate on their own when a task matches their description, or you can invoke them with `/use <name> <task>`.

Some skills include scripts (`safe-web`, `programming`). Read them before running them, as with any code you did not write.

---

## Provenance and verification

`procedencia.json` records, for every skill, its type, author, version, source URL and the SHA-256 of each file taken from a third party.

```bash
python3 scripts/procedencia.py comprobar   # offline: registry, hashes, READMEs and homepages agree
python3 scripts/procedencia.py remoto      # online: compares against what ClawHub serves today
```

The first check runs on every pull request; the second runs weekly, because it depends on an external service. How the origin was established: each file was fetched from ClawHub's public API at the exact version and compared byte for byte. `_meta.json` and `.clawhub/` are generated by the registry and are excluded.

---

## License and credits

- **Community skills:** © their authors, published on ClawHub under MIT-0. Copied unchanged. This repository does not claim authorship over them.
- **Derived skills:** the original files keep their author's terms (MIT-0); the modifications are under MIT.
- **Own skills, curation and documentation:** © Carlos Avila, MIT (see [LICENSE](LICENSE)). Third-party notices are in [NOTICE.md](NOTICE.md).
- Developed with the support of Claude (Anthropic) as an assistant for writing and source verification; the selection and the final review are the author's.

If you authored a skill included here and want it removed or credited differently, [open an issue](https://github.com/AvilaCarlosDev/openclaw-skills/issues) and it gets resolved right away. To report a security problem, see [SECURITY.md](SECURITY.md).

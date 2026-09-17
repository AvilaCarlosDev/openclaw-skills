## Description:

Helps agents manage Git repositories, including commits, branches, merges, rebases, conflict resolution, history recovery, repository configuration, and safer handling of force pushes, secrets, hooks, worktrees, submodules, and large repositories.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ivangdavila](https://clawhub.ai/user/ivangdavila)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineering teams use this skill when an agent needs to inspect or change a Git repository, recover lost work, resolve Git errors or conflicts, prepare reviewable commits, or apply safer repository workflow practices.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide an agent through destructive Git operations or history rewrites.

Mitigation: Confirm before allowing destructive Git commands, global git config changes, force pushes, or shared-history rewrites.

Risk: Local preference memory may retain repository names, workflow preferences, or safety preferences across sessions.

Mitigation: Review or disable ~/Clawic/data/git/ preference memory when persistent local workflow data is not desired.

## Reference(s):

- [ClawHub Git skill page](https://clawhub.ai/ivangdavila/skills/git)
- [Publisher profile](https://clawhub.ai/user/ivangdavila)
- [Clawic Git skill page](https://clawic.com/skills/git)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires the git binary; supports linux, darwin, and win32; may use local preference memory under ~/Clawic/data/git/.]

## Skill Version(s):

1.0.12 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

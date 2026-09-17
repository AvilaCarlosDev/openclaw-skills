## Description:

Writes, reviews, and optimizes SQL queries; designs schemas, indexes, and constraints; plans migrations for relational databases.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ivangdavila](https://clawhub.ai/user/ivangdavila)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and database engineers use this skill for SQL query writing, review, optimization, schema design, migrations, debugging, and operations across common relational database engines.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated destructive SQL or migration guidance could affect production data if run without review.

Mitigation: Review UPDATE, DELETE, DROP, TRUNCATE, migration, backup, and restore commands before execution, and preview destructive DML with an equivalent SELECT where practical.

Risk: Debugging SQL can expose credentials, hostnames, bound parameter values, or personal data in prompts and local memory.

Mitigation: Keep credentials and connection strings in a secret store, redact sensitive query values and logs, and do not store secrets or personal data in the skill memory path.

## Reference(s):

- [ClawHub SQL skill page](https://clawhub.ai/ivangdavila/skills/sql)
- [Clawic SQL skill page](https://clawic.com/skills/sql)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown with SQL, shell command, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce database-specific SQL and operational checklists based on the selected dialect and user preferences.]

## Skill Version(s):

1.0.4 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.

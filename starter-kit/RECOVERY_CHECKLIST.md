# Project Recovery Checklist

## Before a disruption
- [ ] Keep project files in versioned storage or a separate backup.
- [ ] Record the canonical repository, branch, and last reviewed commit.
- [ ] Store credentials and recovery codes in a password manager, never in the repository.
- [ ] Document required software, integrations, permission scopes, and owner approval boundaries.
- [ ] Keep irreplaceable source files and local configuration backed up separately.

## Recovery
1. Secure the account through the provider's official recovery process; revoke lost or exposed sessions.
2. Restore the project from its canonical repository or an official archive.
3. Inspect the last reviewed commit and current status; do not assume the newest work is approved.
4. Reinstall required tools from documented official sources and record versions.
5. Reconnect integrations deliberately, starting read-only where possible.
6. Open key files and run documented checks, comparing results with the last evidence record.
7. Resume only documented safe tasks; ask the owner before external or irreversible actions.

## Recovery record
- Date and reason:
- Restored source and version:
- Files and tools restored:
- Checks run and results:
- Access rotated (never record secrets):
- Still missing or unverified:
- Owner decision needed:
- Next bounded action:

A repository alone does not back up credentials, external data, local configuration, or every dependency.

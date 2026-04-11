# Security policy

## Supported versions

Security-sensitive fixes are applied on the **default branch** (usually `main`). Tags follow [`VERSION`](VERSION) / [`CHANGELOG.md`](CHANGELOG.md).

## Reporting a vulnerability

**Do not** open a public issue for an undisclosed security problem.

- Prefer **[GitHub Security Advisories](https://docs.github.com/en/code-security/security-advisories)** (repository **Security** tab → **Report a vulnerability**) if the feature is enabled for this repo.
- Otherwise contact the maintainers with a **private** channel they publish in the repository description or org profile.

Include: affected paths or docs, reproduction steps, and impact assessment if you can. We will acknowledge receipt and coordinate disclosure.

## Scope

This repository is **documentation, Markdown doctrine, and shell helpers** — not a network service. Reports about **consuming projects** (your app’s secrets, runtime, dependencies) belong in those projects’ own security policies.

## Secrets in forks

Do not commit API keys, tokens, or internal URLs. See [`.gitignore`](.gitignore) and [`CONTRIBUTING.md`](CONTRIBUTING.md) (public repository checklist).

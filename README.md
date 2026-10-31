# Python Subscription Billing-Text Starter

A small Python prototype for subscription descriptions and TON payment links.

**Status: development starter / prototype.** Read the scope before integrating.

## Included

- Formats example subscription tiers and billing text.
- Validates TON amounts and encodes payment memos.

## Scope and limitations

- No AI classification, ticket storage, SLA tracking, messaging service or hosted support.
- Example plans do not activate a service. Do not send payments to test the code.
- Runtime settings live in CONFIG; config.example.json is a reference only.

## Quick start

Python 3.10+; run from the repository directory.

```sh
python support_bot.py
```

## Validation

```sh
python -m unittest discover -s tests -v
```

Unit tests cover billing text, amount validation and URL encoding; they do not test an AI support system.

## Repository map

- `support_bot.py` — implementation.
- `tests/` — current checks and regression tests.
- [CHANGELOG.md](CHANGELOG.md) — changes and verification limits.
- [CONTRIBUTING.md](CONTRIBUTING.md) — issue and change guidelines.

## Downloads and usage terms

[Repository releases](https://github.com/Kirilka4345/ai-customer-support-ticket-bot/releases) contain historical snapshots; use the current source for the documented fixes.
No LICENSE file is present. Earlier MIT badges and commercial-license claims did not establish usable license terms. License terms require clarification before redistribution.

## Questions

For reproducible technical issues, use [GitHub Issues](https://github.com/Kirilka4345/ai-customer-support-ticket-bot/issues). Include the commit, runtime version, expected result and minimal reproduction. Never include tokens, cookies or customer data.

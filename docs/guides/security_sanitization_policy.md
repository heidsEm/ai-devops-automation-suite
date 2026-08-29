# Security & Privacy Sanitization Policy

This repository adheres to strict security standards to ensure zero confidential data or PII is exposed.

## Standard Sanitization Rules

1. **API Keys & Credentials:** All live tokens (`sk-`, `ghp_`, `sl.`, `xi-api-key`) are replaced with safe uppercase placeholders (`YOUR_API_KEY`, `YOUR_GITHUB_TOKEN`).
2. **PII Anonymization:** All personal names, email addresses, phone numbers, and office locations are converted to generic roles (`DevOps Engineer`, `user@example.com`, `YOUR_PHONE_NUMBER`).
3. **Environment Files:** `.env` files and local credential caches are excluded via `.gitignore`.

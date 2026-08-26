# AI & DevOps Automation Suite (2026)

A curated collection of production-ready Python automations, n8n workflow pipelines, API management tools, and DevOps utilities designed for enterprise API gateways (Apigee X, Apigee Edge, Azure APIM), AI media generation, and CI/CD workflows.

> **Problem:** Managing complex API gateway migrations, certificate rotations, AI video generation pipelines, and reporting workflows manually is error-prone and time-consuming.  
> **Solution:** Modular Python scripts and n8n workflow automations that turn multi-step DevOps and AI operations into single-command executions.

---

## Tooling Modules

### 1. n8n AI & Workflow Automation (`n8n-workflow-automation`)
* **AI Video & Media Production:** End-to-end automated pipelines combining Claude (Anthropic), ElevenLabs TTS, Whisper audio QC, HeyGen video lipsyncing, and OpusClip clipping.
* **Interactive Bot & Approvals:** Telegram webhook routers for interactive approval/rejection workflows syncing directly with Notion databases.
* **Reporting Pipelines:** Macro reports and daily briefing digests for team velocity and blocker tracking.

### 2. Apigee Edge Backup & Restore (`apgedge-backup-plan`)
Automated backup and restore scripts for Apigee Edge API proxies, target servers, KVMs, and environment artifacts.
* **Stack:** Python, REST APIs

### 3. Apigee X Automation (`apigeex-automation`)
Utilities for Apigee X API Key expiration calculation, activity logging, and quota field updates (`useEffectiveCount`).
* **Stack:** Python, Apigee Management API

### 4. Azure APIM Tools (`azure-apim-automation`)
Azure API Management classification scripts, ADO pipeline secret sync tools, and dynamic architecture diagram generators.
* **Stack:** Python, Azure SDK, Diagrams-as-Code

### 5. General Automation & Cert Utilities (`general-automations`)
* **Certificate Converters:** Seamless conversion between `.cer`, `.pem`, and `.pfx` formats for TLS endpoint setup.
* **XML & Policy Tools:** Extraction of IP access controls, KVM endpoints, and XML policy diff comparison.
* **Traffic Analytics:** Scripts for fetching total cross-platform traffic metrics across Apigee & Azure APIM.

### 6. GitHub Actions & Governance (`github-automation`)
Automated workflow generators for change documentation, CODEOWNERS assignment, and branch protection enforcement.

---

## Getting Started

### Prerequisites
* Python 3.9+
* n8n v1.0+ (for importing workflow JSON files)
* `pip install -r requirements.txt`

```bash
git clone https://github.com/heidsEm/heidi-ai-automation-projects-2026.git
cd heidi-ai-automation-projects-2026
```

---

## License

This repository is maintained by [Heidi L. Embat](https://github.com/heidsEm). Licensed under the MIT License.

# AI & DevOps Automation Suite (2026)

A curated collection of production-grade Python automations, n8n workflow pipelines, API management utilities, and DevOps scripts designed for enterprise API gateways (Apigee X, Apigee Edge, Azure APIM), AI media generation, and CI/CD operations.

> **Problem:** Managing complex API gateway migrations, certificate rotations, AI video pipelines, and operational reporting manually is error-prone and time-consuming.  
> **Solution:** Modular Python scripts and n8n workflow automations that turn multi-step DevOps and AI operations into single-command executions.

---

## 📁 Repository Architecture

```
heidi-ai-automation-projects-2026/
├── n8n-workflows/                  # AI Media Generation & Interactive Telegram/Notion Workflows
├── apigee/                         # Apigee Edge Backup & Apigee X Operations Tooling
│   ├── edge-backup/
│   └── apigeex/
├── azure-apim/                     # Azure API Management ADO Sync, Classification & Diagrams
│   ├── ado-migration/
│   ├── api-identifier/
│   └── diagram-generator/
├── devops-utilities/               # Cert Converters, Policy Parsers & Cross-Platform Analytics
│   ├── cert-converter/
│   ├── formatting-tools/
│   ├── policy-tools/
│   └── traffic-analytics/
└── github-automation/              # Branch Protection & CI/CD Governance Scripts
    ├── branch-protection/
    └── workflows/
```

---

## ⚙️ Module Breakdown

### 1. n8n AI & Workflow Automation (`/n8n-workflows/`)
* **AI Video & Media Production:** End-to-end automated pipelines combining Claude (Anthropic), ElevenLabs TTS, Whisper audio QC, HeyGen video lipsyncing, and OpusClip clipping.
* **Interactive Bot & Approvals:** Telegram webhook routers for interactive approval/rejection workflows syncing directly with Notion databases.
* **Reporting Pipelines:** Macro reports and daily briefing digests for team velocity and blocker tracking.

### 2. Apigee API Gateway Management (`/apigee/`)
* **Edge Backup & Restore:** Automated scripts for proxies, target servers, KVMs, and environment artifacts.
* **Apigee X Automation:** Quota field updates (`useEffectiveCount`), key date calculations, and CSA activity reporting.

### 3. Azure API Management (`/azure-apim/`)
* **ADO Migration & Secret Sync:** Automated Azure DevOps pipeline key management.
* **Diagrams-as-Code:** Python script generating living APIM architecture diagrams (WAF, Gateway, Auth, Backend).

### 4. DevOps Utilities & Cert Tools (`/devops-utilities/`)
* **Certificate Converters:** Conversion between `.cer`, `.pem`, and `.pfx` formats.
* **Policy Parsers:** XML policy diff comparison, IP whitelist extraction, and KVM endpoint enumeration.
* **Traffic Analytics:** Cross-platform analytics scripts for Apigee & Azure APIM.

### 5. GitHub Governance (`/github-automation/`)
* Branch protection PR enforcers, CODEOWNERS assigners, and automated change documentation workflows.

---

## 🚀 Getting Started

### Prerequisites
* Python 3.9+
* n8n v1.0+ (for importing workflow JSON files)
* Install Python dependencies:
  ```bash
  pip install -r requirements.txt
  ```

### Quick Clone
```bash
git clone https://github.com/heidsEm/heidi-ai-automation-projects-2026.git
cd heidi-ai-automation-projects-2026
```

---

## 🔒 Security & Compliance
All API keys, tokens, webhooks, and private credentials across all JSON workflows and Python scripts have been sanitized with standard placeholders and environment variables.

---

## 📜 License
Maintained by [Heidi L. Embat](https://github.com/heidsEm). Licensed under the [MIT License](LICENSE).

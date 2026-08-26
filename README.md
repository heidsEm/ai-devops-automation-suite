# AI & DevOps Automation Suite (2026)

A curated collection of production-ready Python automations, API management tools, and DevOps utilities designed for enterprise API gateways (Apigee X, Apigee Edge, Azure APIM) and CI/CD workflows.

> **Problem:** Managing complex API gateway migrations, certificate rotations, policy syncs, and architecture diagrams manually is error-prone and time-consuming.  
> **Solution:** Modular Python automation tools that turn multi-step DevOps operations into single-command executions.

---

## Tooling Modules

### 1. Apigee Edge Backup & Restore (`apgedge-backup-plan`)
Automated backup and restore scripts for Apigee Edge API proxies, target servers, KVMs, and environment artifacts.
* **Stack:** Python, REST APIs

### 2. Apigee X Automation (`apigeex-automation`)
Utilities for Apigee X API Key expiration calculation, activity logging, and quota field updates (`useEffectiveCount`).
* **Stack:** Python, Apigee Management API

### 3. Azure APIM Tools (`azure-apim-automation`)
Azure API Management classification scripts, ADO pipeline secret sync tools, and dynamic architecture diagram generators.
* **Stack:** Python, Azure SDK, Diagrams-as-Code

### 4. General Automation & Cert Utilities (`general-automations`)
* **Certificate Converters:** Seamless conversion between `.cer`, `.pem`, and `.pfx` formats for TLS endpoint setup.
* **XML & Policy Tools:** Extraction of IP access controls, KVM endpoints, and XML policy diff comparison.
* **Traffic Analytics:** Scripts for fetching total cross-platform traffic metrics across Apigee & Azure APIM.

### 5. GitHub Actions & Governance (`github-automation`)
Automated workflow generators for change documentation, CODEOWNERS assignment, and branch protection enforcement.

---

## Getting Started

### Prerequisites
* Python 3.9+
* `pip install -r requirements.txt`

```bash
git clone https://github.com/heidsEm/heidi-ai-automation-projects-2026.git
cd heidi-ai-automation-projects-2026
```

---

## License

This repository is maintained by [Heidi L. Embat](https://github.com/heidsEm). Licensed under the MIT License.

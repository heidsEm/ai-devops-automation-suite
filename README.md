# AI & DevOps Automation Suite

An enterprise-grade portfolio of **AI Orchestration Pipelines**, **Media Automation Engines**, **Cloud API Gateways (Apigee & Azure APIM)**, and **DevOps Infrastructure Utilities**.

---

## 👤 Engineering Overview

I build and support production systems — making complex API, cloud, and AI automation workflows easier to operate. 

This repository consolidates **14 production-ready projects** demonstrating end-to-end capabilities across AI workflow engineering, web app development, API gateway management, PKI security, and CI/CD repository governance.

---

## 🚀 Projects Overview

| # | Project Directory | Domain | Primary Tech Stack | Description |
|---|---|---|---|---|
| **01** | [`projects/n8n-ai-automation-pipelines`](projects/n8n-ai-automation-pipelines) | AI Automation | n8n, Claude API, ElevenLabs, Telegram | Multi-agent content generation & automated reporting pipelines |
| **02** | [`projects/elevenlabs-batch-audio-engine`](projects/elevenlabs-batch-audio-engine) | Media / Audio | JavaScript, ElevenLabs API, FFmpeg WASM | Client-side batch TTS generator with FFmpeg speed variants |
| **03** | [`projects/heygen-video-batch-submitter`](projects/heygen-video-batch-submitter) | Media / Video | JavaScript, HeyGen API v2/v3, CSV Export | Avatar video batch generator with automated template variable mapping |
| **04** | [`projects/video-overlay-studio`](projects/video-overlay-studio) | Media / Canvas | HTML5 Canvas, Web Audio, MediaRecorder | Web compositing studio for burning text & B-roll overlays onto video |
| **05** | [`projects/social-media-automation-hub`](projects/social-media-automation-hub) | Governance | HTML5/CSS3, SPA Architecture, n8n Docs | 15-platform setup guide & comprehensive n8n API reference dashboard |
| **06** | [`projects/eod-update-summary-tool`](projects/eod-update-summary-tool) | Productivity | JavaScript, HTML5 Drag-and-Drop, html2canvas | Interactive daily engineering status card with PNG export |
| **07** | [`projects/ai-meeting-transcription-suite`](projects/ai-meeting-transcription-suite) | AI Speech | Python, Whisper API, Claude API, YouTube API | Meeting audio/video transcription & action-item summary engine |
| **08** | [`projects/dropbox-cloud-storage-automation`](projects/dropbox-cloud-storage-automation) | Cloud Storage | Python, Dropbox SDK, openpyxl | Automated Dropbox directory hierarchy creator & Excel sheet splitter |
| **09** | [`projects/apigee-gateway-management`](projects/apigee-gateway-management) | API Management | Python, Apigee Edge/X Admin APIs, XML/JSON | Apigee gateway proxy backup, restore & quota policy automation |
| **10** | [`projects/azure-apim-ops-suite`](projects/azure-apim-ops-suite) | API Management | Python, Azure APIM REST, Azure DevOps, Graphviz | Azure APIM classification, ADO secret sync & Diagrams-as-Code |
| **11** | [`projects/devops-utilities-toolkit`](projects/devops-utilities-toolkit) | Security & PKI | Python, OpenSSL, ElementTree XML, Matplotlib | X.509 cert converters (`.cer`/`.pem`/`.pfx`), policy XML tools & traffic analytics |
| **12** | [`projects/github-automation-suite`](projects/github-automation-suite) | CI/CD Governance | Python, GitHub REST API, GitHub Actions | Repository branch protection, CODEOWNERS, & reusable CI/CD workflows |
| **13** | [`projects/world-time-converter`](projects/world-time-converter) | Operations Utility | HTML5, CSS3, JavaScript ES6+, Intl API | Real-time global timezone converter & time difference matrix |
| **14** | [`projects/script-ost-splitter`](projects/script-ost-splitter) | Media / Production | JavaScript ES6+, RegEx AST, CSV/SRT Exporter | Script parser splitting spoken narration from On-Screen Text (OST) cues |

---

## 🏗️ System Architecture

```
                    ┌────────────────────────────────────────┐
                    │      n8n Orchestration Engine          │
                    └──────────────────┬─────────────────────┘
                                       │
           ┌───────────────────────────┼───────────────────────────┐
           ▼                           ▼                           ▼
┌─────────────────────┐     ┌─────────────────────┐     ┌─────────────────────┐
│  AI Video Pipelines │     │   Media Generation  │     │  Cloud & API Ops    │
│  - Claude Scripting │     │  - ElevenLabs TTS   │     │  - Apigee Edge/X    │
│  - HeyGen Avatars   │     │  - Video Overlay    │     │  - Azure APIM       │
│  - Content Prompts  │     │  - EOD Summary      │     │  - GitHub Workflows │
└─────────────────────┘     └─────────────────────┘     └─────────────────────┘
```

---

## 💻 Tech Stack Matrix

* **AI & Language Models:** Anthropic Claude API, OpenAI Whisper API, HeyGen Avatar API, ElevenLabs TTS API
* **API Management:** Apigee Edge, Apigee X, Azure API Management (APIM), OpenAPI / Swagger
* **Orchestration & Workflow:** n8n, GitHub Actions, Async / Event-Driven Pipelines
* **Cloud & DevOps:** Azure DevOps, Dropbox Cloud API, OpenSSL PKI, Terraform, Python 3.10+
* **Frontend & Media:** HTML5 Canvas API, Web Audio API (OfflineAudioContext), FFmpeg WebAssembly, MediaRecorder

---

## 🔒 Security & Privacy Disclosure

All code, configurations, workflows, and documentation in this repository have undergone 100% security sanitization. All real API keys, bearer tokens, passwords, company names, personal names, phone numbers, and environment URLs have been replaced with standardized safe placeholders (`YOUR_API_KEY`, `YOUR_ACCESS_TOKEN`, `user@example.com`).

For details, refer to the [Security & Sanitization Policy](docs/guides/security_sanitization_policy.md).

---

## 📄 License

This repository is licensed under the [MIT License](LICENSE).

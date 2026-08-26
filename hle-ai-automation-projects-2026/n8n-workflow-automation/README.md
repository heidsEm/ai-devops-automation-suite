# n8n AI & Workflow Automation Pipelines

A suite of production-grade **n8n automation workflows** built for automated media production, multi-agent AI script generation, speech synthesis, and real-time interactive messaging via Telegram & Notion APIs.

---

## ⚙️ Workflows Included

### 1. Automated AI Video & Media Pipelines
* **`crp-tg-sf-workflow-stacy.json`**: Short-form video production pipeline integrating Claude script generation, ElevenLabs TTS, Whisper audio QC, HeyGen lipsyncing, and YouTube upload.
* **`crp-mflf-thumbnail-graphics-stacy.json`**: Medium/Long-form video & podcast pipeline with automated thumbnail composite engine, sentiment extraction, OpusClip clipping, and Spotify audio packaging.

### 2. Interactive Bot & Approval Engine
* **`crp-tg-interactions.json`**: Real-time Telegram bot webhook callback router handling `Approve` / `Reject` actions, Notion database state updates, and force-reply rejection feedback.

### 3. Automated Reporting & Digest Pipelines
* **`crp-tg-weekly-macro-report.json`**: Weekly macro report aggregator querying Notion content library & blockers to calculate status and metrics.
* **`crp-tg-sat-preview.json`**: Saturday preview digest generator sending content previews with inline approval buttons to Telegram.
* **`crp-tg-daily-digest.json`**: Daily briefing workflow summarizing daily shipped items and open blockers.

---

## 🔒 Security Note
All API keys, tokens, webhooks, and private credentials in these workflow templates have been sanitized with environment variables and placeholders for safe open-source sharing.

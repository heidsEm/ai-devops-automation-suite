# n8n AI Automation Pipelines

## Overview
Multi-agent automation workflows integrating LLM script generation, speech synthesis, audio quality control, and scheduled digest generation.

## Problem
Manual content creation and reporting across multiple channels is slow, inconsistent, and error-prone.

## Solution
Automates multi-stage content pipelines using n8n, Claude API, ElevenLabs API, and automated Telegram/email notification nodes.

## Tech Stack
- n8n Workflow Automation
- Anthropic Claude API
- ElevenLabs TTS API
- Python & JSON Data Pipelines
- Telegram & Webhook Triggers

## Architecture / Workflow
Webhook / Schedule Trigger -> Prompt Generation Node -> Claude API Execution -> Audio Synthesis -> Output Routing & Digest Notification.

## Key Features
- Automated daily and weekly macro digest reporting
- Multi-agent script generation with customizable tone
- Automated SAT preview and Telegram interaction routing
- Modular JSON workflow export for rapid deployment

## Project Structure
```
projects/n8n-ai-automation-pipelines/
├── README.md
├── config/
└── scripts/
```

## Setup
1. Import any `.json` file from `config/` into your n8n instance.
2. Configure credentials.

## Example
```json
{"name": "AI Pipeline"}
```

## Security & Privacy
All API tokens and credentials redacted.

## Skills Demonstrated
- Enterprise n8n Workflow Design
- AI API Integration

# HeyGen Video Batch Submitter

## Overview
Batch video generation submitter interfacing with HeyGen Template API v2/v3.

## Problem
Creating avatar videos manually through web UIs for dozens of scripts takes hours of repetitive clicking.

## Solution
Automates batch asset uploading, dynamic variable replacement, asynchronous rendering request submission, and queue status polling.

## Tech Stack
- JavaScript (ES6+)
- HeyGen Template & Asset API v2/v3
- Async/Await & Fetch API
- CSV Export Engine

## Architecture / Workflow
Select Audio Files -> Auto-upload to HeyGen Asset API -> Map Template Variables -> Batch Submit Render Jobs -> Poll Status -> Export Results CSV.

## Key Features
- Automated template variable discovery & dynamic drop-down selection
- Direct binary MP3/WAV asset uploading
- Configurable submission delay to avoid API rate limits
- Real-time job status polling and CSV results export

## Project Structure
```
projects/heygen-video-batch-submitter/
├── README.md
└── src/
    └── heygen_batch_submitter.html
```

## Setup
1. Open `src/heygen_batch_submitter.html` in a web browser.
2. Input your HeyGen API Key and Template ID.
3. Click 'Load Template Variables', select audio files, and click 'Submit All'.

## Example
```javascript
const API_BASE = "https://api.heygen.com";
```

## Security & Privacy
All API keys are entered via secure client-side password inputs and redacted in version control.

## Skills Demonstrated
- Batch REST API Automation & Polling Workflows
- File Handling & Binary Data Uploading
- Defensive Error Handling & CSV Generation

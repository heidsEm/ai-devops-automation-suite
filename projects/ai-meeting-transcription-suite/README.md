# AI Meeting Transcription Suite

## Overview
Automated meeting audio/video transcription and executive action-item summarization suite.

## Problem
Long technical meetings require hours of manual note-taking to extract key decisions and action items.

## Solution
Uses OpenAI Whisper API for timestamped speech-to-text and Anthropic Claude / GPT-4 for structured executive summaries.

## Tech Stack
- Python 3.10+
- OpenAI Whisper API
- Anthropic Claude API
- youtube_transcript_api

## Architecture / Workflow
Audio/Video Input -> FFmpeg 16kHz WAV Chunking -> Whisper API Transcription -> Timestamped SRT/TXT Generation -> LLM Summary Synthesis.

## Key Features
- Automatic WAV chunking for large files
- Output in TXT, SRT, and Executive Summary
- YouTube transcript fetching utility

## Project Structure
```
projects/ai-meeting-transcription-suite/
├── README.md
└── scripts/
```

## Setup
1. Set API keys: `OPENAI_API_KEY`, `ANTHROPIC_API_KEY`.
2. Run `python scripts/crp_transcribe.py meeting.mp4`.

## Example
```bash
python scripts/crp_transcribe.py meeting.mp4
```

## Security & Privacy
Credentials managed via environment variables.

## Skills Demonstrated
- Multi-Model AI Orchestration

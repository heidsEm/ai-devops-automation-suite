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
- FFmpeg Audio Processing

## Architecture / Workflow
Audio/Video Input -> FFmpeg 16kHz WAV Chunking -> Whisper API Transcription -> Timestamped SRT/TXT Generation -> LLM Summary Synthesis.

## Key Features
- Automatic WAV chunking for large video/audio files
- Output generation in TXT (timestamped), SRT (subtitles), and Executive Summary
- YouTube transcript fetching utility for online video inputs
- Environment variable configuration via `.env`

## Project Structure
```
projects/ai-meeting-transcription-suite/
├── README.md
└── scripts/
    ├── crp_transcribe.py
    └── youtube_transcript_api_extractor.py
```

## Setup
1. Install requirements: `pip install openai anthropic python-dotenv youtube_transcript_api`.
2. Set environment variables: `export OPENAI_API_KEY="YOUR_API_KEY"` and `export ANTHROPIC_API_KEY="YOUR_API_KEY"`.
3. Run: `python scripts/crp_transcribe.py meeting.mp4`.

## Example
```bash
python scripts/crp_transcribe.py meeting.mp4 --output-dir ./transcripts
```

## Security & Privacy
API keys are loaded securely from environment variables. Temporary WAV chunks are purged immediately after processing.

## Skills Demonstrated
- Audio Processing & FFmpeg Pipeline Integration
- Multi-Model AI Orchestration (Whisper + Claude/GPT-4)
- Automated Transcript & Subtitle Formatting

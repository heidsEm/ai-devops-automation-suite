# ElevenLabs Batch Audio Engine

## Overview
High-throughput Text-to-Speech generation web engine with in-browser FFmpeg audio speed variant processing.

## Problem
Generating individual voice tracks manually for multiple scripts and speed variations creates massive production bottlenecks.

## Solution
Provides a single-page batch web tool that connects to ElevenLabs API for multi-voice generation and runs FFmpeg in WebAssembly for instant speed variations.

## Tech Stack
- HTML5 / JavaScript (ES6+)
- ElevenLabs REST API
- FFmpeg WebAssembly
- CSS3 UI

## Architecture / Workflow
User Inputs API Key & Voice IDs -> Text Script Batched -> ElevenLabs API Calls -> In-Browser FFmpeg Post-Processing -> Downloadable MP3 Variants.

## Key Features
- Dynamic Voice Slot Management (1 to 10 voice IDs per batch)
- Live Model Fetching & Custom Stability/Similarity Sliders
- Browser-side FFmpeg WebAssembly +15%, +20%, +30% audio speed variants
- Zero-server client-side execution

## Project Structure
```
projects/elevenlabs-batch-audio-engine/
├── README.md
└── src/
    └── elevenlabs_audio_generator.html
```

## Setup
1. Open `src/elevenlabs_audio_generator.html` in browser.
2. Enter API key and script.

## Example
```html
<input type="password" id="apiKey">
```

## Security & Privacy
API keys stored only in browser memory.

## Skills Demonstrated
- REST API Integration
- WebAssembly Audio Processing

# Video Overlay Studio

## Overview
In-browser video compositing engine for burning on-screen text (OST) and B-roll overlays onto video tracks.

## Problem
Adding broadcast-quality text callouts, lower thirds, and B-roll cuts traditionally requires heavy desktop video editing software.

## Solution
Builds a browser-native HTML5 Canvas and Web Audio compositing studio with interactive multi-track timeline, auto-timing, and real-time MediaRecorder rendering.

## Tech Stack
- HTML5 Canvas API
- Web Audio API
- HTML5 MediaRecorder API
- JavaScript ES6 Modules

## Architecture / Workflow
Load Video -> Auto-Decode Waveform & Speech Bursts -> Position Text & B-roll Overlay Clips -> Real-time Canvas Compositing -> MediaRecorder MP4/WebM Render.

## Key Features
- Real-time HTML5 Canvas text styling
- OfflineAudioContext speech energy detection for automatic subtitle alignment
- Interactive multi-track timeline with drag-to-trim handles
- In-browser 1080p video rendering & instant file download

## Project Structure
```
projects/video-overlay-studio/
├── README.md
└── src/
    └── video_overlay_studio.html
```

## Setup
1. Open `src/video_overlay_studio.html` in Chrome/Edge.
2. Load video and add overlays.

## Example
```javascript
const CANVAS_W = 1920, CANVAS_H = 1080;
```

## Security & Privacy
100% client-side execution.

## Skills Demonstrated
- HTML5 Canvas & Web Audio Engineering

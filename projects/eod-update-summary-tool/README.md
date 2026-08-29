# EOD Update Summary Tool

## Overview
Interactive daily status update card builder with PNG image export and drag-and-drop reordering.

## Problem
Formatting daily engineering progress reports for team channels is tedious and visually inconsistent.

## Solution
Provides a clean card UI for tracking Completed, Active, and Pending tasks with interactive drag-and-drop reordering and html2canvas PNG export.

## Tech Stack
- HTML5 / CSS3
- JavaScript Drag & Drop API
- html2canvas PNG Library

## Architecture / Workflow
Edit Inline Content -> Drag to Reorder Tasks -> Upload Reference Attachments -> Click Save as Image -> High-Res PNG Download.

## Key Features
- Inline contenteditable task fields
- Drag-and-drop task reordering
- One-click high-resolution PNG snapshot generation

## Project Structure
```
projects/eod-update-summary-tool/
├── README.md
└── src/
    └── eod_update_summary.html
```

## Setup
1. Open `src/eod_update_summary.html` in browser.

## Example
```html
<div id="card"><h1>EOD Summary</h1></div>
```

## Security & Privacy
100% client-side execution.

## Skills Demonstrated
- HTML5 Drag-and-Drop & DOM Snapshotting

# Script -> OST Splitter

## Overview
An automated script parser and cue-sheet generator that separates spoken narration from On-Screen Text (OST) visual cues and graphic prompts.

## Problem
Video production workflows require manual extraction of spoken narration, lower thirds, and B-roll graphic prompts from master script documents.

## Solution
Parses structured markdown/text scripts to separate spoken audio from OST cues, calculates estimated section runtimes, highlights triggers, and exports ready-to-use CSV/SRT cue sheets.

## Tech Stack
- HTML5 / CSS3 (Anton & JetBrains Mono typography)
- JavaScript ES6+ (Regex parsing & AST cue extraction)
- Web Storage API

## Architecture / Workflow
Paste Master Script -> RegEx AST Parser -> Separate Narration & OST Cues -> Calculate WPM Word Offsets -> Render Dual-Column Editing View & Export CSV/SRT.

## Key Features
- Automated dual-column view: Narration on left, OST Cues on right
- Interactive click-to-sync highlight between spoken lines and OST cards
- Configurable speaking speed (WPM) with live runtime estimations
- Export cue sheets to CSV, SRT subtitles, or clean narration TXT
- Built-in multi-version script tab manager

## Project Structure
```
projects/script-ost-splitter/
├── README.md
└── src/
    └── script_ost_splitter.html
```

## Setup
1. Open `src/script_ost_splitter.html` in any web browser.
2. Paste a master script and click '⚡ Split Script & Generate Cues'.

## Example
```
O.S.T. : RECOVER WHAT YOU'RE OWED
SCRIPT LINE: Does someone still owe you money?
```

## Security & Privacy
Executed entirely in browser memory. Zero external server dependencies or API calls.

## Skills Demonstrated
- Text Parsing & Regular Expression AST Construction
- Interactive UI State Synchronization
- Client-Side CSV & SRT File Export Generation

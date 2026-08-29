# World Time Converter

## Overview
An interactive client-side web application for real-time international timezone conversion and hour-offset matrix visualization.

## Problem
Coordinating global DevOps deployments, client meetings, and multi-region incident responses across different timezones causes scheduling errors and manual math mistakes.

## Solution
Provides a clean single-page interface with live UTC clock, instant city search, dark/light theme switching, and automatic time difference matrix calculation relative to any chosen home city.

## Tech Stack
- HTML5 / CSS3 (DM Sans & DM Mono typography)
- JavaScript ES6+ (Intl.DateTimeFormat API)
- LocalStorage state persistence

## Architecture / Workflow
User Adds Cities -> Live UTC Clock Engine -> Intl.DateTimeFormat Calculation -> Real-Time City Cards & Time Difference Matrix Rendered.

## Key Features
- Live UTC clock with real-time second updates
- Global city search covering 100+ major financial and engineering hubs
- Dynamic time difference grid (+/- hours ahead or behind home city)
- Date and time converter panel for specific future deployment times
- Dark & Light mode theme switching with state persistence

## Project Structure
```
projects/world-time-converter/
├── README.md
└── src/
    └── world_time_converter.html
```

## Setup
1. Open `src/world_time_converter.html` in any web browser.
2. Search and add target cities, or set a home city in Settings.

## Example
```javascript
const fmt = new Intl.DateTimeFormat('en-AU', { timeZone: 'Asia/Tokyo', hour: '2-digit', minute: '2-digit' });
```

## Security & Privacy
100% client-side execution. No user search data or location info is transmitted to external servers.

## Skills Demonstrated
- Native JavaScript Internationalization API
- Responsive CSS Grid & Dynamic Theme State Management

#!/usr/bin/env python3
"""
Video Content Package Prompt Creator

Creates ready-to-copy prompts for generating short-form, medium-form, or long-form
video content packages for enterprise and technical audiences.
"""

from __future__ import annotations
import argparse
import csv
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, Iterable, List, Optional

AUDIENCE_DEFAULT = "Enterprise clients, engineering teams, and technical business owners."
PURPOSE_DEFAULT = "Engagement, authority, technical trust, and enquiry generation."

MODE_GUIDANCE = {
    "short-form": {
        "length": "30-90 seconds",
        "structure": "Fast hook, one clear idea, tight proof/example, direct CTA.",
        "repurposing": "Include caption, thumbnail, and cutdown notes.",
    },
    "medium-form": {
        "length": "3-7 minutes",
        "structure": "Hook, context, 3-5 teaching points, practical example, CTA.",
        "repurposing": "Include 3-6 short-form cutdown ideas with hooks and timestamps.",
    },
    "long-form": {
        "length": "8-20 minutes",
        "structure": "Strong hook, problem framing, teaching sections, examples, objections, recap, CTA.",
        "repurposing": "Include 5-10 short-form cutdown ideas with hooks, timestamps, and angles.",
    },
}

@dataclass
class PromptInput:
    mode: str
    topic_title: str
    campaign_theme: str
    series_name: str
    content_angle: str
    audience: str = AUDIENCE_DEFAULT
    purpose: str = PURPOSE_DEFAULT

def normalize_mode(raw: str) -> str:
    val = (raw or "").strip().lower().replace("_", "-")
    aliases = {"short": "short-form", "shortform": "short-form", "short-form": "short-form",
               "medium": "medium-form", "mediumform": "medium-form", "medium-form": "medium-form",
               "long": "long-form", "longform": "long-form", "long-form": "long-form"}
    return aliases.get(val, "short-form")

def build_prompt(data: PromptInput) -> str:
    mode = normalize_mode(data.mode)
    guidance = MODE_GUIDANCE[mode]
    return f"""Create a {mode.upper()} video content package for this topic.

Topic Title: {data.topic_title}
Campaign / Main Theme: {data.campaign_theme}
Series Name: {data.series_name}
Content Angle: {data.content_angle}
Audience: {data.audience}
Purpose: {data.purpose}

Recommended video length: {guidance['length']}
Structure guidance: {guidance['structure']}

Include:
1. Recommended title
2. Hook options (at least 5)
3. Timestamped structure
4. Full presenter script
5. On-screen text & lower thirds
6. B-roll suggestions
7. CTA
8. Producer/editor notes
9. Short-form repurposing opportunities ({guidance['repurposing']})
""".strip()

if __name__ == "__main__":
    print("Video Content Package Prompt Creator Initialized.")

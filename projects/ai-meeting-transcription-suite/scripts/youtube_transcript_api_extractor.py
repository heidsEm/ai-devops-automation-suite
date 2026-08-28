#!/usr/bin/env python3
"""
YouTube Transcript API Extractor
Sanitized Utility to extract timestamped text from YouTube Videos for AI processing.
"""
import re
from youtube_transcript_api import YouTubeTranscriptApi

def extract_video_id(url_or_id: str) -> str:
    patterns = [
        r"(?:v=)([a-zA-Z0-9_-]{11})",
        r"(?:youtu\.be/)([a-zA-Z0-9_-]{11})",
        r"(?:embed/)([a-zA-Z0-9_-]{11})",
        r"^([a-zA-Z0-9_-]{11})$",
    ]
    for pattern in patterns:
        match = re.search(pattern, url_or_id)
        if match:
            return match.group(1)
    raise ValueError("Could not extract a valid YouTube video ID.")

def get_youtube_text(url_or_id: str, languages=None) -> str:
    video_id = extract_video_id(url_or_id)
    if languages is None:
        languages = ["en"]
    ytt_api = YouTubeTranscriptApi()
    transcript = ytt_api.fetch(video_id, languages=languages)
    return "\n".join(snippet.text for snippet in transcript)

if __name__ == "__main__":
    print("YouTube Transcript Extractor Ready.")

#!/usr/bin/env python3
"""
Video Content Prompt Creator Utility
Generates structured image and motion graphics prompts for multi-agent video pipelines.
"""
import sys
import argparse

def build_prompt(topic: str, style: str = "A"):
    return f"PROMPT (Style {style}): Minimalist line-art illustration representing {topic} on dark background."

def main():
    parser = argparse.ArgumentParser(description="Video Content Prompt Creator")
    parser.add_argument("--topic", required=True, help="Topic for prompt generation")
    parser.add_argument("--style", default="A", help="Style key (A or B)")
    args = parser.parse_args()
    
    prompt = build_prompt(args.topic, args.style)
    print(prompt)

if __name__ == "__main__":
    main()

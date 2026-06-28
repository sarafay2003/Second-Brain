import os
import json
import re
from datetime import datetime
from pathlib import Path

def sanitize_filename(name):
    if not name:
        return "untitled_conversation"
    name = re.sub(r'[\\/*?:"<>|]', "", name)
    return name.strip()

def convert_json_to_md(json_path):
    with open(json_path, 'r', encoding='utf-8') as f:
        try:
            data = json.load(f)
        except json.JSONDecodeError:
            print(f"Failed to decode JSON: {json_path}")
            return

    # Determine the subfolder name for the 'source' frontmatter
    source_folder = json_path.parent.name if json_path.parent.name != 'second-brain' else 'raw'
    if 'raw' in json_path.parts:
        # Get the folder immediately following 'raw'
        idx = json_path.parts.index('raw')
        if idx + 1 < len(json_path.parts):
            source_folder = json_path.parts[idx+1]

    # Case 1: List of conversations (like conversations.json)
    if isinstance(data, list):
        for entry in data:
            if isinstance(entry, dict) and 'chat_messages' in entry:
                process_conversation(entry, json_path.parent, source_folder)
    # Case 2: Single conversation object
    elif isinstance(data, dict) and 'chat_messages' in data:
        process_conversation(data, json_path.parent, source_folder)
    else:
        print(f"Unrecognized JSON structure in {json_path}. Skipping.")

def process_conversation(conv, output_dir, source_folder):
    title = conv.get('name') or "Untitled Conversation"
    created_at = conv.get('created_at', 'Unknown Date')
    messages = conv.get('chat_messages', [])

    # Format transcript
    transcript = []
    for msg in messages:
        sender = msg.get('sender', 'Unknown').capitalize()
        # Extract text from content list
        content_list = msg.get('content', [])
        text = ""
        if isinstance(content_list, list):
            text = "\n".join([item.get('text', '') for item in content_list if isinstance(item, dict)])
        elif isinstance(content_list, str):
            text = content_list

        if not text:
            text = msg.get('text', '')

        transcript.append(f"**{sender}**: {text}\n")

    full_text = "\n---\n".join(transcript)

    # Construct Markdown with Frontmatter
    md_content = f"---\nsource: {source_folder}\ndate: {created_at}\ntopic: {title}\n---\n\n# {title}\n\n{full_text}"

    # Save file
    filename = f"{sanitize_filename(title)}.md"
    # Avoid overwriting if title is too generic or collisions occur
    final_path = output_dir / filename
    counter = 1
    while final_path.exists():
        final_path = output_dir / f"{sanitize_filename(title)}_{counter}.md"
        counter += 1

    with open(final_path, 'w', encoding='utf-8') as f:
        f.write(md_content)
    print(f"Created: {final_path.name}")

def main():
    raw_root = Path('raw')
    if not raw_root.exists():
        print("raw/ directory not found.")
        return

    json_files = list(raw_root.rglob('*.json'))
    if not json_files:
        print("No JSON files found in raw/.")
        return

    for json_file in json_files:
        print(f"Processing {json_file}...")
        convert_json_to_md(json_file)

if __name__ == "__main__":
    main()

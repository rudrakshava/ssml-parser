"""
SSML Parser
A simple parser that converts SSML text into a structured format (list of tokens).
"""

import re

def parse_ssml(ssml_text):
    tokens = []
    tag_pattern = re.compile(r"<(/?)(\\w+)([^>]*)>")

    pos = 0
    for match in tag_pattern.finditer(ssml_text):
        # Add text between tags
        if match.start() > pos:
            tokens.append({"type": "text", "value": ssml_text[pos:match.start()]})

        tag_type = "end" if match.group(1) else "start"
        tag_name = match.group(2)
        tag_attrs = match.group(3).strip()

        tokens.append({"type": tag_type, "tag": tag_name, "attrs": tag_attrs})
        pos = match.end()

    # Add remaining text after last tag
    if pos < len(ssml_text):
        tokens.append({"type": "text", "value": ssml_text[pos:]})

    return tokens


if __name__ == "__main__":
    ssml = "<speak>Hello <break time=\"500ms\"/> world</speak>"
    result = parse_ssml(ssml)
    for token in result:
        print(token)

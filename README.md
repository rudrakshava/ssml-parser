# ssml-parser
# 🗣️ SSML Parser

A simple Python project to **parse SSML text** into structured tokens.  
This is useful for text-to-speech preprocessing.

## ⚡ Example

Input:
```xml
<speak>Hello <break time="500ms"/> world</speak>
output:
{'type': 'start', 'tag': 'speak', 'attrs': ''}
{'type': 'text', 'value': 'Hello '}
{'type': 'start', 'tag': 'break', 'attrs': 'time="500ms"/'}
{'type': 'text', 'value': ' world'}
{'type': 'end', 'tag': 'speak', 'attrs': ''}
run:


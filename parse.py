from fileinput import input
from re import match
import re
import llist
import sys

args = sys.argv
file_to_open = sys.argv[1]

with open(file_to_open) as f:
    lines = f.readlines()

conversation_log = []

for l in lines: 
	result = match('[A-z]+:', l)
	if result: 
		character_speech = l.replace('\n', "")
		character_speech = re.sub(r'\(.+\)', '', character_speech)
		conversation_log.append(character_speech)

conversation_by_character = {}
# for reference of previous line
conversation_lines = []
for index in range(0, len(conversation_log)):
	conversation_line = conversation_log[index]
	character = match('[A-z]+:', conversation_line).group(0).replace(':', '')
	character_line = str.strip(re.sub('[A-z]+:', '', conversation_line))
	conversation_lines.append(character_line)
	if not conversation_by_character.has_key(character):
		conversation_by_character[character] = []
	if (index == 0):
		conversation_by_character[character].append(['', character_line])
	else:
		previous_line = conversation_lines[index - 1]
		conversation_by_character[character].append([previous_line, character_line])

print conversation_by_character


		                                                                            
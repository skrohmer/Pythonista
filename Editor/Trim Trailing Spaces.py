import editor

text = editor.get_text()
replacement = ''
for line in text.splitlines():
	replacement += line.rstrip() + '\n'
replacement = replacement[:-1]   # don't use last linefeed

editor.replace_text(0, len(text), replacement)


import editor

text = editor.get_text()
selection = editor.get_line_selection()
selected_lines = text[selection[0]:selection[1]]
is_comment = selected_lines.strip().startswith('#')
replacement = ''
for line in selected_lines.splitlines():
	if is_comment:
		if line.strip().startswith('#'):
			replacement += line[line.find('#') + 1:] + '\n'
		else:
			replacement += line + '\n'
	else:
		replacement += '#' + line + '\n'
replacement = replacement[:-1]   # don't use last linefeed

editor.replace_text(selection[0], selection[1], replacement)
editor.set_selection(selection[0], selection[0] + len(replacement))


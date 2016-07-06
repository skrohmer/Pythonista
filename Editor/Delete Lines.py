import editor

text = editor.get_text()
selection = editor.get_line_selection()
selected_lines = text[selection[0]:selection[1]]

if len(selected_lines) == len(text) - 1:
	editor.replace_text(selection[0], selection[1]+1, '\n')   # when complete text is deleted
else:
	editor.replace_text(selection[0], selection[1]+1, '')

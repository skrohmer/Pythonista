import editor

text = editor.get_text()
selection = editor.get_line_selection()
selected_lines = text[selection[0]:selection[1]]
replacement = selected_lines + '\n' + selected_lines

editor.replace_text(selection[0], selection[1], replacement)
editor.set_selection(selection[0], selection[0] + len(replacement))


''' Open the URL which is found in the selected line '''

# example: https://forum.omz-software.com, http://www.google.de

import editor
import ui


class MyWebView(ui.View):
	def __init__(self, url):
		self.width, self.height = ui.get_window_size()
		self.wv = ui.WebView(frame=self.bounds)
		self.wv.load_url(url)
		self.add_subview(self.wv)
		bi_back = ui.ButtonItem(image=ui.Image.named('iob:ios7_arrow_back_32'))
		bi_forward = ui.ButtonItem(image=ui.Image.named('iob:ios7_arrow_forward_32'))
		bi_back.action = self.go_back
		bi_forward.action = self.go_forward
		self.right_button_items = [bi_forward, bi_back]
		self.present()

	def go_back(self, bi):
		self.wv.go_back()
	
	def go_forward(self, bi):
		self.wv.go_forward()


def rstrip_notalpha(s):
	for i in range(len(s)-1, 14, -1):
		if s[i].isalpha():
			return s[:i+1]
	return s

text = editor.get_text()
selection = editor.get_line_selection()
selected_lines = text[selection[0]:selection[1]]
elements = selected_lines.split()
urls = [x for x in elements if 'http' in x]
for u in urls:
	u = rstrip_notalpha(u)
	wv = MyWebView(u)
	wv.wait_modal()
	


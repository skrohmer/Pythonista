import clipboard
import console
import editor
import ftplib
import os
import sys


ftp_srv = 'XXXXXXXX'
ftp_usr = 'XXXXXXXX'
ftp_pwd = 'XXXXXXXX'

tmp = 'clipboard.txt'

mode = 'R'
if len(sys.argv) > 1:
	mode = sys.argv[1]

if mode == 'W':
	text = editor.get_text()
	selection = editor.get_selection()
	selected_chars = text[selection[0]:selection[1]]
	if len(selected_chars) != 0:
		c = selected_chars
	else:
		c = clipboard.get()
	f = open(tmp, 'w')
	f.write(c)
	f.close()
	
	ftp = ftplib.FTP()
	print('Connect...')
	ftp.connect(ftp_srv)
	print('Login...')
	ftp.login(ftp_usr, ftp_pwd)
	print('Store...')
	ftp.storbinary("STOR " + tmp, open(tmp, 'rb'))
	print('Quit...')
	ftp.quit()
	
	console.hud_alert('Clipboard sent')
	os.remove(tmp)
	
elif mode == 'R':
	ftp = ftplib.FTP()
	print('Connect...')
	ftp.connect(ftp_srv)
	print('Login...')
	ftp.login(ftp_usr, ftp_pwd)
	print('Retrieve...')
	ftp.retrbinary("RETR " + tmp, open(tmp, 'wb').write)
	print('Quit...')
	ftp.quit()

	f = open(tmp, 'r')
	c = f.read()
	f.close()
	clipboard.set(c)
	console.hud_alert('Clipboard received')
	os.remove(tmp)

else:
	print("Invalid mode: '%s'" % (mode))

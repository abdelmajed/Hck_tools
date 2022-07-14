import ftplib
def anonLogin(hostname):
	try:
		ftp = ftplib.FTP(hostname)
		ftp.login('anonymous', 'me@your.com')
		print '\n[*] '+str(hostname)+' FTP Anonymous Logon Succeeded.'
		ftp.quit()
		return True
	except Exception, e:
		print '\n[-] '+str(hostname)+' FTP Anonymous Logon Failed.'
		return False



for host  in ['10.42.0.1', '10.42.0.184', '10.42.0.113', '10.42.0.200', '10.42.0.33']:
	anonLogin(host)

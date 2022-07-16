import ftplib

def retList(ftp):
	try:
		dirList = ftp.nlst()
	except Exception, e:
		print '[-] Could not list directory contents.'
		print '[-] Skipping To Next Target.'
		return
	
	retList = []
	for filename in dirList:
		fn= filename.lower()
		if '.php' in fn  or '.html' in fn or '.htm'  in fn or '.asp' in fn:
			print '[*] Found default page: '+filename
			retList.append(filename)
	return retList

host = '127.0.0.1'
username = 'whoami'
password = 'luser-bash'
ftp = ftplib.FTP(host)
ftp.login(username, password)
retList(ftp)

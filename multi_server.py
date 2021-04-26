import socket
from _thread import *
import threading

def threaded(c,addr):
	while True:
		data=c.recv(1024)
		if not data:
			break
		data=data[::-1]
		c.sendall(data)
	print('Connection closed by: ',addr[0],' ',addr[1])
	c.close()



host = ""
  
# reverse a port on your computer
# in our case it is 12345 but it
# can be anything
port = 12345
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((host, port))
print("socket binded to port", port)
  
# put the socket into listening mode
s.listen(5)
print("socket is listening")

while True:
	c,addr=s.accept()
	print('Connected to : ',addr[0],':', addr[1])
	start_new_thread(threaded,(c,addr))
	
s.close()

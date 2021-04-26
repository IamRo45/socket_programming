import socket

host='127.0.0.1'
port=12345
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))


while True:
	message=input('Say something')
	if (message=='bye'):
		break
	s.sendall(message.encode())
	data=s.recv(1024)
	print(str(data.decode('ascii')))

s.close()	
	

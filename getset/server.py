import socket
import threading
from threading import Thread

host='127.0.0.1'
port=5002
data=0

#client_sockets=set()
lock=threading.Lock()
s=socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host,port))
s.listen(5)
print(host," listening at port ",port)

def listen_for_client(cs):
	global data
	while True:
		try:
			msg=cs.recv(1204).decode()
			if (msg==''):
				print("Connection closed by client")
				break
		except Exception as e:
			#client is no longer connected
			print(" Error")
			#client_sockets.remove(cs)
		else:
			if msg=="GET":
				ret=str(data)
				cs.sendall(ret.encode())
			elif msg=="SET":
				curr=cs.recv(1024).decode()
				with lock:
					data=curr
					ret='Successful operation, data = '+data
					cs.sendall(ret.encode())

while True:
	cs,addr=s.accept()
	print(f"[+] {addr} connected.")
	#client_sockets.add(cs)
	t=Thread(target=listen_for_client, args=(cs,))
	t.daemon=True
	t.start()
	
for cs in client_sockets:
    cs.close()
# close server socket
s.close()

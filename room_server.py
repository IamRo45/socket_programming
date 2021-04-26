import socket
from threading import Thread

host='127.0.0.1'
port=5002
seperator_tok="<SEP>"

client_sockets=set()

s=socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host,port))
s.listen(5)
print(host," listening at port ",port)

def listen_for_client(cs):
	while True:
		try:
			msg=cs.recv(1204).decode()
		except Expection as e:
			#client is no longer connected
			print(" Error")
			client_sockets.remove(cs)
		else:
			msg=msg.replace(seperator_tok,": ")
		
		for client_socket in client_sockets:
			if client_socket!=cs:
				client_socket.send(msg.encode())

while True:
	cs,addr=s.accept()
	print(f"[+] {addr} connected.")
	client_sockets.add(cs)
	t=Thread(target=listen_for_client, args=(cs,))
	t.daemon=True
	t.start()
	
for cs in client_sockets:
    cs.close()
# close server socket
s.close()

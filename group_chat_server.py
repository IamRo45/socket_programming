import socket
from threading import Thread
from collections import defaultdict as df

host='127.0.0.1'
port=5002
seperator_tok="<SEP>"

client_sockets=set()
groups=df(set)

s=socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((host,port))
s.listen(5)
print(host," listening at port ",port)

def listen_for_client(cs,g_name,u_name):
	while True:
		try:
			msg=cs.recv(1204).decode()
			if (msg==''):
				#client is no longer connected
				print("User "+u_name+" got disconnected")
				groups[g_name].remove(cs)
				break
				
		except Exception as e:
			#client is no longer connected
			print("User "+u_name+" got disconnected")
			groups[g_name].remove(cs)
			
		else:
			msg=msg.replace(seperator_tok,": ")
		
		for client_socket in groups[g_name]:
			if client_socket!=cs:
				client_socket.send(msg.encode())

while True:
	cs,addr=s.accept()
	print(f"[+] {addr} connected.")
	u_name=cs.recv(1024).decode()
	g_name=cs.recv(1024).decode()
	
	if (g_name not in groups):
		cs.sendall('New group has been created'.encode())
	groups[g_name].add(cs)
	t=Thread(target=listen_for_client, args=(cs,g_name,u_name))
	t.daemon=True
	t.start()
	
for cs in client_sockets:
    cs.close()
# close server socket
s.close()

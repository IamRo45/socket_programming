import socket
from threading import Thread
import time




SERVER_HOST = "127.0.0.1"
SERVER_PORT = 5002 # server's port
separator_token = "<SEP>" # we will use this to separate the client name & message

# initialize TCP socket
s = socket.socket()
print(f"[*] Connecting to {SERVER_HOST}:{SERVER_PORT}...")
# connect to the server
s.connect((SERVER_HOST, SERVER_PORT))
print("[+] Connected.")

name=input("Enter your name: ")
s.sendall(name.encode())
time.sleep(0.1)
group=input("Enter your group: ")
s.sendall(group.encode())

def listen_for_messages():
	while True:
		message = s.recv(1024).decode()
		print("\n" + message)
        
t=Thread(target=listen_for_messages)
t.daemon =True
t.start()

while True:
	to_send=input()
	
	if to_send.lower()=='q':
		break
		
	to_send=name+separator_token+to_send
	s.sendall(to_send.encode())
s.close()

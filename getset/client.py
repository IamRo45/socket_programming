import socket

host="127.0.0.1"
port=5002

s=socket.socket()
s.connect((host,port))
print("[+] Connected.")


while True:
	ops=input("What you wanna do?")
	if ops=="GET":
		s.sendall(ops.encode())
		msg=s.recv(1024).decode()
		print("Current Value = ",msg)
	elif ops=="SET":
		s.sendall(ops.encode())
		inp=input("Enter the value: ")
		s.sendall(inp.encode())
		msg=s.recv(1024).decode()
		print(msg)
	elif ops=="q":
		break
s.close()
		

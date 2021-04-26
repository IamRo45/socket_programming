import socket
import sys

try:
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    print ("Socket successfully created")
except socket.error as err:
    print ("Socket creation falied with error %s" %(err))

port=80

try:
    host=socket.gethostbyname('www.google.com')
except socket.gaierror:

    print("there was an unexpected error")
    sys.exit()

s.connect((host,port))

print ("the socket is successfully connected to google")

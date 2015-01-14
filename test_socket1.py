import socket
import sys 
import time

# create socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#
server_address = (sys.argv[1], int(sys.argv[2]))
sock.connect(server_address)
print('connect success')
#
sock.recv(100)
print('recv end')
sock.send('aaaaaa')
sock.send('aaaaaa')
sock.send('aaaaaa')
sock.send('aaaaaa')
time.sleep(1000)

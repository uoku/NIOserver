import socket, sys

s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
host = '127.0.0.1'
while True:
    s.sendto('A'.encode('utf-8'), (host,8888))
    s.sendto('B'.encode('utf-8'), (host,8888))
    s.sendto('C'.encode('utf-8'), (host,8888))
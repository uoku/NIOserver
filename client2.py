import socket, sys, pickle

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = '127.0.0.1'
client.connect((host,8888))
while True:
    a=input()
    print(a)


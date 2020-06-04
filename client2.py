import socket, sys, json, pickle

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = '127.0.0.1'
client.connect((host,8888))


m = client.recv(10000)
print(json.loads(m.decode('utf-8')))


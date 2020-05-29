import socket, sys, pickle

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = '127.0.0.1'
client.connect((host,8888))
a = [
    [1,2,3],
    [3,2,1],
    [1,2,3],
]
client.send(pickle.dumps(a))
m = client.recv(10000)
print(pickle.loads(m))
while True:
    a=input()
    print(a)


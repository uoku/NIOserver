import socket, sys, json, pickle, threading

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host = '127.0.0.1'
client.connect((host,8888))


def listen():
    while True:
        m = client.recv(10000)
        print((json.loads(m.decode('utf-8'))))


t = threading.Thread(target=listen)
t.start()

while True:
    a = input('input')
    client.send(json.dumps(a).encode('utf-8'))



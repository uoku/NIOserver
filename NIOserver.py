import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind(('',8888))

s.setblocking(0)

data = ''

address = ''
while True:
    try:
        data, address = s.recvfrom(20000)
    except:
        pass
    else:
        data =data.decode('utf-8')
        print("recv:",data[0] ,'from:',address)
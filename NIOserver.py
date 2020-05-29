import select
import socket
import pickle, time, datetime

with socket.socket(socket.AF_INET,socket.SOCK_STREAM) as ServerSocket:
    ServerSocket.bind(('127.0.0.1', 8889))

    ServerSocket.setblocking(0)

    reader = [ServerSocket]
    writer = []
    error  = []
    ServerSocket.listen(5)

    while True:
        readable, writable, exception = select.select(reader, writer, error)

        for s in readable:
            if s == ServerSocket:
                print('connecting')
                client, addr = ServerSocket.accept()
                client.setblocking(0)
                reader.append(client)
            else:
                try:
                    t1 = datetime.datetime.now().microsecond
                    t3 = time.mktime(datetime.datetime.now().timetuple())
                    message = s.recv(10000)
                    if len(message) is 0:
                        print('asdf')
                        raise socket.error
                    else:
                        sentence =pickle.loads(message)
                        print(sentence)
                        s.send(pickle.dumps(sentence))
                    t2 = datetime.datetime.now().microsecond
                    t4 = time.mktime(datetime.datetime.now().timetuple())
                    strTime = 'funtion time use:%dms' % ((t4 - t3) * 1000 + (t2 - t1) / 1000)
                    print(strTime)
                except:
                    reader.remove(s)
                    Name, Port = s.getpeername()
                    print("disconnect to ",Name,"Port",Port)
                    s.close()


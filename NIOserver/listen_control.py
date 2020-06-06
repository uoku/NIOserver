import json
import select
from socket import error


def listen_control(socket, reader):
    print(reader)
    while True:
        readable, writable, exceptional = select.select(reader, [], [])

        for s in readable:
            if s is not socket:
                try:
                    message = s.recv(10000)
                    message = json.loads(message.decode('utf-8'))
                    if len(message) is 0:
                        raise error
                    else:
                        sname, sport = s.getpeername()
                        print(message)
                        for client in reader:
                            if client is not socket:
                                client.send(json.dumps(message).encode('utf-8'))
                except:
                    reader.remove(s)
                    sname, sport = s.getpeername()
                    print("disconnect to ", sname)
                    s.close()

import json
import select
from socket import error


def listen_control(socket, reader, map):
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
                        # 處理json message
                        action = message['action']
                        # end
                        # 根據 收到的json 做移動跟放水球
                        if action is 0:
                            # move up
                            move = 0
                        elif action is 1:
                            # move right
                            move = 1
                        elif action is 2:
                            # move down
                            move = 2
                        elif action is 3:
                            # move left
                            move = 3
                        elif action is 4:
                            # set waterball
                            move = 4
                        else:
                            # errors
                            print('something wrong')
                        # end
                        for client in reader:
                            if client is not socket:
                                # 從map 物件 拿出更改的資訊 存成json

                                #
                                client.send(json.dumps().encode('utf-8'))
                except:
                    reader.remove(s)
                    sname, sport = s.getpeername()
                    print("disconnect to ", sname)
                    s.close()

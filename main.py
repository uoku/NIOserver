import NIOserver as server
import listen_control
import json,pickle,threading
import Map


socket, reader = server.wait_for_gamer(2)

for player in reader:
    if player is not socket:
        msg =[{'head':"game start"}]
        player.send((json.dumps(msg)).encode('utf-8'))
reader = reader[1:]

listen_control.listen_control(socket, reader)


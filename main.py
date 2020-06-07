import NIOserver as server
import listen_control
import json,pickle,threading
import Map

player_num = 2

socket, reader = server.wait_for_gamer(player_num)

for player in reader:
    if player is not socket:
        msg =[{'head':"game start"}]
        player.send((json.dumps(msg)).encode('utf-8'))
reader = reader[1:]

solidobject = [[1,3],[2,4]]
map = Map.Map(100, 100, 15, 13, player_num, solidobject)

listen_control.listen_control(socket, reader, map)


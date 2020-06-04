import NIOserver as server
import json,pickle


socket , reader=server.wait_for_gamer(2)

for player in reader:
    if player is not socket:
        msg =[{'head':"game start"}]
        player.send((json.dumps(msg)).encode('utf-8'))



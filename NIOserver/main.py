import NIOserver as server
import listen_control
import json,pickle,threading


socket, reader = server.wait_for_gamer(2)

for player in reader:
    if player is not socket:
        msg =[{'head':"game start"}]
        player.send((json.dumps(msg)).encode('utf-8'))
reader = reader[1:]

# 建立地圖資訊----------------
class Map():
    def __init__(self,x,y,w,h,playernum,solidobj): #w,h is cell   x,y is 有幾格
        self.cell = [w,h]
        self.map = [x * w, y * h]
        self.cellmap = [x, y]
        self.solidobj = [solidobj]
        self.init_speed = 5
        self.init_waterball = 2
        self.init_power = 2
        self.size = [90,90]
        self.status = 0
        self.player=[]
        for i in range(playernum):
            position = [0, 0]
            direciotn = 1
            player_list=[self.init_speed, self.init_waterball, self.init_power, position, self.size, self.status, position, direciotn]
            player.append(player_list)

    def set_player_speed(self,player_num,newspeed):
        self.player[player_num][0]=newspeed


#---------------------------
listen_control.listen_control(socket, reader)


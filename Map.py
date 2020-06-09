import math


def colision(p1, p2):
    if (p1[0] + p1[2] > p2[0]) and (p2[0] + p2[2] > p1[0]) and (p1[1] + p1[3] > p2[1]) and (p2[1] + p2[3] > p1[1]):
        return True
    else:
        return False


class Map():
    def __init__(self, x, y, w, h, playernum, solidobj):  # w,h is cell   x,y is 有幾格
        self.timedis = 20
        self.cell = [w, h]
        self.map = [x * w, y * h]
        self.cellmap = [x, y]
        self.solidobj = [solidobj]
        self.waterball = []
        self.init_speed = 5
        self.init_waterball = 2
        self.init_power = 2
        self.size = [90, 90]
        self.status = 0
        self.player = []
        play_pos = [[0, 0], [14, 11]]
        for i in range(playernum):
            position = play_pos[i]
            direciotn = 1
            player_list = [self.init_speed, self.init_waterball, self.init_power, position, self.size, self.status,
                           direciotn]
            self.player.append(player_list)

    def add_player_speed(self, player_num):
        self.player[player_num][0] += 1

    def add_player_waterball(self, player_num):
        self.player[player_num][1] += 1

    def add_player_power(self, player_num):
        self.player[player_num][2] += 1

    def change_player_position(self, player_num, direct):
        # need to 判斷碰撞
        move_dis = self.player[player_num][0] * self.timedis
        x, y = self.player[player_num][3]
        new_x, new_y = x, y
        if direct is 0:
            new_y = y + move_dis
        elif direct is 1:
            new_x = x + move_dis
        elif direct is 2:
            new_y = y - move_dis
        elif direct is 3:
            new_x = x - move_dis
        else:
            print("move error")
            raise
        for obj in self.solidobj:
            if obj[2] <= 2:
                if colision([new_x, new_y, self.size[0], self.size[1]], [obj[0], obj[1], self.cell[0], self.cell[1]]):
                    new_x, new_y = x, y
        # 吃東西判斷
        if new_x != x and new_y != y:
            for object in self.solidobj:
                if [object[0], object[1]] == [new_x, new_y]:
                    # object[2] 是 物品種類
                    if object[2] == 3:  # 鞋子
                        self.player[player_num][0] += 1
                    elif object[2] == 4:  # 水球
                        self.player[player_num][1] += 1
                    elif object[2] == 5:  # 威力
                        self.player[player_num][2] += 1
                    else:
                        print('eat error')
                        raise

    def change_status(self, player_num, status):
        self.player[player_num][5] = status

    def set_waterball(self, player_num):
        if self.player[player_num][1] is not 0:
            x, y = self.player[player_num][3]
            x = math.ceil(x // self.cell[0])
            y = math.ceil(y // self.cell[1])
            self.waterball.append([x, y])


class Map():
    def __init__(self, x, y, w, h, playernum, solidobj):  # w,h is cell   x,y is 有幾格
        self.cell = [w, h]
        self.map = [x * w, y * h]
        self.cellmap = [x, y]
        self.solidobj = [solidobj]
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
                           position, direciotn]
            self.player.append(player_list)

    def add_player_speed(self, player_num):
        self.player[player_num][0] += 1

    def add_player_waterball(self, player_num):
        self.player[player_num][1] += 1

    def add_player_power(self, player_num):
        self.player[player_num][2] += 1

    def change_player_position(self, player_num, x, y):
        # need to 判斷碰撞
        self.player[player_num][3] = [x, y]

    def change_status(self, player_num, status):
        self.player[player_num][5] = status

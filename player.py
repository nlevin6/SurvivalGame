class Player:
    move_speed = 4

    def __init__(self, player_x, player_y, player_x_change, player_y_change):
        self.player_x = player_x
        self.player_y = player_y
        self.player_x_change = player_x_change
        self.player_y_change = player_y_change

    def get_player_x(self):
        return self.player_x

    def get_player_y(self):
        return self.player_y

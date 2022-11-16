class Enemy:
    move_speed = 2

    def __init__(self, enemy_x, enemy_y, enemy_x_change, enemy_y_change):
        self.enemy_x = enemy_x
        self.enemy_y = enemy_y
        self.enemy_x_change = enemy_x_change
        self.enemy_y_change = enemy_y_change

    def get_enemy_x(self):
        return self.enemy_x

    def get_enemy_y(self):
        return self.enemy_y

    def enemy_reset(self):
        pass
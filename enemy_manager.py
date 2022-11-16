import pygame

from background import screen

zombie_animation_up = [pygame.image.load('zombie/zombie_walk1_u.png').convert_alpha(),
                       pygame.image.load('zombie/zombie_walk1_u.png').convert_alpha(),
                       pygame.image.load('zombie/zombie_walk1_u.png').convert_alpha(),
                       pygame.image.load('zombie/zombie_walk1_u.png').convert_alpha(),
                       pygame.image.load('zombie/zombie_walk1_u.png').convert_alpha(),
                       pygame.image.load('zombie/zombie_walk2_u.png').convert_alpha(),
                       pygame.image.load('zombie/zombie_walk2_u.png').convert_alpha(),
                       pygame.image.load('zombie/zombie_walk2_u.png').convert_alpha(),
                       pygame.image.load('zombie/zombie_walk2_u.png').convert_alpha(),
                       pygame.image.load('zombie/zombie_walk2_u.png').convert_alpha(),
                       pygame.image.load('zombie/zombie_walk3_u.png').convert_alpha(),
                       pygame.image.load('zombie/zombie_walk3_u.png').convert_alpha(),
                       pygame.image.load('zombie/zombie_walk3_u.png').convert_alpha(),
                       pygame.image.load('zombie/zombie_walk3_u.png').convert_alpha(),
                       pygame.image.load('zombie/zombie_walk3_u.png').convert_alpha(),
                       pygame.image.load('zombie/zombie_walk4_u.png').convert_alpha(),
                       pygame.image.load('zombie/zombie_walk4_u.png').convert_alpha(),
                       pygame.image.load('zombie/zombie_walk4_u.png').convert_alpha(),
                       pygame.image.load('zombie/zombie_walk4_u.png').convert_alpha(),
                       pygame.image.load('zombie/zombie_walk4_u.png').convert_alpha(),
                       pygame.image.load('zombie/zombie_walk5_u.png').convert_alpha(),
                       pygame.image.load('zombie/zombie_walk5_u.png').convert_alpha(),
                       pygame.image.load('zombie/zombie_walk5_u.png').convert_alpha(),
                       pygame.image.load('zombie/zombie_walk5_u.png').convert_alpha(),
                       pygame.image.load('zombie/zombie_walk5_u.png').convert_alpha(),
                       pygame.image.load('zombie/zombie_walk6_u.png').convert_alpha(),
                       pygame.image.load('zombie/zombie_walk6_u.png').convert_alpha(),
                       pygame.image.load('zombie/zombie_walk6_u.png').convert_alpha(),
                       pygame.image.load('zombie/zombie_walk6_u.png').convert_alpha(),
                       pygame.image.load('zombie/zombie_walk6_u.png').convert_alpha(),
                       ]
zombie_animation_down = [pygame.image.load('zombie/zombie_walk1_d.png').convert_alpha(),
                         pygame.image.load('zombie/zombie_walk1_d.png').convert_alpha(),
                         pygame.image.load('zombie/zombie_walk1_d.png').convert_alpha(),
                         pygame.image.load('zombie/zombie_walk1_d.png').convert_alpha(),
                         pygame.image.load('zombie/zombie_walk1_d.png').convert_alpha(),
                         pygame.image.load('zombie/zombie_walk2_d.png').convert_alpha(),
                         pygame.image.load('zombie/zombie_walk2_d.png').convert_alpha(),
                         pygame.image.load('zombie/zombie_walk2_d.png').convert_alpha(),
                         pygame.image.load('zombie/zombie_walk2_d.png').convert_alpha(),
                         pygame.image.load('zombie/zombie_walk2_d.png').convert_alpha(),
                         pygame.image.load('zombie/zombie_walk3_d.png').convert_alpha(),
                         pygame.image.load('zombie/zombie_walk3_d.png').convert_alpha(),
                         pygame.image.load('zombie/zombie_walk3_d.png').convert_alpha(),
                         pygame.image.load('zombie/zombie_walk3_d.png').convert_alpha(),
                         pygame.image.load('zombie/zombie_walk3_d.png').convert_alpha(),
                         pygame.image.load('zombie/zombie_walk4_d.png').convert_alpha(),
                         pygame.image.load('zombie/zombie_walk4_d.png').convert_alpha(),
                         pygame.image.load('zombie/zombie_walk4_d.png').convert_alpha(),
                         pygame.image.load('zombie/zombie_walk4_d.png').convert_alpha(),
                         pygame.image.load('zombie/zombie_walk4_d.png').convert_alpha(),
                         pygame.image.load('zombie/zombie_walk5_d.png').convert_alpha(),
                         pygame.image.load('zombie/zombie_walk5_d.png').convert_alpha(),
                         pygame.image.load('zombie/zombie_walk5_d.png').convert_alpha(),
                         pygame.image.load('zombie/zombie_walk5_d.png').convert_alpha(),
                         pygame.image.load('zombie/zombie_walk5_d.png').convert_alpha(),
                         pygame.image.load('zombie/zombie_walk6_d.png').convert_alpha(),
                         pygame.image.load('zombie/zombie_walk6_d.png').convert_alpha(),
                         pygame.image.load('zombie/zombie_walk6_d.png').convert_alpha(),
                         pygame.image.load('zombie/zombie_walk6_d.png').convert_alpha(),
                         pygame.image.load('zombie/zombie_walk6_d.png').convert_alpha(),
                         ]
zombie_animation_left = [pygame.image.load('zombie/zombie_walk1_l.png').convert_alpha(),
                         pygame.image.load('zombie/zombie_walk1_l.png').convert_alpha(),
                         pygame.image.load('zombie/zombie_walk1_l.png').convert_alpha(),
                         pygame.image.load('zombie/zombie_walk1_l.png').convert_alpha(),
                         pygame.image.load('zombie/zombie_walk1_l.png').convert_alpha(),
                         pygame.image.load('zombie/zombie_walk2_l.png').convert_alpha(),
                         pygame.image.load('zombie/zombie_walk2_l.png').convert_alpha(),
                         pygame.image.load('zombie/zombie_walk2_l.png').convert_alpha(),
                         pygame.image.load('zombie/zombie_walk2_l.png').convert_alpha(),
                         pygame.image.load('zombie/zombie_walk2_l.png').convert_alpha(),
                         pygame.image.load('zombie/zombie_walk3_l.png').convert_alpha(),
                         pygame.image.load('zombie/zombie_walk3_l.png').convert_alpha(),
                         pygame.image.load('zombie/zombie_walk3_l.png').convert_alpha(),
                         pygame.image.load('zombie/zombie_walk3_l.png').convert_alpha(),
                         pygame.image.load('zombie/zombie_walk3_l.png').convert_alpha(),
                         pygame.image.load('zombie/zombie_walk4_l.png').convert_alpha(),
                         pygame.image.load('zombie/zombie_walk4_l.png').convert_alpha(),
                         pygame.image.load('zombie/zombie_walk4_l.png').convert_alpha(),
                         pygame.image.load('zombie/zombie_walk4_l.png').convert_alpha(),
                         pygame.image.load('zombie/zombie_walk4_l.png').convert_alpha(),
                         pygame.image.load('zombie/zombie_walk5_l.png').convert_alpha(),
                         pygame.image.load('zombie/zombie_walk5_l.png').convert_alpha(),
                         pygame.image.load('zombie/zombie_walk5_l.png').convert_alpha(),
                         pygame.image.load('zombie/zombie_walk5_l.png').convert_alpha(),
                         pygame.image.load('zombie/zombie_walk5_l.png').convert_alpha(),
                         pygame.image.load('zombie/zombie_walk6_l.png').convert_alpha(),
                         pygame.image.load('zombie/zombie_walk6_l.png').convert_alpha(),
                         pygame.image.load('zombie/zombie_walk6_l.png').convert_alpha(),
                         pygame.image.load('zombie/zombie_walk6_l.png').convert_alpha(),
                         pygame.image.load('zombie/zombie_walk6_l.png').convert_alpha(),
                         ]
zombie_animation_right = [pygame.image.load('zombie/zombie_walk1_r.png').convert_alpha(),
                          pygame.image.load('zombie/zombie_walk1_r.png').convert_alpha(),
                          pygame.image.load('zombie/zombie_walk1_r.png').convert_alpha(),
                          pygame.image.load('zombie/zombie_walk1_r.png').convert_alpha(),
                          pygame.image.load('zombie/zombie_walk1_r.png').convert_alpha(),
                          pygame.image.load('zombie/zombie_walk2_r.png').convert_alpha(),
                          pygame.image.load('zombie/zombie_walk2_r.png').convert_alpha(),
                          pygame.image.load('zombie/zombie_walk2_r.png').convert_alpha(),
                          pygame.image.load('zombie/zombie_walk2_r.png').convert_alpha(),
                          pygame.image.load('zombie/zombie_walk2_r.png').convert_alpha(),
                          pygame.image.load('zombie/zombie_walk3_r.png').convert_alpha(),
                          pygame.image.load('zombie/zombie_walk3_r.png').convert_alpha(),
                          pygame.image.load('zombie/zombie_walk3_r.png').convert_alpha(),
                          pygame.image.load('zombie/zombie_walk3_r.png').convert_alpha(),
                          pygame.image.load('zombie/zombie_walk3_r.png').convert_alpha(),
                          pygame.image.load('zombie/zombie_walk4_r.png').convert_alpha(),
                          pygame.image.load('zombie/zombie_walk4_r.png').convert_alpha(),
                          pygame.image.load('zombie/zombie_walk4_r.png').convert_alpha(),
                          pygame.image.load('zombie/zombie_walk4_r.png').convert_alpha(),
                          pygame.image.load('zombie/zombie_walk4_r.png').convert_alpha(),
                          pygame.image.load('zombie/zombie_walk5_r.png').convert_alpha(),
                          pygame.image.load('zombie/zombie_walk5_r.png').convert_alpha(),
                          pygame.image.load('zombie/zombie_walk5_r.png').convert_alpha(),
                          pygame.image.load('zombie/zombie_walk5_r.png').convert_alpha(),
                          pygame.image.load('zombie/zombie_walk5_r.png').convert_alpha(),
                          pygame.image.load('zombie/zombie_walk6_r.png').convert_alpha(),
                          pygame.image.load('zombie/zombie_walk6_r.png').convert_alpha(),
                          pygame.image.load('zombie/zombie_walk6_r.png').convert_alpha(),
                          pygame.image.load('zombie/zombie_walk6_r.png').convert_alpha(),
                          pygame.image.load('zombie/zombie_walk6_r.png').convert_alpha(),
                          ]
frame_count = 0


def draw_zombie(z, p):
    global frame_count

    frame_count += 1
    if frame_count + 1 > 30:  # 30 frames to cycle through
        frame_count = 0

    #  move zombie towards player position
    if z.get_enemy_x() < p.get_player_x():  # compare zombie pos x to player pos x
        z.enemy_x_change = z.move_speed  # if zombie x is less than player x, add zombie x
        # draw zombie (animated) in the direction depending on where it needs to go
        screen.blit(zombie_animation_right[frame_count], (z.enemy_x, z.enemy_y))

    elif z.get_enemy_x() > p.get_player_x():
        z.enemy_x_change = -z.move_speed
        screen.blit(zombie_animation_left[frame_count], (z.enemy_x, z.enemy_y))

    elif z.get_enemy_y() < p.get_player_y():
        z.enemy_y_change = z.move_speed
        screen.blit(zombie_animation_down[frame_count], (z.enemy_x, z.enemy_y))

    elif z.get_enemy_y() > p.get_player_y():
        z.enemy_y_change = -z.move_speed
        screen.blit(zombie_animation_up[frame_count], (z.enemy_x, z.enemy_y))

    #  stop moving zombie
    # TODO: fix zombie vibrating (sometimes vanishing) when reaching player position
    if z.get_enemy_x() == p.get_player_x():
        z.enemy_x_change = 0
    if z.get_enemy_y() == p.get_player_y():
        z.enemy_y_change = 0

    z.enemy_y += z.enemy_y_change
    z.enemy_x += z.enemy_x_change

    # TODO: make it so zombies can't move through walls

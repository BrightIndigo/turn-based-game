import pygame
import sys
import random

pygame.init()

screen_width = 1000
screen_height = 1000
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
running = True
dt = 0
brick_wall = pygame.image.load("background.jpg")
font = pygame.font.Font(None, 36)
grid_unit = screen_height / 10

# borders
border_top = pygame.Rect(0, 0, screen_width, 5)
border_left = pygame.Rect(0, 0, 5, screen_height)
border_right = pygame.Rect(995, 0, 5, screen_height)
border_bottom = pygame.Rect(0, 995, screen_width, 5)

# grid
wall1 = pygame.Rect(0, grid_unit, screen_width, 5)
wall2 = pygame.Rect(0, grid_unit * 2, screen_width, 5)
wall3 = pygame.Rect(0, grid_unit * 3, screen_width, 5)
wall4 = pygame.Rect(0, grid_unit * 4, screen_width, 5)
wall5 = pygame.Rect(0, grid_unit * 5, screen_width, 5)
wall6 = pygame.Rect(0, grid_unit * 6, screen_width, 5)
wall7 = pygame.Rect(0, grid_unit * 7, screen_width, 5)
wall8 = pygame.Rect(0, grid_unit * 8, screen_width, 5)
wall9 = pygame.Rect(0, grid_unit * 9, screen_width, 5)
wall10 = pygame.Rect(grid_unit, 0, 5, screen_height)
wall11 = pygame.Rect(grid_unit * 2, 0, 5, screen_height)
wall12 = pygame.Rect(grid_unit * 3, 0, 5, screen_height)
wall13 = pygame.Rect(grid_unit * 4, 0, 5, screen_height)
wall14 = pygame.Rect(grid_unit * 5, 0, 5, screen_height)
wall15 = pygame.Rect(grid_unit * 6, 0, 5, screen_height)
wall16 = pygame.Rect(grid_unit * 7, 0, 5, screen_height)
wall17 = pygame.Rect(grid_unit * 8, 0, 5, screen_height)
wall18 = pygame.Rect(grid_unit * 9, 0, 5, screen_height)


# player
class Player():
    def __init__(self):
        self.points = 0
        self.hp = 100
        self.row = 1
        self.col = 1
        self.unknown_area_move_r = 25
        self.unknown_area_move_d = 25


Player = Player()

player_width = 50
player_height = 50
player_x = (grid_unit / 2) - (player_width / 2)
player_y = (grid_unit / 2) - (player_height / 2)
player = pygame.Rect(player_x, player_y, player_width, player_height)
player_turn = True

# area to explore
area_a = 100 + 5
area_x = ((grid_unit / 2) - (area_a / 2)) + 2.5
area_y = ((grid_unit / 2) - (area_a / 2)) + 2.5

# first row
unknown_area1 = pygame.Rect(area_x + 100, area_y, area_a, area_a)
unknown_area2 = pygame.Rect(area_x + 200, area_y, area_a, area_a)
unknown_area3 = pygame.Rect(area_x + 300, area_y, area_a, area_a)
unknown_area4 = pygame.Rect(area_x + 400, area_y, area_a, area_a)
unknown_area5 = pygame.Rect(area_x + 500, area_y, area_a, area_a)
unknown_area6 = pygame.Rect(area_x + 600, area_y, area_a, area_a)
unknown_area7 = pygame.Rect(area_x + 700, area_y, area_a, area_a)
unknown_area8 = pygame.Rect(area_x + 800, area_y, area_a, area_a)
unknown_area9 = pygame.Rect(area_x + 900, area_y, area_a, area_a)
first_unknown_row = [unknown_area1, unknown_area2, unknown_area3, unknown_area4, unknown_area5, unknown_area6,
                     unknown_area7, unknown_area8, unknown_area9]

# second row
r2_unknown_area1 = pygame.Rect(area_x, area_y + 100, area_a, area_a)
r2_unknown_area2 = pygame.Rect(area_x + 100, area_y + 100, area_a, area_a)
r2_unknown_area3 = pygame.Rect(area_x + 200, area_y + 100, area_a, area_a)
r2_unknown_area4 = pygame.Rect(area_x + 300, area_y + 100, area_a, area_a)
r2_unknown_area5 = pygame.Rect(area_x + 400, area_y + 100, area_a, area_a)
r2_unknown_area6 = pygame.Rect(area_x + 500, area_y + 100, area_a, area_a)
r2_unknown_area7 = pygame.Rect(area_x + 600, area_y + 100, area_a, area_a)
r2_unknown_area8 = pygame.Rect(area_x + 700, area_y + 100, area_a, area_a)
r2_unknown_area9 = pygame.Rect(area_x + 800, area_y + 100, area_a, area_a)
r2_unknown_area10 = pygame.Rect(area_x + 900, area_y + 100, area_a, area_a)
r2_unknown_row = [r2_unknown_area1, r2_unknown_area2, r2_unknown_area3, r2_unknown_area4, r2_unknown_area5,
                  r2_unknown_area6, r2_unknown_area7, r2_unknown_area8, r2_unknown_area9, r2_unknown_area10]
# third row
r3_unknown_area1 = pygame.Rect(area_x, area_y + 200, area_a, area_a)
r3_unknown_area2 = pygame.Rect(area_x + 100, area_y + 200, area_a, area_a)
r3_unknown_area3 = pygame.Rect(area_x + 200, area_y + 200, area_a, area_a)
r3_unknown_area4 = pygame.Rect(area_x + 300, area_y + 200, area_a, area_a)
r3_unknown_area5 = pygame.Rect(area_x + 400, area_y + 200, area_a, area_a)
r3_unknown_area6 = pygame.Rect(area_x + 500, area_y + 200, area_a, area_a)
r3_unknown_area7 = pygame.Rect(area_x + 600, area_y + 200, area_a, area_a)
r3_unknown_area8 = pygame.Rect(area_x + 700, area_y + 200, area_a, area_a)
r3_unknown_area9 = pygame.Rect(area_x + 800, area_y + 200, area_a, area_a)
r3_unknown_area10 = pygame.Rect(area_x + 900, area_y + 200, area_a, area_a)
r3_unknown_row = [r3_unknown_area1, r3_unknown_area2, r3_unknown_area3, r3_unknown_area4, r3_unknown_area5,
                  r3_unknown_area6, r3_unknown_area7, r3_unknown_area8, r3_unknown_area9, r3_unknown_area10]
# fourth row
r4_unknown_area1 = pygame.Rect(area_x, area_y + 300, area_a, area_a)
r4_unknown_area2 = pygame.Rect(area_x + 100, area_y + 300, area_a, area_a)
r4_unknown_area3 = pygame.Rect(area_x + 200, area_y + 300, area_a, area_a)
r4_unknown_area4 = pygame.Rect(area_x + 300, area_y + 300, area_a, area_a)
r4_unknown_area5 = pygame.Rect(area_x + 400, area_y + 300, area_a, area_a)
r4_unknown_area6 = pygame.Rect(area_x + 500, area_y + 300, area_a, area_a)
r4_unknown_area7 = pygame.Rect(area_x + 600, area_y + 300, area_a, area_a)
r4_unknown_area8 = pygame.Rect(area_x + 700, area_y + 300, area_a, area_a)
r4_unknown_area9 = pygame.Rect(area_x + 800, area_y + 300, area_a, area_a)
r4_unknown_area10 = pygame.Rect(area_x + 900, area_y + 300, area_a, area_a)
r4_unknown_row = [r4_unknown_area1, r4_unknown_area2, r4_unknown_area3, r4_unknown_area4, r4_unknown_area5,
                  r4_unknown_area6, r4_unknown_area7, r4_unknown_area8, r4_unknown_area9, r4_unknown_area10]

r5_unknown_area1 = pygame.Rect(area_x, area_y + 400, area_a, area_a)
r5_unknown_area2 = pygame.Rect(area_x + 100, area_y + 400, area_a, area_a)
r5_unknown_area3 = pygame.Rect(area_x + 200, area_y + 400, area_a, area_a)
r5_unknown_area4 = pygame.Rect(area_x + 300, area_y + 400, area_a, area_a)
r5_unknown_area5 = pygame.Rect(area_x + 400, area_y + 400, area_a, area_a)
r5_unknown_area6 = pygame.Rect(area_x + 500, area_y + 400, area_a, area_a)
r5_unknown_area7 = pygame.Rect(area_x + 600, area_y + 400, area_a, area_a)
r5_unknown_area8 = pygame.Rect(area_x + 700, area_y + 400, area_a, area_a)
r5_unknown_area9 = pygame.Rect(area_x + 800, area_y + 400, area_a, area_a)
r5_unknown_area10 = pygame.Rect(area_x + 900, area_y + 400, area_a, area_a)
r5_unknown_row = [r5_unknown_area1, r5_unknown_area2, r5_unknown_area3, r5_unknown_area4, r5_unknown_area5,
                  r5_unknown_area6, r5_unknown_area7, r5_unknown_area8, r5_unknown_area9, r5_unknown_area10]

r6_unknown_area1 = pygame.Rect(area_x, area_y + 500, area_a, area_a)
r6_unknown_area2 = pygame.Rect(area_x + 100, area_y + 500, area_a, area_a)
r6_unknown_area3 = pygame.Rect(area_x + 200, area_y + 500, area_a, area_a)
r6_unknown_area4 = pygame.Rect(area_x + 300, area_y + 500, area_a, area_a)
r6_unknown_area5 = pygame.Rect(area_x + 400, area_y + 500, area_a, area_a)
r6_unknown_area6 = pygame.Rect(area_x + 500, area_y + 500, area_a, area_a)
r6_unknown_area7 = pygame.Rect(area_x + 600, area_y + 500, area_a, area_a)
r6_unknown_area8 = pygame.Rect(area_x + 700, area_y + 500, area_a, area_a)
r6_unknown_area9 = pygame.Rect(area_x + 800, area_y + 500, area_a, area_a)
r6_unknown_area10 = pygame.Rect(area_x + 900, area_y + 500, area_a, area_a)
r6_unknown_row = [r6_unknown_area1, r6_unknown_area2, r6_unknown_area3, r6_unknown_area4, r6_unknown_area5,
                  r6_unknown_area6, r6_unknown_area7, r6_unknown_area8, r6_unknown_area9, r6_unknown_area10]

r7_unknown_area1 = pygame.Rect(area_x, area_y + 600, area_a, area_a)
r7_unknown_area2 = pygame.Rect(area_x + 100, area_y + 600, area_a, area_a)
r7_unknown_area3 = pygame.Rect(area_x + 200, area_y + 600, area_a, area_a)
r7_unknown_area4 = pygame.Rect(area_x + 300, area_y + 600, area_a, area_a)
r7_unknown_area5 = pygame.Rect(area_x + 400, area_y + 600, area_a, area_a)
r7_unknown_area6 = pygame.Rect(area_x + 500, area_y + 600, area_a, area_a)
r7_unknown_area7 = pygame.Rect(area_x + 600, area_y + 600, area_a, area_a)
r7_unknown_area8 = pygame.Rect(area_x + 700, area_y + 600, area_a, area_a)
r7_unknown_area9 = pygame.Rect(area_x + 800, area_y + 600, area_a, area_a)
r7_unknown_area10 = pygame.Rect(area_x + 900, area_y + 600, area_a, area_a)
r7_unknown_row = [r7_unknown_area1, r7_unknown_area2, r7_unknown_area3, r7_unknown_area4, r7_unknown_area5,
                  r7_unknown_area6, r7_unknown_area7, r7_unknown_area8, r7_unknown_area9, r7_unknown_area10]

r8_unknown_area1 = pygame.Rect(area_x, area_y + 700, area_a, area_a)
r8_unknown_area2 = pygame.Rect(area_x + 100, area_y + 700, area_a, area_a)
r8_unknown_area3 = pygame.Rect(area_x + 200, area_y + 700, area_a, area_a)
r8_unknown_area4 = pygame.Rect(area_x + 300, area_y + 700, area_a, area_a)
r8_unknown_area5 = pygame.Rect(area_x + 400, area_y + 700, area_a, area_a)
r8_unknown_area6 = pygame.Rect(area_x + 500, area_y + 700, area_a, area_a)
r8_unknown_area7 = pygame.Rect(area_x + 600, area_y + 700, area_a, area_a)
r8_unknown_area8 = pygame.Rect(area_x + 700, area_y + 700, area_a, area_a)
r8_unknown_area9 = pygame.Rect(area_x + 800, area_y + 700, area_a, area_a)
r8_unknown_area10 = pygame.Rect(area_x + 900, area_y + 700, area_a, area_a)
r8_unknown_row = [r8_unknown_area1, r8_unknown_area2, r8_unknown_area3, r8_unknown_area4, r8_unknown_area5,
                  r8_unknown_area6, r8_unknown_area7, r8_unknown_area8, r8_unknown_area9, r8_unknown_area10]

r9_unknown_area1 = pygame.Rect(area_x, area_y + 800, area_a, area_a)
r9_unknown_area2 = pygame.Rect(area_x + 100, area_y + 800, area_a, area_a)
r9_unknown_area3 = pygame.Rect(area_x + 200, area_y + 800, area_a, area_a)
r9_unknown_area4 = pygame.Rect(area_x + 300, area_y + 800, area_a, area_a)
r9_unknown_area5 = pygame.Rect(area_x + 400, area_y + 800, area_a, area_a)
r9_unknown_area6 = pygame.Rect(area_x + 500, area_y + 800, area_a, area_a)
r9_unknown_area7 = pygame.Rect(area_x + 600, area_y + 800, area_a, area_a)
r9_unknown_area8 = pygame.Rect(area_x + 700, area_y + 800, area_a, area_a)
r9_unknown_area9 = pygame.Rect(area_x + 800, area_y + 800, area_a, area_a)
r9_unknown_area10 = pygame.Rect(area_x + 900, area_y + 800, area_a, area_a)
r9_unknown_row = [r9_unknown_area1, r9_unknown_area2, r9_unknown_area3, r9_unknown_area4, r9_unknown_area5,
                  r9_unknown_area6, r9_unknown_area7, r9_unknown_area8, r9_unknown_area9, r9_unknown_area10]

r10_unknown_area1 = pygame.Rect(area_x, area_y + 900, area_a, area_a)
r10_unknown_area2 = pygame.Rect(area_x + 100, area_y + 900, area_a, area_a)
r10_unknown_area3 = pygame.Rect(area_x + 200, area_y + 900, area_a, area_a)
r10_unknown_area4 = pygame.Rect(area_x + 300, area_y + 900, area_a, area_a)
r10_unknown_area5 = pygame.Rect(area_x + 400, area_y + 900, area_a, area_a)
r10_unknown_area6 = pygame.Rect(area_x + 500, area_y + 900, area_a, area_a)
r10_unknown_area7 = pygame.Rect(area_x + 600, area_y + 900, area_a, area_a)
r10_unknown_area8 = pygame.Rect(area_x + 700, area_y + 900, area_a, area_a)
r10_unknown_area9 = pygame.Rect(area_x + 800, area_y + 900, area_a, area_a)
r10_unknown_area10 = pygame.Rect(area_x + 900, area_y + 900, area_a, area_a)
r10_unknown_row = [r10_unknown_area1, r10_unknown_area2, r10_unknown_area3, r10_unknown_area4, r10_unknown_area5,
                   r10_unknown_area6, r10_unknown_area7, r10_unknown_area8, r10_unknown_area9, r10_unknown_area10]

all_map = first_unknown_row+r2_unknown_row+r3_unknown_row+r4_unknown_row+r5_unknown_row+r6_unknown_row+r7_unknown_row+r8_unknown_row+r9_unknown_row+r10_unknown_row

item_a = 40
item_x = (grid_unit / 2) - (item_a / 2)
item_y = (grid_unit / 2) - (item_a / 2)

rand_1 = random.randint(2, 9)
rand_2 = random.randint(1, 9)

item_pos_x = (100 * rand_1)
item_pos_y = (100 * rand_2)

item_1_x = (item_x + item_pos_x)
item_1_y = (item_y + item_pos_y)

item_1 = pygame.Rect(item_1_x, item_1_y, item_a, item_a)
item_2 = pygame.Rect(item_1_x, item_1_y, item_a, item_a)
item_3 = pygame.Rect(item_1_x, item_1_y, item_a, item_a)
item_4 = pygame.Rect(item_1_x, item_1_y, item_a, item_a)


def computers_turn():
    direction = random.randint(1, 4)
    if direction == 1 and item_1.x < 925:
        item_1.x += 100
    elif direction == 2 and item_1.x > 30:
        item_1.x -= 100
    elif direction == 3 and item_1.y < 925:
        item_1.y += 100
    elif direction == 4 and item_1.y > 30:
        item_1.y -= 100

    direction2 = random.randint(1, 4)
    if direction2 == 1 and item_2.x < 925:
        item_2.x += 100
    elif direction2 == 2 and item_2.x > 30:
        item_2.x -= 100
    elif direction2 == 3 and item_2.y < 925:
        item_2.y += 100
    elif direction2 == 4 and item_2.y > 30:
        item_2.y -= 100

    direction3 = random.randint(1, 4)
    if direction3 == 1 and item_3.x < 925:
        item_3.x += 100
    elif direction3 == 2 and item_3.x > 30:
        item_3.x -= 100
    elif direction3 == 3 and item_3.y < 925:
        item_3.y += 100
    elif direction3 == 4 and item_3.y > 30:
        item_3.y -= 100

    direction4 = random.randint(1, 4)
    if direction4 == 1 and item_4.x < 925:
        item_4.x += 100
    elif direction4 == 2 and item_4.x > 30:
        item_4.x -= 100
    elif direction4 == 3 and item_4.y < 925:
        item_4.y += 100
    elif direction4 == 4 and item_4.y > 30:
        item_4.y -= 100

    player_turn = True


def print_coords():
    pygame.display.set_caption(f"x: {player.x} y: {player.y} row: {Player.row} col: {Player.col}")


def item_1_action():
    Player.item_1()


while running and Player.hp > 0:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(brick_wall, (0, 0))

    if player.colliderect(item_1) or player.colliderect(item_2) or player.colliderect(item_3) or player.colliderect(
            item_4):
        sys.exit()

    if player_turn == True:
        print_coords()
        keys = pygame.key.get_pressed()
        pressed = False

        if keys[pygame.K_UP] and player.y > 25:

            if player.colliderect(unknown_area1 or unknown_area2 or unknown_area3 or unknown_area4 or unknown_area5 or unknown_area6 or unknown_area7 or unknown_area8 or unknown_area9 or r2_unknown_area1 or r2_unknown_area2 or r2_unknown_area3 or r2_unknown_area4 or r2_unknown_area5 or r2_unknown_area6 or r2_unknown_area7 or r2_unknown_area8 or r2_unknown_area9 or r2_unknown_area10 or r3_unknown_area1 or r3_unknown_area2 or r3_unknown_area3 or r3_unknown_area4 or r3_unknown_area5 or r3_unknown_area6 or r3_unknown_area7 or r3_unknown_area8 or r3_unknown_area9 or r3_unknown_area10 or r4_unknown_area1 or r4_unknown_area2 or r4_unknown_area3 or r4_unknown_area4 or r4_unknown_area5 or r4_unknown_area6 or r4_unknown_area7 or r4_unknown_area8 or r4_unknown_area9 or r4_unknown_area10 or r5_unknown_area1 or r5_unknown_area2 or r5_unknown_area3 or r5_unknown_area4 or r5_unknown_area5 or r5_unknown_area6 or r5_unknown_area7 or r5_unknown_area8 or r5_unknown_area9 or r5_unknown_area10 or r6_unknown_area1 or r6_unknown_area2 or r6_unknown_area3 or r6_unknown_area4 or r6_unknown_area5 or r6_unknown_area6 or r6_unknown_area7 or r6_unknown_area8 or r6_unknown_area9 or r6_unknown_area10 or r7_unknown_area1 or r7_unknown_area2 or r7_unknown_area3 or r7_unknown_area4 or r7_unknown_area5 or r7_unknown_area6 or r7_unknown_area7 or r7_unknown_area8 or r7_unknown_area9 or r7_unknown_area10 or r8_unknown_area1 or r8_unknown_area2 or r8_unknown_area3 or r8_unknown_area4 or r8_unknown_area5 or r8_unknown_area6 or r8_unknown_area7 or r8_unknown_area8 or r8_unknown_area9 or r8_unknown_area10 or r9_unknown_area1 or r9_unknown_area2 or r9_unknown_area3 or r9_unknown_area4 or r9_unknown_area5 or r9_unknown_area6 or r9_unknown_area7 or r9_unknown_area8 or r9_unknown_area9 or r9_unknown_area10 or r10_unknown_area1 or r10_unknown_area2 or r10_unknown_area3 or r10_unknown_area4 or r10_unknown_area5 or r10_unknown_area6 or r10_unknown_area7 or r10_unknown_area8 or r10_unknown_area9 or r10_unknown_area10):
                player.y += 100
                Player.row += 1
                pressed = True
            else:
                player.y -= 100
                Player.row -= 1
                pressed = True
        if keys[pygame.K_DOWN] and player.y < 925:

            if player.colliderect(unknown_area1 or unknown_area2 or unknown_area3 or unknown_area4 or unknown_area5 or unknown_area6 or unknown_area7 or unknown_area8 or unknown_area9 or r2_unknown_area1 or r2_unknown_area2 or r2_unknown_area3 or r2_unknown_area4 or r2_unknown_area5 or r2_unknown_area6 or r2_unknown_area7 or r2_unknown_area8 or r2_unknown_area9 or r2_unknown_area10 or r3_unknown_area1 or r3_unknown_area2 or r3_unknown_area3 or r3_unknown_area4 or r3_unknown_area5 or r3_unknown_area6 or r3_unknown_area7 or r3_unknown_area8 or r3_unknown_area9 or r3_unknown_area10 or r4_unknown_area1 or r4_unknown_area2 or r4_unknown_area3 or r4_unknown_area4 or r4_unknown_area5 or r4_unknown_area6 or r4_unknown_area7 or r4_unknown_area8 or r4_unknown_area9 or r4_unknown_area10 or r5_unknown_area1 or r5_unknown_area2 or r5_unknown_area3 or r5_unknown_area4 or r5_unknown_area5 or r5_unknown_area6 or r5_unknown_area7 or r5_unknown_area8 or r5_unknown_area9 or r5_unknown_area10 or r6_unknown_area1 or r6_unknown_area2 or r6_unknown_area3 or r6_unknown_area4 or r6_unknown_area5 or r6_unknown_area6 or r6_unknown_area7 or r6_unknown_area8 or r6_unknown_area9 or r6_unknown_area10 or r7_unknown_area1 or r7_unknown_area2 or r7_unknown_area3 or r7_unknown_area4 or r7_unknown_area5 or r7_unknown_area6 or r7_unknown_area7 or r7_unknown_area8 or r7_unknown_area9 or r7_unknown_area10 or r8_unknown_area1 or r8_unknown_area2 or r8_unknown_area3 or r8_unknown_area4 or r8_unknown_area5 or r8_unknown_area6 or r8_unknown_area7 or r8_unknown_area8 or r8_unknown_area9 or r8_unknown_area10 or r9_unknown_area1 or r9_unknown_area2 or r9_unknown_area3 or r9_unknown_area4 or r9_unknown_area5 or r9_unknown_area6 or r9_unknown_area7 or r9_unknown_area8 or r9_unknown_area9 or r9_unknown_area10 or r10_unknown_area1 or r10_unknown_area2 or r10_unknown_area3 or r10_unknown_area4 or r10_unknown_area5 or r10_unknown_area6 or r10_unknown_area7 or r10_unknown_area8 or r10_unknown_area9 or r10_unknown_area10):
                player.y -= 100
                Player.row -= 1
                pressed = True
            else:
                player.y += 100
                Player.row += 1
                pressed = True
        if keys[pygame.K_LEFT] and player.x > 25:
            if player.colliderect(unknown_area1 or unknown_area2 or unknown_area3 or unknown_area4 or unknown_area5 or unknown_area6 or unknown_area7 or unknown_area8 or unknown_area9 or r2_unknown_area1 or r2_unknown_area2 or r2_unknown_area3 or r2_unknown_area4 or r2_unknown_area5 or r2_unknown_area6 or r2_unknown_area7 or r2_unknown_area8 or r2_unknown_area9 or r2_unknown_area10 or r3_unknown_area1 or r3_unknown_area2 or r3_unknown_area3 or r3_unknown_area4 or r3_unknown_area5 or r3_unknown_area6 or r3_unknown_area7 or r3_unknown_area8 or r3_unknown_area9 or r3_unknown_area10 or r4_unknown_area1 or r4_unknown_area2 or r4_unknown_area3 or r4_unknown_area4 or r4_unknown_area5 or r4_unknown_area6 or r4_unknown_area7 or r4_unknown_area8 or r4_unknown_area9 or r4_unknown_area10 or r5_unknown_area1 or r5_unknown_area2 or r5_unknown_area3 or r5_unknown_area4 or r5_unknown_area5 or r5_unknown_area6 or r5_unknown_area7 or r5_unknown_area8 or r5_unknown_area9 or r5_unknown_area10 or r6_unknown_area1 or r6_unknown_area2 or r6_unknown_area3 or r6_unknown_area4 or r6_unknown_area5 or r6_unknown_area6 or r6_unknown_area7 or r6_unknown_area8 or r6_unknown_area9 or r6_unknown_area10 or r7_unknown_area1 or r7_unknown_area2 or r7_unknown_area3 or r7_unknown_area4 or r7_unknown_area5 or r7_unknown_area6 or r7_unknown_area7 or r7_unknown_area8 or r7_unknown_area9 or r7_unknown_area10 or r8_unknown_area1 or r8_unknown_area2 or r8_unknown_area3 or r8_unknown_area4 or r8_unknown_area5 or r8_unknown_area6 or r8_unknown_area7 or r8_unknown_area8 or r8_unknown_area9 or r8_unknown_area10 or r9_unknown_area1 or r9_unknown_area2 or r9_unknown_area3 or r9_unknown_area4 or r9_unknown_area5 or r9_unknown_area6 or r9_unknown_area7 or r9_unknown_area8 or r9_unknown_area9 or r9_unknown_area10 or r10_unknown_area1 or r10_unknown_area2 or r10_unknown_area3 or r10_unknown_area4 or r10_unknown_area5 or r10_unknown_area6 or r10_unknown_area7 or r10_unknown_area8 or r10_unknown_area9 or r10_unknown_area10):
                player.x += 100
                Player.col += 1
                pressed = True
            else:
                player.x -= 100
                Player.col -= 1
                pressed = True
        if keys[pygame.K_RIGHT] and player.x < 925:
            if player.colliderect(unknown_area1 or unknown_area2 or unknown_area3 or unknown_area4 or unknown_area5 or unknown_area6 or unknown_area7 or unknown_area8 or unknown_area9 or r2_unknown_area1 or r2_unknown_area2 or r2_unknown_area3 or r2_unknown_area4 or r2_unknown_area5 or r2_unknown_area6 or r2_unknown_area7 or r2_unknown_area8 or r2_unknown_area9 or r2_unknown_area10 or r3_unknown_area1 or r3_unknown_area2 or r3_unknown_area3 or r3_unknown_area4 or r3_unknown_area5 or r3_unknown_area6 or r3_unknown_area7 or r3_unknown_area8 or r3_unknown_area9 or r3_unknown_area10 or r4_unknown_area1 or r4_unknown_area2 or r4_unknown_area3 or r4_unknown_area4 or r4_unknown_area5 or r4_unknown_area6 or r4_unknown_area7 or r4_unknown_area8 or r4_unknown_area9 or r4_unknown_area10 or r5_unknown_area1 or r5_unknown_area2 or r5_unknown_area3 or r5_unknown_area4 or r5_unknown_area5 or r5_unknown_area6 or r5_unknown_area7 or r5_unknown_area8 or r5_unknown_area9 or r5_unknown_area10 or r6_unknown_area1 or r6_unknown_area2 or r6_unknown_area3 or r6_unknown_area4 or r6_unknown_area5 or r6_unknown_area6 or r6_unknown_area7 or r6_unknown_area8 or r6_unknown_area9 or r6_unknown_area10 or r7_unknown_area1 or r7_unknown_area2 or r7_unknown_area3 or r7_unknown_area4 or r7_unknown_area5 or r7_unknown_area6 or r7_unknown_area7 or r7_unknown_area8 or r7_unknown_area9 or r7_unknown_area10 or r8_unknown_area1 or r8_unknown_area2 or r8_unknown_area3 or r8_unknown_area4 or r8_unknown_area5 or r8_unknown_area6 or r8_unknown_area7 or r8_unknown_area8 or r8_unknown_area9 or r8_unknown_area10 or r9_unknown_area1 or r9_unknown_area2 or r9_unknown_area3 or r9_unknown_area4 or r9_unknown_area5 or r9_unknown_area6 or r9_unknown_area7 or r9_unknown_area8 or r9_unknown_area9 or r9_unknown_area10 or r10_unknown_area1 or r10_unknown_area2 or r10_unknown_area3 or r10_unknown_area4 or r10_unknown_area5 or r10_unknown_area6 or r10_unknown_area7 or r10_unknown_area8 or r10_unknown_area9 or r10_unknown_area10):
                player.x -= 100
                Player.col -= 1
                pressed = True
            else:
                player.x += 100
                Player.col += 1
                pressed = True
        if keys[pygame.K_SPACE]:
            if Player.row == 1 and Player.col == 1:
                first_unknown_row[Player.col - 1] = pygame.Rect(0, 0, 0, 0)
                r2_unknown_row[Player.col - 1] = pygame.Rect(0, 0, 0, 0)
                r2_unknown_row[Player.col] = pygame.Rect(0, 0, 0, 0)
                Player.unknown_area_move_r += 105
                Player.unknown_area_move_d += 105
            elif Player.row == 2 and Player.col == 1:
                r2_unknown_row[Player.col] = pygame.Rect(0, 0, 0, 0)
                r3_unknown_row[Player.col - 1] = pygame.Rect(0, 0, 0, 0)
                r3_unknown_row[Player.col] = pygame.Rect(0, 0, 0, 0)
                Player.unknown_area_move_d += 105
            elif Player.row == 3 and Player.col == 1:
                r4_unknown_row[Player.col - 1] = pygame.Rect(0, 0, 0, 0)
                r4_unknown_row[Player.col] = pygame.Rect(0, 0, 0, 0)
                Player.unknown_area_move_d += 105
            elif Player.row == 4 and Player.col == 1:
                r5_unknown_row[Player.col - 1] = pygame.Rect(0, 0, 0, 0)
                r5_unknown_row[Player.col] = pygame.Rect(0, 0, 0, 0)
                Player.unknown_area_move_d += 105
            elif Player.row == 5 and Player.col == 1:
                r6_unknown_row[Player.col - 1] = pygame.Rect(0, 0, 0, 0)
                r6_unknown_row[Player.col] = pygame.Rect(0, 0, 0, 0)
                Player.unknown_area_move_d += 105
            elif Player.row == 6 and Player.col == 1:
                r7_unknown_row[Player.col - 1] = pygame.Rect(0, 0, 0, 0)
                r7_unknown_row[Player.col] = pygame.Rect(0, 0, 0, 0)
                Player.unknown_area_move_d += 105
            elif Player.row == 7 and Player.col == 1:
                r8_unknown_row[Player.col - 1] = pygame.Rect(0, 0, 0, 0)
                r8_unknown_row[Player.col] = pygame.Rect(0, 0, 0, 0)
                Player.unknown_area_move_d += 105
            elif Player.row == 8 and Player.col == 1:
                r9_unknown_row[Player.col - 1] = pygame.Rect(0, 0, 0, 0)
                r9_unknown_row[Player.col] = pygame.Rect(0, 0, 0, 0)
                Player.unknown_area_move_d += 105
            elif Player.row == 9 and Player.col == 1:
                r10_unknown_row[Player.col - 1] = pygame.Rect(0, 0, 0, 0)
                r10_unknown_row[Player.col] = pygame.Rect(0, 0, 0, 0)
                Player.unknown_area_move_d += 105
            elif Player.row == 1 and Player.col == 2:
                first_unknown_row[1] = pygame.Rect(0, 0, 0, 0)
                Player.unknown_area_move_r += 105
                r2_unknown_row[1] = pygame.Rect(0, 0, 0, 0)
            pressed = True

        if pressed == True:
            player_turn = False

    elif player_turn == False:
        computers_turn()

        player_turn = True



    pygame.draw.rect(screen, (200, 200, 200), border_top)
    pygame.draw.rect(screen, (200, 200, 200), border_left)
    pygame.draw.rect(screen, (200, 200, 200), border_right)
    pygame.draw.rect(screen, (200, 200, 200), border_bottom)

    pygame.draw.rect(screen, "black", wall1)
    pygame.draw.rect(screen, "black", wall2)
    pygame.draw.rect(screen, "black", wall3)
    pygame.draw.rect(screen, "black", wall4)
    pygame.draw.rect(screen, "black", wall5)
    pygame.draw.rect(screen, "black", wall6)
    pygame.draw.rect(screen, "black", wall7)
    pygame.draw.rect(screen, "black", wall8)
    pygame.draw.rect(screen, "black", wall9)
    pygame.draw.rect(screen, "black", wall10)
    pygame.draw.rect(screen, "black", wall11)
    pygame.draw.rect(screen, "black", wall12)
    pygame.draw.rect(screen, "black", wall13)
    pygame.draw.rect(screen, "black", wall14)
    pygame.draw.rect(screen, "black", wall15)
    pygame.draw.rect(screen, "black", wall16)
    pygame.draw.rect(screen, "black", wall17)
    pygame.draw.rect(screen, "black", wall18)

    for i in first_unknown_row:
        pygame.draw.rect(screen, "black", i)

    for i in range(0, 10):
        pygame.draw.rect(screen, "black", r2_unknown_row[i])

    for i in range(0, 10):
        pygame.draw.rect(screen, "black", r3_unknown_row[i])

    for i in range(0, 10):
        pygame.draw.rect(screen, "black", r4_unknown_row[i])

    for i in range(0, 10):
        pygame.draw.rect(screen, "black", r5_unknown_row[i])

    for i in range(0, 10):
        pygame.draw.rect(screen, "black", r6_unknown_row[i])

    for i in range(0, 10):
        pygame.draw.rect(screen, "black", r7_unknown_row[i])

    for i in range(0, 10):
        pygame.draw.rect(screen, "black", r8_unknown_row[i])

    for i in range(0, 10):
        pygame.draw.rect(screen, "black", r9_unknown_row[i])

    for i in range(0, 10):
        pygame.draw.rect(screen, "black", r10_unknown_row[i])

    pygame.draw.rect(screen, (100, 255, 100), player)

    draw_item_1 = pygame.draw.rect(screen, "red", item_1)
    draw_item_2 = pygame.draw.rect(screen, "red", item_2)
    draw_item_3 = pygame.draw.rect(screen, "red", item_3)
    draw_item_4 = pygame.draw.rect(screen, "red", item_4)

    pygame.display.flip()
    dt = clock.tick(30) / 1000

pygame.quit()
sys.exit()
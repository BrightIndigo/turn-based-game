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
brick_wall = pygame.image.load("brick_wall.png")
font = pygame.font.Font(None, 36)
grid_unit = screen_height // 10

#borders
border_top = pygame.Rect(0, 0, screen_width, 5)
border_left = pygame.Rect(0, 0, 5, screen_height)
border_right = pygame.Rect(995, 0, 5, screen_height)
border_bottom = pygame.Rect(0, 995, screen_width, 5)

#grid
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

#player
player_width = 50
player_height = 50
player_x = (grid_unit / 2)-(player_width/2)
player_y = (grid_unit / 2)-(player_height/2)
player = pygame.Rect(player_x, player_y, player_width, player_height)
player_turn = True

#area to explore
area_a = 100
area_x = ((grid_unit / 2)-(area_a/2))
area_y = ((grid_unit / 2)-(area_a/2))
#first row
unknown_area1 = pygame.Rect(area_x+100, area_y, area_a, area_a)
unknown_area2 = pygame.Rect(area_x+200, area_y, area_a, area_a)
unknown_area3 = pygame.Rect(area_x+300, area_y, area_a, area_a)
unknown_area4 = pygame.Rect(area_x+400, area_y, area_a, area_a)
unknown_area5 = pygame.Rect(area_x+500, area_y, area_a, area_a)
unknown_area6 = pygame.Rect(area_x+600, area_y, area_a, area_a)
unknown_area7 = pygame.Rect(area_x+700, area_y, area_a, area_a)
unknown_area8 = pygame.Rect(area_x+800, area_y, area_a, area_a)
unknown_area9 = pygame.Rect(area_x+900, area_y, area_a, area_a)

#second row
r2_unknown_area1 = pygame.Rect(area_x, area_y+100, area_a, area_a)
r2_unknown_area2 = pygame.Rect(area_x+100, area_y+100, area_a, area_a)
r2_unknown_area3 = pygame.Rect(area_x+200, area_y+100, area_a, area_a)
r2_unknown_area4 = pygame.Rect(area_x+300, area_y+100, area_a, area_a)
r2_unknown_area5 = pygame.Rect(area_x+400, area_y+100, area_a, area_a)
r2_unknown_area6 = pygame.Rect(area_x+500, area_y+100, area_a, area_a)
r2_unknown_area7 = pygame.Rect(area_x+600, area_y+100, area_a, area_a)
r2_unknown_area8 = pygame.Rect(area_x+700, area_y+100, area_a, area_a)
r2_unknown_area9 = pygame.Rect(area_x+800, area_y+100, area_a, area_a)
r2_unknown_area10 = pygame.Rect(area_x+900, area_y+100, area_a, area_a)

#third row
r3_unknown_area1 = pygame.Rect(area_x, area_y+200, area_a, area_a)
r3_unknown_area2 = pygame.Rect(area_x+100, area_y+200, area_a, area_a)
r3_unknown_area3 = pygame.Rect(area_x+200, area_y+200, area_a, area_a)
r3_unknown_area4 = pygame.Rect(area_x+300, area_y+200, area_a, area_a)
r3_unknown_area5 = pygame.Rect(area_x+400, area_y+200, area_a, area_a)
r3_unknown_area6 = pygame.Rect(area_x+500, area_y+200, area_a, area_a)
r3_unknown_area7 = pygame.Rect(area_x+600, area_y+200, area_a, area_a)
r3_unknown_area8 = pygame.Rect(area_x+700, area_y+200, area_a, area_a)
r3_unknown_area9 = pygame.Rect(area_x+800, area_y+200, area_a, area_a)
r3_unknown_area10 = pygame.Rect(area_x+900, area_y+200, area_a, area_a)

#fourth row
r4_unknown_area1 = pygame.Rect(area_x, area_y+300, area_a, area_a)
r4_unknown_area2 = pygame.Rect(area_x+100, area_y+300, area_a, area_a)
r4_unknown_area3 = pygame.Rect(area_x+200, area_y+300, area_a, area_a)
r4_unknown_area4 = pygame.Rect(area_x+300, area_y+300, area_a, area_a)
r4_unknown_area5 = pygame.Rect(area_x+400, area_y+300, area_a, area_a)
r4_unknown_area6 = pygame.Rect(area_x+500, area_y+300, area_a, area_a)
r4_unknown_area7 = pygame.Rect(area_x+600, area_y+300, area_a, area_a)
r4_unknown_area8 = pygame.Rect(area_x+700, area_y+300, area_a, area_a)
r4_unknown_area9 = pygame.Rect(area_x+800, area_y+300, area_a, area_a)
r4_unknown_area10 = pygame.Rect(area_x+900, area_y+300, area_a, area_a)


item_a = 40
item_x = (grid_unit / 2)-(item_a/2)
item_y = (grid_unit / 2)-(item_a/2)

rand_1 = random.randint(2, 9)
rand_2 = random.randint(1, 9)

item_pos_x = (100 * rand_1)
item_pos_y = (100 * rand_2)

item_1_x = (item_x + item_pos_x)
item_1_y = (item_y + item_pos_y)

item_1 = pygame.Rect(item_1_x, item_1_y, item_a, item_a)

def computers_turn():
    pass

def print_coords():
    pygame.display.set_caption(f"x: {player.x} y: {player.y}")

def item_1_action():
    print("COLLISION!!!")

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.blit(brick_wall, (0, 0))
    pygame.draw.rect(screen, (255, 0, 0), player)

    if player_turn == True:
        print_coords()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and player.y > 25:
            player.y -= 100
        if keys[pygame.K_DOWN] and player.y < 925:
            player.y += 100
        if keys[pygame.K_LEFT] and player.x > 25:
            player.x -= 100
        if keys[pygame.K_RIGHT] and player.x < 925:
            player.x += 100
        player_turn = False
    else:
        computers_turn()

        player_turn = True

    if player.colliderect(item_1):
        item_1_action()

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

    pygame.draw.rect(screen, "black", unknown_area1)
    pygame.draw.rect(screen, "black", unknown_area2)
    pygame.draw.rect(screen, "black", unknown_area3)
    pygame.draw.rect(screen, "black", unknown_area4)
    pygame.draw.rect(screen, "black", unknown_area5)
    pygame.draw.rect(screen, "black", unknown_area6)
    pygame.draw.rect(screen, "black", unknown_area7)
    pygame.draw.rect(screen, "black", unknown_area8)
    pygame.draw.rect(screen, "black", unknown_area9)

    pygame.draw.rect(screen, "black", r2_unknown_area1)
    pygame.draw.rect(screen, "black", r2_unknown_area2)
    pygame.draw.rect(screen, "black", r2_unknown_area3)
    pygame.draw.rect(screen, "black", r2_unknown_area4)
    pygame.draw.rect(screen, "black", r2_unknown_area5)
    pygame.draw.rect(screen, "black", r2_unknown_area6)
    pygame.draw.rect(screen, "black", r2_unknown_area7)
    pygame.draw.rect(screen, "black", r2_unknown_area8)
    pygame.draw.rect(screen, "black", r2_unknown_area9)
    pygame.draw.rect(screen, "black", r2_unknown_area10)

    pygame.draw.rect(screen, "black", r3_unknown_area1)
    pygame.draw.rect(screen, "black", r3_unknown_area2)
    pygame.draw.rect(screen, "black", r3_unknown_area3)
    pygame.draw.rect(screen, "black", r3_unknown_area4)
    pygame.draw.rect(screen, "black", r3_unknown_area5)
    pygame.draw.rect(screen, "black", r3_unknown_area6)
    pygame.draw.rect(screen, "black", r3_unknown_area7)
    pygame.draw.rect(screen, "black", r3_unknown_area8)
    pygame.draw.rect(screen, "black", r3_unknown_area9)
    pygame.draw.rect(screen, "black", r3_unknown_area10)

    pygame.draw.rect(screen, "black", r4_unknown_area1)
    pygame.draw.rect(screen, "black", r4_unknown_area2)
    pygame.draw.rect(screen, "black", r4_unknown_area3)
    pygame.draw.rect(screen, "black", r4_unknown_area4)
    pygame.draw.rect(screen, "black", r4_unknown_area5)
    pygame.draw.rect(screen, "black", r4_unknown_area6)
    pygame.draw.rect(screen, "black", r4_unknown_area7)
    pygame.draw.rect(screen, "black", r4_unknown_area8)
    pygame.draw.rect(screen, "black", r4_unknown_area9)
    pygame.draw.rect(screen, "black", r4_unknown_area10)

    pygame.draw.rect(screen, "purple", item_1)

    pygame.display.flip()
    dt = clock.tick(30) / 1000

pygame.quit()
sys.exit()

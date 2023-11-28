import pygame
import sys

pygame.init()

# Use consistent screen dimensions
screen_width = 1000
screen_height = 1000
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
running = True
dt = 0
brick_wall = pygame.image.load("brick_wall.png")

# Use a consistent unit for the grid (screen_height/10)
grid_unit = screen_height // 10

border_top = pygame.Rect(0, 0, screen_width, 5)
border_left = pygame.Rect(0, 0, 5, screen_height)
border_right = pygame.Rect(995, 0, 5, screen_height)
border_bottom = pygame.Rect(0, 995, screen_width, 5)

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

player_width = 50
player_height = 50
player_x = (grid_unit // 2)-(player_width/2)
player_y = (grid_unit // 2)-(player_height/2)
player = pygame.Rect(player_x, player_y, player_width, player_height)

# Draw the brick wall once before the main loop
screen.blit(brick_wall, (0, 0))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        player_y -= 5
    if keys[pygame.K_DOWN]:
        player_y += 5
    if keys[pygame.K_LEFT]:
        player_x -= 5
    if keys[pygame.K_RIGHT]:
        player_x += 5



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
    pygame.draw.rect(screen, (255, 0, 0), player)





    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()
sys.exit()

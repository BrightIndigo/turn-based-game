import pygame
import sys

pygame.init()

screen_width = 1000
screen_height = 1000
screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
running = True
dt = 0
brick_wall = pygame.image.load("brick_wall.png")
wall1 = pygame.Rect(0, screen_height/10, 1200, 5)
wall2 = pygame.Rect(0, screen_height/10*2, 1200, 5)
wall3 = pygame.Rect(0, screen_height/10*3, 1200, 5)
wall4 = pygame.Rect(0, screen_height/10*4, 1200, 5)
wall5 = pygame.Rect(0, screen_height/10*5, 1200, 5)
wall6 = pygame.Rect(0, screen_height/10*6, 1200, 5)
wall7 = pygame.Rect(0, screen_height/10*7, 1200, 5)
wall8 = pygame.Rect(0, screen_height/10*8, 1200, 5)
wall9 = pygame.Rect(0, screen_height/10*9, 1200, 5)
wall10 = pygame.Rect(screen_height/10, 0, 5, 1200)
wall11 = pygame.Rect(screen_height/10*2, 0, 5, 1200)
wall12 = pygame.Rect(screen_height/10*3, 0, 5, 1200)
wall13 = pygame.Rect(screen_height/10*4, 0, 5, 1200)
wall14 = pygame.Rect(screen_height/10*5, 0, 5, 1200)
wall15 = pygame.Rect(screen_height/10*6, 0, 5, 1200)
wall16 = pygame.Rect(screen_height/10*7, 0, 5, 1200)
wall17 = pygame.Rect(screen_height/10*8, 0, 5, 1200)
wall18 = pygame.Rect(screen_height/10*9, 0, 5, 1200)


# Draw the brick wall once before the main loop
screen.blit(brick_wall, (0, 0))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

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

    keys = pygame.key.get_pressed()

    pygame.display.flip()
    dt = clock.tick(60) / 1000

pygame.quit()
sys.exit()

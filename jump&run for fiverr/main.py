import pygame
from pygame.locals import *
import player
import bullet

# Globals
groundLvl = 450
bgColor = (0,0,0)

# Display
ws = [500,500]
fps = 60
win = pygame.display.set_mode(ws)
clock = pygame.time.Clock()

# Player
p = player.Player(pygame.Rect(100,groundLvl-20,20,20), (255,0,0))

# Bullets
bullets = bullet.Bullets((0,255,0))
bullets.create((pygame.Rect(100,100,10,10)))
bullets.create((pygame.Rect(120,120,10,10)))
bullets.create((pygame.Rect(140,140,10,10)))

while True:
    
    clock.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                p.headDirection = 0
                p.movement[0] = -5
            if event.key == pygame.K_d:
                p.headDirection = 1
                p.movement[0] = 5
            if event.key == pygame.K_SPACE:
                if not p.isJumping:
                    p.isJumping = True
            if event.key == pygame.K_w:
                pass
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                p.movement[0] = 0
            if event.key == pygame.K_d:
                p.movement[0] = 0

    p.show(win, bgColor)
    pygame.draw.line(win, (255,255,255), (0, groundLvl), (ws[1], groundLvl))
    bullets.show(win)

    p.move()

    pygame.display.update()
    win.fill(bgColor)
import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800, 600))

x = random.randint(0, 775)
y = random.randint(0, 575)
d = 20


running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_RIGHT:
                x += d
            if event.key == pygame.K_LEFT:
                x -= d
            if event.key == pygame.K_UP:
                y -= d
            if event.key == pygame.K_DOWN:
                y += d

    if x > 800 or x < 0:
        x = (x + 800) % 800
    if y > 600 or y < 0:
        y = (y + 600) % 600

    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (255, 0, 0), (x, y), 25)
    
    pygame.display.flip()
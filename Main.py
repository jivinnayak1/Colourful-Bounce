import pygame
import random
pygame.init()

screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("Colourful Bounce")


colour = (255,0,0)

Rad = 35

Ball_x = (250)
Ball_y = (250)

centre = (Ball_x,Ball_y)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    screen.fill((255,255,255))
    Ball_y = Ball_y+0.2

    if Ball_y>500:
        Ball_y=40
        Ball_x = random.randint(50,450)
        colour = (random.randint(0,255),random.randint(0,255),random.randint(0,255))



    pygame.draw.circle(screen,colour,(Ball_x,Ball_y),Rad)
    pygame.display.flip()
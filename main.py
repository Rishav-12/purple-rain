import pygame
from drop import Drop

pygame.init()
clock = pygame.time.Clock()
WIDTH = 640
HEIGHT = 360
BG = (230, 230, 250)
DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT))
#DISPLAYSURF.fill(BG)
pygame.display.set_caption('Purple Rain!')

running = True
drops = []
for i in range(500):
    drops.append(Drop(WIDTH))
while running:
    for d in drops:
        pygame.draw.line(DISPLAYSURF, (138, 43, 226), (d.x, d.y), (d.x, d.y+d.len))
        d.fall(HEIGHT)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    clock.tick(60)
    pygame.display.update()
    DISPLAYSURF.fill(BG)

pygame.quit()
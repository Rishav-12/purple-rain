import random
import pygame

pygame.init()
clock = pygame.time.Clock()
WIDTH = 640
HEIGHT = 360
BG = (230, 230, 250)
DISPLAYSURF = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption('Purple Rain!')

class Drop:
    def __init__(self, WIDTH):
        self.x = random.randint(0, WIDTH)
        self.y = random.randint(-500, -50)
        self.yspeed = random.randint(4, 10)
        self.len = random.randint(10, 40)

    def fall(self, HEIGHT):
        self.y += self.yspeed
        if self.y > HEIGHT:
            self.y = random.randint(-200, -100)

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
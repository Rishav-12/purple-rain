import random

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

    def show(self):
        pass
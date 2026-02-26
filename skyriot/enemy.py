"""Enemy behavior and logic."""


class Enemy:
    def __init__(self, x=0, y=0, speed=1):
        self.x = x
        self.y = y
        self.speed = speed

    def update(self):
        self.y += self.speed

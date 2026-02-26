"""Bullet handling."""


class Bullet:
    def __init__(self, x=0, y=0, velocity=5):
        self.x = x
        self.y = y
        self.velocity = velocity

    def update(self):
        self.y -= self.velocity

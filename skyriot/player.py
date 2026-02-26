"""Player-related logic."""


class Player:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.health = 100

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

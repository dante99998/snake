from settings import *

class Snake:
    def __init__(self, pos, dir):
        self.pos = pos
        self.dir = dir

class Position:
    def __init__(self, *args):
        self.x = args[0]
        self.y = args[1]

    def cur(self):
        return self.x, self.y

    def change(self, *args):
        self.x = self.x + args[0]
        self.y = self.y + args[1]

        if self.x > SCR_WIDTH: self.x = 0
        if self.y > SCR_HEIGHT: self.y = 0
        if self.x < 0: self.x = SCR_WIDTH
        if self.y < 0: self.y = SCR_HEIGHT
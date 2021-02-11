from settings import *

class Snake:
    def __init__(self, pos):
        self.head = pos
        self.tail = pos
        self.blocks = [self.head]
        self.long_enough = False

    def move(self, *dir):
        self.cur_dir = dir

        x = self.head.x + dir[0]
        y = self.head.y + dir[1]

        if x > SCR_WIDTH: x = 0
        if y > SCR_HEIGHT: y = 0
        if x < 0: x = SCR_WIDTH
        if y < 0: y = SCR_HEIGHT

        self.head = Position(x,y)

        if self.head in self.blocks:
            return False

        self.blocks.append(self.head)

        self.tail = self.blocks[0]
        del self.blocks[0]

        return True

    def grow(self):
        new_head = self.head
        new_head.change(*self.cur_dir)
        self.blocks.append(new_head)
        self.head = new_head
        self.long_enough = True

    def get_head(self):
        return self.head.cur()

    def get_tail(self):
        return self.tail.cur()

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
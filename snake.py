from settings import *

class Snake:
    def __init__(self, pos, color):
        self.head = pos
        self.tail = pos
        self.blocks = [self.head]
        self.color = color

    def move(self, *dir):
        self.cur_dir = dir

        x = self.head.x + dir[0]
        y = self.head.y + dir[1]

        self.head = Position(x,y)

        if not self.in_screen(x, y): return False
        if self.eat_body(): return False

        self.blocks.append(self.head)

        self.tail = self.blocks[0]
        del self.blocks[0]

        return True

    def in_screen(self, x, y):
        margin = SCR_WIDTH - BLOCK_SIZE[0]
        if x > margin or y > margin : return False
        if x < 0 or y < 0: return False

        return True

    def eat_body(self):
        dir_s = DIR_RIGHT[0]
        h_x, h_y = self.head.cur()
        for pos in self.blocks:
            x, y = pos.cur()
            if abs(x - h_x) < dir_s and abs(y - h_y) < dir_s: 
                return True

    def grow(self):
        new_head = self.head
        new_head.change(*self.cur_dir)
        self.blocks.append(new_head)
        self.head = new_head

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
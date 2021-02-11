import pygame as pg
from snake import Snake, Position
from settings import * 

class Game:
    is_running = True
    dir = DIR_RIGHT

    def sweep(self, surf, rect):
        size = len(rect)
        if size is not 4: 
            print("rect size is not 4, size = ", size)
            return
        pg.draw.rect(surf, BLACK, rect)
    
    def __init__(self):
        pg.init()
        self.clock = pg.time.Clock()
        self.display = pg.display.set_mode(SCR_SIZE)

        self.pos = Position(*START_POS)
        self.snake = Snake(self.pos)
        self.snake.move(*self.dir)
        
    def render(self):
        self.draw_snake(self.snake)
        pg.display.update()

        # pg.draw.rect(self.display , WHITE, self.pos.cur() + BLOCK_SIZE)
        # pg.display.update()
        # self.sweep(self.display, self.pos.cur() + BLOCK_SIZE)

    def draw_snake(self, snake):
        
        self.sweep(self.display, self.snake.get_tail() + BLOCK_SIZE)
        pg.draw.rect(self.display , WHITE, self.snake.get_head() + BLOCK_SIZE)

    def update(self):
        # self.pos.change(*self.dir)
        if not self.snake.move(*self.dir):
            self.is_running = False
        self.clock.tick(FPS)
    
    def event_handler(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.is_running = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.is_running = False
                elif event.key == pg.K_d:
                    self.dir = DIR_RIGHT
                elif event.key == pg.K_a:
                    self.dir = DIR_LEFT
                elif event.key == pg.K_w:
                    self.dir = DIR_UP
                elif event.key == pg.K_s:
                    self.dir = DIR_DOWN
                elif event.key == pg.K_f:
                    self.snake.grow()
                    print("Here should be drowing")

    def quit(self):
        pg.quit()


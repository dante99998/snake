import pygame as pg
from snake import Snake, Position
from settings import * 
import random as rand

class Game:
    is_running = True
    dir = DIR_RIGHT
    
    def __init__(self):
        pg.init()
        self.clock = pg.time.Clock()
        self.display = pg.display.set_mode(SCR_SIZE)
        self.bg_color = BLACK

        self.pos = Position(*START_POS)
        self.snake = Snake(self.pos, GREEN)
        self.snake.move(*self.dir)

        self.meal = self.draw_meal()
        
    def render(self):
        self.draw_snake(self.snake)
        pg.display.update()

    def update(self):
        if not self.snake.move(*self.dir):
            self.is_running = False

        if self.is_eat(self.snake.head, self.meal):
            self.snake.grow()
            self.meal = self.draw_meal()


        self.clock.tick(FPS)

    def is_eat(self, snake_head, meal):
        h_bx, h_by = snake_head.cur()
        m_x, m_y = meal.cur() 
        if abs(m_x - h_bx) < BLOCK_SIZE[0] and abs(m_y - h_by) < BLOCK_SIZE[0]:
            self.sweep(self.display, meal.cur()  + BLOCK_SIZE)
            return True

        return False

    def event_handler(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.is_running = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    self.is_running = False
                elif event.key == pg.K_d:
                    if self.dir != DIR_LEFT: self.dir = DIR_RIGHT
                elif event.key == pg.K_a:
                    if self.dir != DIR_RIGHT: self.dir = DIR_LEFT
                elif event.key == pg.K_w:
                    if self.dir != DIR_DOWN: self.dir = DIR_UP
                elif event.key == pg.K_s:
                    if self.dir != DIR_UP: self.dir = DIR_DOWN

    def draw_snake(self, snake):
        self.sweep(self.display, self.snake.get_tail() + BLOCK_SIZE)
        pg.draw.rect(self.display , self.snake.color, self.snake.get_head() + BLOCK_SIZE)

    def sweep(self, surf, rect):
        # size = len(rect)
        # if size is not 4: 
        #     print("rect size is not 4, size = ", size)
        #     return
        pg.draw.rect(surf, self.bg_color, rect)

    def draw_meal(self):
        margin = SCR_WIDTH - BLOCK_SIZE[0]
        scr_size = SCR_WIDTH * SCR_HEIGHT
        r = rand.randint(0, scr_size)
        pos = divmod(r, SCR_WIDTH)
        while pos[0] > margin or pos[1] > margin:
            r = rand.randint(0, scr_size)
            pos = divmod(r, SCR_WIDTH)
        
        pg.draw.rect(self.display , RED, pos + BLOCK_SIZE)
        return Position(*pos)

    def quit(self):
        pg.quit()


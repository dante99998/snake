from game import Game

def main():
    game = Game()

    while game.is_running:
        game.render()
        game.event_handler()
        game.update()

    game.quit()
        
if __name__ == "__main__":
    main()
    # pos = Position(0,0)
    # print(pos.cur())
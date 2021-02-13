from game import Game

def main():
    game = Game()

    while game.is_running:
        game.render()
        game.update()
        game.event_handler()

    game.quit()
    print("GAME OVER")
        
if __name__ == "__main__":
    main()
    # pos = Position(0,0)
    # print(pos.cur())
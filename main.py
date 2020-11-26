from src.reader import Reader
from src.board import Board
from src.gameSystem import GameSystem

if __name__ == '__main__':
    config = Reader.config('config.txt')
    try :
        game = GameSystem(config)
        game.run()
    except Exception :
        print("Exit Program")
from src.reader import Reader
from src.board import Board
from src.gameSystem import GameSystem

if __name__ == '__main__':
    config = Reader.config('config.txt')
    game = GameSystem(config)
    game.run()
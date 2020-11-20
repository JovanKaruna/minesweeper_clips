from src.reader import Reader
from src.board import Board

if __name__ == '__main__':
    config = Reader.config('config.txt')
    board = Board(config)

    print(board)
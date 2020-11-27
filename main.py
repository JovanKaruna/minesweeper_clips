import sys
from src.reader import Reader
from src.gameSystem import GameSystem

if __name__ == '__main__':
    CONFIG = sys.argv[1] if len(sys.argv) > 1 else 'config.txt'
    config = Reader.config(CONFIG)
    try :
        game = GameSystem(config)
        game.run()
    except Exception :
        print("Exit Program")
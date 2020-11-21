from .board import Board
from .agent import Agent

class GameSystem:

    def __init__(self, config):
        self.goals_board = Board(config, False)
        self.agent_board = Board(config, True)
        self.agent = Agent()

        # Initialize First Move Agent (Start at (0,0))
        self.open_board((0,0), [])

    def open_board(self, location, done):
        '''Mechanics when press on board to open the tiles

        Parameters:
            location (Tuple(int, int))
        
        Returns:
            Board: newest Board
        '''
        element = self.goals_board.get_element(location)
        self.agent_board.board[location[0]][location[1]] = element
        
        if element != 0:
            return

        list_moves = {
            'left': (location[0], location[1]-1),
            'right': (location[0], location[1]+1),
            'top': (location[0]-1, location[1]),
            'bottom': (location[0]+1, location[1]),
        }

        moves = []
        for k, v in list_moves.items():
            if self.agent_board.is_valid(v[0]) and self.agent_board.is_valid(v[1]):
                if v not in done:
                    moves.append(v)
                    done.append(v)

        for move in moves:
            self.open_board(move, done)

    def run(self):
        moves = self.agent.decide(self.agent_board.board)
        while len(moves) != 0:
            for move in moves:
                self.open_board(move, [])
            moves = self.agent.decide(self.agent_board.board)
        print(self.agent.bombs)
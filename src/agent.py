from clips import Environment

class Agent:

    def __init__(self):
        self.env = Environment()
        self.bombs = []

    def assert_facts(self, board):

        # positions Facts
        for row in range(len(board)):
            for col in range(len(board)):
                element = board[row][col]
                if element == '?':
                    element = 'nil'
                fact_string = f'(positions {row} {col} {element})'
                self.env.assert_string(fact_string)
        
        # mark Facts
        self.env.assert_string('(mark nil nil 0)')
        for row in range(len(board)):
            for col in range(len(board)):
                element = board[row][col]
                if element == '?':
                    element = '1'
                else:
                    element = '0'
                fact_string = f'(mark {row} {col} {element})'
                self.env.assert_string(fact_string)

        # markBomb Facts
        self.env.assert_string('(markBomb nil nil 0)')
        for row in range(len(board)):
            for col in range(len(board)):
                if (row, col) in self.bombs:
                    element = '1'
                else:
                    element = '0'
                fact_string = f'(markBomb {row} {col} {element})'
                self.env.assert_string(fact_string)
        
        # bomb Facts
        self.env.assert_string('(bomb nil nil 0)')
        
        # board_size Facts
        self.env.assert_string(f'(board_size {len(board)})')

    def get_bomb(self):
        for fact in self.env.facts():
            if fact.template.name == 'bomb':
                if fact[0] == 'nil' or fact[1] == 'nil':
                    continue
                if (fact[0], fact[1]) in self.bombs:
                    continue
                self.bombs.append((int(fact[0]), int(fact[1])))

    def get_tiles(self):
        tiles = []
        for fact in self.env.facts():
            if fact.template.name == 'tiles':
                if fact[0] == 'nil' or fact[1] == 'nil':
                    continue
                tiles.append((int(fact[0]), int(fact[1])))
        return tiles

    def decide(self, board):
        self.env = Environment()
        self.env.load('src/brains/rules.clp')
        self.assert_facts(board)
        self.env.run()
        self.get_bomb()
        return self.get_tiles()
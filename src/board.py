class Board:
    '''Class Board contains everything on board game'''

    def __init__(self, config, agent):
        self.board_size = config['board_size']
        self.bomb_size = config['bomb_size']
        self.bomb_locations = config['bomb_locations']

        if not agent:
            self.init_board_element()
        else:
            self.board = [['?' for i in range(self.board_size)] for j in range(self.board_size)]

    
    def __str__(self):
        out = ''
        for i in range(self.board_size):
            for j in range(self.board_size):
                out += str(self.board[i][j])
                out += ' '
            out += '\r\n'
        return out
    
    def __eq__(self, another):
        for i in range(self.board_size):
            for j in range(self.board_size):
                if self.board[i][j] != another.board[i][j]:
                    return False
        return True 
    
    def get_element(self, location):
        return self.board[location[0]][location[1]]

    def is_valid(self, value):
        '''Is value outside board
        
        Parameters:
            value (int): value to be checked

        Returns:
            boolean: True if valid
        '''
        return (value >= 0) and (value < self.board_size)
    
    def is_bomb(self, location):
        '''Is tiles equals bomb

        Parameters:
            location (Tuple(int, int)): location to be checked

        Returns:
            boolean: True if valid
        '''
        for bomb in self.bomb_locations:
            if (location[0] == bomb[0]) and (location[1] == bomb[1]):
                return True

    def set_tile_element(self, location):
        '''Set element in tiles

        Parameters:
            location (Tuple(int, int)): location to be set
        
        Returns:
            int: tile element
        '''
        if self.is_bomb(location):
            return '?'

        check = {
            'left': (location[0], location[1]-1),
            'right': (location[0], location[1]+1),
            'top': (location[0]-1, location[1]),
            'bottom': (location[0]+1, location[1]),
            'left_top': (location[0]-1, location[1]-1),
            'left_bottom': (location[0]+1, location[1]-1),
            'right_top': (location[0]-1, location[1]+1),
            'right_bottom': (location[0]+1, location[1]+1)
        }

        fin_check = []
        for k, v in check.items():
            if self.is_valid(v[0]) and self.is_valid(v[1]):
                fin_check.append(v)


        ret = 0
        for pos in fin_check:
            if self.is_bomb(pos):
                ret += 1
        return ret

    def init_board_element(self):
        '''Initialize all elements for board
        '''
        self.board = [[0 for i in range(self.board_size)] for j in range(self.board_size)]

        for row in range(self.board_size):
            for col in range(self.board_size):
                self.board[row][col] = self.set_tile_element((row, col))

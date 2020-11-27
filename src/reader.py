class Reader:

    @staticmethod
    def config(filename):
        f = open(f'config/{filename}', 'r')
        content = f.read()
        return Reader.parse(content)

    @staticmethod
    def parse(text):
        splitted_text = text.split('\n')
        board_size = int(splitted_text[0])
        bomb_size = int(splitted_text[1])
        location_bomb = []
        for i in range(bomb_size):
            splitted_loc = splitted_text[2+i].replace(' ', '').split(',')
            location_bomb.append((int(splitted_loc[0]), int(splitted_loc[1])))
        
        return {
            'board_size': board_size,
            'bomb_size': bomb_size,
            'bomb_locations': location_bomb
        }
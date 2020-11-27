import PySimpleGUI as sg

class GUI:
    def __init__(self, b_size):
        self.b_size = b_size
        self.window = None
        sg.ChangeLookAndFeel('Reddit')
     
    def init_game_board(self):
        tile_size = (4,2) if self.b_size <= 10 else (2,1)

        board = [[(i,j) for j in range(self.b_size)] for i in range(self.b_size)]
        axis = [[sg.B('X/Y', size=tile_size, pad=(0,0), disabled=True,border_width=0, focus=False, button_color=(("black", sg.theme_background_color())), disabled_button_color=("black", sg.theme_background_color()))] 
                + list(sg.B(i, size=tile_size, pad=(0,0), disabled=True, focus=False, border_width=0, button_color=(("black", sg.theme_background_color())), disabled_button_color=("black", sg.theme_background_color())) for i in range(self.b_size))]

        board_layout = [[sg.B(i, size=tile_size, pad=(0,0), disabled=True, focus=False, border_width=0, button_color=(("black", sg.theme_background_color())), disabled_button_color=("black", sg.theme_background_color()))] 
                        + [sg.B('', size=tile_size, key=(i,j), pad=(0,0),focus=False, button_color=("black",self.generate_button_color((i,j))),border_width=0)
              for j in range(self.b_size)] for i in range(self.b_size)]

        self.board_window = axis + board_layout
        
    def init_layout(self):
        if self.board_window is None: 
            return 
        self.layout = [[sg.Text("💣",  font=("Helvetica", 20)), sg.Text('Mine Sweeper', text_color='#76ba1b', font=("Helvetica", 24)), sg.Text("💣",  font=("Helvetica", 20))],
            [sg.Column(self.board_window)]]

    def generate_button_color(self, position, opened=False):
        if not opened:
            return "#a4de02" if (position[0] + position[1]) % 2 == 0 else "#76ba1b" #green
        else:
            return "#e7dec8" if (position[0] + position[1]) % 2 == 0 else "#cbaf87" #brown
    
    def render(self, agent_board):
        if self.window is None or self.layout is None: 
            self.init_game_board()
            self.init_layout()
            self.window = sg.Window('Mine Sweeper', self.layout, keep_on_top=True, resizable=False, element_justification='c')
            self.window.Finalize()
        for i in range(agent_board.board_size):
            for j in range(agent_board.board_size):
                if (agent_board.board[i][j] == "?"):
                    self.window[(i,j)].update("", disabled=True, button_color=("#411f1f", self.generate_button_color(position=(i, j))))
                elif (agent_board.board[i][j] == 0):
                    self.window[(i,j)].update("", disabled=True, button_color=("#411f1f", self.generate_button_color(position=(i, j), opened=True)))
                else:
                    if (agent_board.board[i][j] == 1):
                        self.window[(i,j)].update(str(agent_board.board[i][j]), disabled=True, button_color=("white", self.generate_button_color(position=(i, j), opened=True)), disabled_button_color=("blue", sg.theme_background_color()))
                    elif (agent_board.board[i][j] == 2):
                        self.window[(i,j)].update(str(agent_board.board[i][j]), disabled=True, button_color=("white", self.generate_button_color(position=(i, j), opened=True)), disabled_button_color=("green", sg.theme_background_color()))
                    else : #3
                        self.window[(i,j)].update(str(agent_board.board[i][j]), disabled=True, button_color=("white", self.generate_button_color(position=(i, j), opened=True)), disabled_button_color=("red", sg.theme_background_color()))
        self.window.read(timeout=10)
        
    def render_end_game(self, bomb_location):
        for (x, y) in bomb_location:
            self.window[(x, y)].update("💣", disabled=True, button_color=("white", "gray"), disabled_button_color=("black", sg.theme_background_color()))
        self.render_end_bombloc(bomb_location)
            
    def render_end_bombloc(self, bomb_location):
        bomb_loc_str = str(bomb_location).strip('[]')
        layout = [
            [sg.T('END GAME', size=(20,1), text_color='#76ba1b', font='Any 20', justification='center')],
            [sg.T('Detected Bomb Location:', justification='center')],
            [sg.T(bomb_loc_str, justification='center')]
        ]
        self.end_window = sg.Window('End Game', layout, element_justification='center', keep_on_top=True, grab_anywhere=True)
        event, values = self.end_window.read()          
        if event == sg.WIN_CLOSED:
            self.end_window.close()
        
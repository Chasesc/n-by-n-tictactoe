import pygame, graphics, constants as Const

from random import randint

class Game(object):

    def __init__(self, against_ai = True):
        self.running = True
        self.in_menu = False
        self.game_state = GameState(against_ai)
        self.ai = None

    def setup(self):
        Rules.winner = None
        Rules.winner_indices = []

    def run(self):
        import tictactoeAgent
        self.setup()

        if self.game_state.is_against_ai():
            if Const.AI_DIFFICULTY == Const.AI_DIFFICULTY_EASY:
                self.ai = tictactoeAgent.RandomAgent()
            elif Const.AI_DIFFICULTY == Const.AI_DIFFICULTY_HARD:
                self.ai = tictactoeAgent.MiniMaxAgent()
            else: raise Exception("AI_DIFFICULTY in constants.py set to an invalid option.")

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False                   
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if not self.in_menu and Rules.winner is None:
                        self.game_state.place(get_loc_from_mouse(event.pos))
                        print self.game_state.get_current_player()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r: 
                        Game(self.game_state.is_against_ai()).run() # Restart the game.

            if Rules.is_terminal_state(self.game_state.get_board()):
                # TODO: Ask the user if they want to play again.
                         
                graphics.draw_game(self.game_state.get_board(), Rules.winner_indices)
            else:
                if self.in_menu: graphics.draw_menu()
                else: graphics.draw_game(self.game_state.get_board()) 

            if self.game_state.is_ai_turn() and Rules.winner is None:
                self.game_state.place(self.ai.get_action(self.game_state.get_board()))

        pygame.quit()


class GameState(object):      

    def __init__(self, against_ai = True):
        assert Const.BOARD_N > 1
        self.__board = [None] * Const.BOARD_SIZE
        self.__against_ai = against_ai # If this is false, it's two humans playing each other.

        # Selects either X or O for player one and the opposite for player two
        rand = randint(0, 1)
        self.__player_one = ['X', 'O'][rand]
        self.__player_two = ['X', 'O'][not rand]

        self.__current_turn = self.__player_one if rand == 0 else self.__player_two # 'X' goes first

    def is_against_ai(self):
        return self.__against_ai

    def is_ai_turn(self):
        return self.__against_ai and self.__player_two == self.__current_turn

    def place(self, index):
        if self.__board[index] is not None: return
        self.__board[index] = self.__current_turn
        self.__current_turn = 'X' if self.__current_turn == 'O' else 'O'

    def get_current_player(self):
        return self.__current_turn

    def get_board(self):
        return self.__board

    def __str__(self):
        str = ""
        for i in range(Const.BOARD_SIZE):
            if i % Const.BOARD_N == 0: str += "\n"
            if self.__board[i] is not None: str += self.__board[i]
            else: str += "n"            

        return str


class Rules(object):

    winner = None
    winner_indices = []

    ''' Returns the indices of the avaliable moves. '''
    @staticmethod
    def avaliable_moves(board):
        return [index for index, play in list(enumerate(board)) if play is None]

    @staticmethod
    def line_connected(board, player, start, stop, step = 1):
        indices = [i for i in range(start, stop, step)]
        connected = [board[i] for i in indices].count(player) == Const.BOARD_N
        if connected: Rules.winner_indices = indices
        return connected

    @staticmethod
    def col_win(board, player):
        for i in range(Const.BOARD_N):
            if Rules.line_connected(board, player, i, (Const.BOARD_N - 1) * Const.BOARD_N + i + 1, Const.BOARD_N): return True

        return False

    @staticmethod
    def row_win(board, player):
        for i in range(Const.BOARD_N):
            if Rules.line_connected(board, player, i * Const.BOARD_N, (i + 1) * Const.BOARD_N): return True

        return False

    @staticmethod
    def diag_win(board, player):     
        return  (    
                    Rules.line_connected(board, player, 0, Const.BOARD_SIZE, Const.BOARD_N + 1) or 
                    Rules.line_connected(board, player, Const.BOARD_N - 1, (Const.BOARD_N - 1) * Const.BOARD_N + 1, Const.BOARD_N - 1)
                )

    @staticmethod
    def has_won(board, player):
        won = Rules.diag_win(board, player) or Rules.col_win(board, player) or Rules.row_win(board, player)
        if won: Rules.winner = player
        return won

    @staticmethod
    def either_won(board):
        return Rules.has_won(board, 'X') or Rules.has_won(board, 'O')

    @staticmethod
    def is_tie(board):
        return len(Rules.avaliable_moves(board)) == 0

    @staticmethod
    def is_terminal_state(board):
        return Rules.either_won(board) or Rules.is_tie(board)


''' Returns the index to the board from a mouse_location.  For example, clicking in
    the top left would return 0 which is the first element on the board. '''
def get_loc_from_mouse(mouse_location):
    # box_width and box_height are the width and height of a single game square.
    box_width = Const.BOARD_N * Const.WINDOW_WIDTH // Const.BOARD_SIZE
    box_height = Const.BOARD_N * Const.WINDOW_HEIGHT // Const.BOARD_SIZE

    two_box_width = 2 * box_width
    two_box_height = 2 * box_height

    three_box_width = 3 * box_width
    three_box_height = 3 * box_height

    x = mouse_location[0]
    y = mouse_location[1]

    if x <= box_width and y <= box_height: return 0
    elif x <= two_box_width and y <= box_height: return 1
    elif x <= three_box_width and y <= box_height: return 2
    elif x <= box_width and y <= two_box_height: return 3
    elif x <= two_box_width and y <= two_box_height: return 4
    elif x <= three_box_width and y <= two_box_height: return 5
    elif x <= box_width and y <= three_box_height: return 6
    elif x <= two_box_width and y <= three_box_height: return 7
    elif x <= three_box_width and y <= three_box_height: return 8
    else: raise Exception("Unable to determine correct index in get_loc_from_mouse!") # Shouldn't happen, but just in case.



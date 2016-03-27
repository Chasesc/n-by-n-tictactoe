from __future__ import division
import pygame, constants as Const


# Graphics
pygame.display.set_caption('TicTacToe - chasesc')
screen = pygame.display.set_mode(Const.WINDOW_SIZE)

pygame.font.init()
main_font = pygame.font.SysFont("monospace", 15)

# TODO: change this function
def display_text(text, location):
    location = (location[0] - len(text), location[1])
    if location[0] < 0: location[0] = 0
    label = main_font.render(text, 1, (255,255,255))
    screen.blit(label, location)


def draw_board():

    # vertical line(s)
    for i in range(1, Const.BOARD_N):
        i_width_over_n = (i * Const.WINDOW_WIDTH) // Const.BOARD_N
        pygame.draw.line(screen, Const.WHITE, (i_width_over_n, 0), (i_width_over_n, Const.WINDOW_HEIGHT), Const.LINE_WIDTH)

    # horizontal line(s)
    for i in range(1, Const.BOARD_N):
        i_height_over_n = (i * Const.WINDOW_HEIGHT) // Const.BOARD_N
        pygame.draw.line(screen, Const.WHITE, (0, i_height_over_n), (Const.WINDOW_WIDTH, i_height_over_n), Const.LINE_WIDTH)


def draw_piece(location, current_piece, winner = False):

    coeff_x, coeff_y = get_coefficients(location)

    # Note a << b is the same as a * (2 ** b)
    width = (coeff_x * Const.WINDOW_WIDTH) // (Const.BOARD_N << 1)
    height = (coeff_y * Const.WINDOW_HEIGHT) // (Const.BOARD_N << 1)

    start_pos = (width, height)

    if current_piece == 'X':
        color = Const.X_WIN_COLOR if winner else Const.X_COLOR

        #top right line of X
        x = width + Const.COS_45_MUL_LEN
        y = height + Const.SIN_45_MUL_LEN
        pygame.draw.line(screen, color, start_pos, (x, y), Const.HALF_LINE_WIDTH)
        
        #top left line of X
        x = width + Const.COS_135_MUL_LEN
        y = height + Const.SIN_135_MUL_LEN
        pygame.draw.line(screen, color, start_pos, (x, y), Const.HALF_LINE_WIDTH)

        #bottom left line of X
        x = width + Const.COS_225_MUL_LEN
        y = height + Const.SIN_225_MUL_LEN
        pygame.draw.line(screen, color, start_pos, (x, y), Const.HALF_LINE_WIDTH)
        
        #bottom right line of X
        x = width + Const.COS_315_MUL_LEN
        y = height + Const.SIN_315_MUL_LEN
        pygame.draw.line(screen, color, start_pos, (x, y), Const.HALF_LINE_WIDTH)

    elif current_piece == 'O':
        color = Const.O_WIN_COLOR if winner else Const.O_COLOR
        pygame.draw.circle(screen, color, start_pos, Const.RADIUS_LENGTH, Const.LINE_WIDTH >> 1)
    else:
        raise Exception("Current piece should be either 'X' or 'O'") # Shouldn't happen, but just in case.

def draw_game_pieces(game_board, winners = []):
    win = False
    for index, play in list(enumerate(game_board)):
        if play is not None:
            if winners is not None:
                for win_index in winners:
                    if win_index == index: win = True

            draw_piece(index, play, win)
            win = False


def blank_screen(color = Const.LIGHT_BLACK):
    screen.fill(color)

#TODO: Make the menu system.
def draw_menu(first_game = True):
    blank_screen()

    display_text("Hello, world!", (Const.WINDOW_WIDTH // 2, 15))

    pygame.time.delay(50)
    pygame.display.flip() #Update the full screen


def draw_game(game_board, winners = []):
    blank_screen()

    draw_board()
    draw_game_pieces(game_board, winners)

    pygame.time.delay(50)
    pygame.display.flip() #Update the full screen



def get_coefficients(location):
    loc_over_n = location // Const.BOARD_N
    x = (2 * (location - (Const.BOARD_N * loc_over_n))) + 1
    y = (2 * loc_over_n) + 1

    return (x , y)

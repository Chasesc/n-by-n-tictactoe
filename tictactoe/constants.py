from __future__ import division
import math

AI_DIFFICULTY_EASY = 0
AI_DIFFICULTY_HARD = 1

# value must be an AI_DIFFICULTY option above
AI_DIFFICULTY = AI_DIFFICULTY_HARD

BOARD_N = 3
BOARD_SIZE = BOARD_N ** 2

#window
WINDOW_WIDTH = 1280
WINDOW_HEIGHT = 720
WINDOW_SIZE = (WINDOW_WIDTH, WINDOW_HEIGHT)

#length and width info
LINE_WIDTH = 5

HALF_LINE_WIDTH = LINE_WIDTH // 2
X_LINE_LENGTH = int(WINDOW_HEIGHT // (BOARD_N * 2))
RADIUS_LENGTH = int(WINDOW_HEIGHT // (BOARD_N * 2.5))

#math, saves computation each frame
COS_45 = math.cos(math.radians(45))
SIN_45 = math.sin(math.radians(45))

COS_135 = math.cos(math.radians(135))
SIN_135 = math.sin(math.radians(135))

COS_225 = math.cos(math.radians(225))
SIN_225 = math.sin(math.radians(225))

COS_315 = math.cos(math.radians(315))
SIN_315 = math.sin(math.radians(315))

COS_45_MUL_LEN = COS_45 * X_LINE_LENGTH
SIN_45_MUL_LEN = SIN_45 * X_LINE_LENGTH

COS_135_MUL_LEN = COS_135 * X_LINE_LENGTH
SIN_135_MUL_LEN = SIN_135 * X_LINE_LENGTH

COS_225_MUL_LEN = COS_225 * X_LINE_LENGTH
SIN_225_MUL_LEN = SIN_225 * X_LINE_LENGTH

COS_315_MUL_LEN = COS_315 * X_LINE_LENGTH
SIN_315_MUL_LEN = SIN_315 * X_LINE_LENGTH


#colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_BLACK = (28, 28, 28)

X_COLOR = (255,99,71)
O_COLOR = (135,206,235)

X_WIN_COLOR = WHITE
O_WIN_COLOR = WHITE

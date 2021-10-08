import random
import copy
from time import sleep
import os


ALIVE = '■'
DEAD = ' '
CLR = "\033[37m"

MATRIX_SIZE = 19201
ROW_LENGTH = 211


def refresh():
    os.system("clear")

#
# class Cell:
#     def __init__(self, index, start):
#         self.state = start
#         self.idx = index
#         self.neighbors = [index + x for x in [1, -1, *[ROW_LENGTH + x for x in [-1, 0, 1]], *[-ROW_LENGTH + x for x in [-1, 0, 1]]]]
#         self.neighbors = [x for x in self.neighbors if (0 <= x < MATRIX_SIZE)]
#
#     def get_state(self):
#         return self.state
#
#     def set_state(self, state):
#         self.state = state
#
#     def __str__(self):
#         return self.state
#
#     def __repr__(self):
#         return self.state


def get_neighbors(idx):
    neighbors = [idx + x for x in
                      [1, -1, *[ROW_LENGTH + x for x in [-1, 0, 1]], *[-ROW_LENGTH + x for x in [-1, 0, 1]]]]
    return [x for x in neighbors if (0 <= x < MATRIX_SIZE)]


def next_state(pos, mtrx):
    n_of_live_neighbors = len([x for x in get_neighbors(pos) if mtrx[x] == ALIVE])
    if mtrx[pos] == ALIVE:
        if n_of_live_neighbors == 2 or n_of_live_neighbors == 3:
            return ALIVE
        return DEAD
    if n_of_live_neighbors == 3:
        return ALIVE
    return DEAD


# def start_cell(mtrx):
#     idx = random.randint(0, MATRIX_SIZE)
#     cells = [idx] + random.sample(mtrx[idx].neighbors, )


def gliding_gun_right(mtrx, pos):
    # Left square
    left_sqr = [pos, pos+1, pos+ROW_LENGTH, pos+ROW_LENGTH+1,]
    pos += 10
    #Left circle
    left_circ = [pos, pos+ROW_LENGTH, pos+ROW_LENGTH*2, pos+ROW_LENGTH*3+1, pos+ROW_LENGTH*4+2, pos+ROW_LENGTH*4+3, pos+ROW_LENGTH*3+5, pos+ROW_LENGTH*2+6, pos+ROW_LENGTH*1+6, pos+6, pos-ROW_LENGTH*1+5, pos-ROW_LENGTH*2+3, pos-ROW_LENGTH*2+2, pos-ROW_LENGTH*1+1, pos+ROW_LENGTH*1+4, pos+ROW_LENGTH+7]
    pos += 10
    #Right thing
    right_thing = [pos, pos+1, pos+ROW_LENGTH*1+2, pos+ROW_LENGTH*1+4, pos+ROW_LENGTH*2+4, pos-ROW_LENGTH*1+0, pos-ROW_LENGTH*1+1, pos-ROW_LENGTH*2+0, pos-ROW_LENGTH*2+1, pos-ROW_LENGTH*3+2, pos-ROW_LENGTH*3+4,pos-ROW_LENGTH*4+4 ]
    pos = pos + 14 - ROW_LENGTH
    #Right square
    right_sqr = [pos, pos+1, pos - ROW_LENGTH, pos - ROW_LENGTH + 1]

    gun = left_circ + left_sqr + right_sqr + right_thing

    for x in gun:
        mtrx[x] = ALIVE



def gliding_gun_left(mtrx, pos):
    # Left square
    left_sqr = [pos, pos-1, pos-ROW_LENGTH, pos-ROW_LENGTH-1,]
    pos -= 10
    #Left circle
    left_circ = [pos, pos-ROW_LENGTH, pos-ROW_LENGTH*2, pos-ROW_LENGTH*3-1, pos-ROW_LENGTH*4-2, pos-ROW_LENGTH*4-3, pos-ROW_LENGTH*3-5, pos-ROW_LENGTH*2-6, pos-ROW_LENGTH*1-6, pos-6, pos+ROW_LENGTH*1-5, pos+ROW_LENGTH*2-3, pos+ROW_LENGTH*2-2, pos+ROW_LENGTH*1-1, pos-ROW_LENGTH*1-4, pos-ROW_LENGTH-7]
    pos -= 10
    #Right thing
    right_thing = [pos, pos-1, pos-ROW_LENGTH*1-2, pos-ROW_LENGTH*1-4, pos-ROW_LENGTH*2-4, pos+ROW_LENGTH*1-0, pos+ROW_LENGTH*1-1, pos+ROW_LENGTH*2-0, pos+ROW_LENGTH*2-1, pos+ROW_LENGTH*3-2, pos+ROW_LENGTH*3-4,pos+ROW_LENGTH*4-4 ]
    pos = pos - 14 + ROW_LENGTH
    #Right square
    right_sqr = [pos, pos-1, pos + ROW_LENGTH, pos + ROW_LENGTH - 1]

    gun = left_circ + left_sqr + right_sqr + right_thing

    for x in gun:
        mtrx[x] = ALIVE


matrix = [DEAD for i in range(0, MATRIX_SIZE)]
gliding_gun_right(matrix, 40 * ROW_LENGTH + ROW_LENGTH // 4)
gliding_gun_left(matrix, 70 * ROW_LENGTH + ROW_LENGTH - 110)
print(*[x for x in matrix], sep='')

while True:
    tmp = copy.deepcopy(matrix)
    for x in range(len(matrix)):
        tmp[x] = (next_state(x, matrix))
    matrix = copy.deepcopy(tmp)
    print(*[CLR + x for x in matrix], sep='')
    sleep(0.05)
    #input()
    refresh()



#
# while True:
#     idx = random.randint(0, 6307)
#     MATRIX[idx] = random.choice(CHARACTERS)
#     tmp = MATRIX
#     for x in range(len(MATRIX)):
#         MATRIX[x] = tmp[(x + COUNTER) % (len(MATRIX) - 1)]
#     os.system("clear")
#     print(*[CLR + x for x in MATRIX])
#     sleep(0.1)
#

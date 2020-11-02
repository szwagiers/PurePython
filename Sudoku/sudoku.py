# Sudoku solver
from IPython.display import clear_output

b = [[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ''],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '], [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
         [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']]


def sudoku_board(board):
    clear_output()
    # print board with positions
    print(f'  1  |   2   |   3   |   4  |   5   |   6   |   7   |   8   |   9   ')
    print(f' {board[0][0]}   |   {board[1][0]}   |   {board[2][0]}   |  {board[3][0]}   |   {board[4][0]}   |   {board[5][0]}   |   {board[6][0]}   |   {board[7][0]}   |   {board[8][0]}')
    print('--------------------------------------------------------------------')
    print(f' {board[0][1]}   |   {board[1][1]}   |   {board[2][1]}   |  {board[3][1]}   |   {board[4][1]}   |   {board[5][1]}   |   {board[6][1]}   |   {board[7][1]}   |   {board[8][1]}')
    print('--------------------------------------------------------------------')
    print(f' {board[0][2]}   |   {board[1][2]}   |   {board[2][2]}   |  {board[3][2]}   |   {board[4][2]}   |   {board[5][2]}   |   {board[6][2]}   |   {board[7][2]}   |   {board[8][2]}')
    print('--------------------------------------------------------------------')
    print(f' {board[0][3]}   |   {board[1][3]}   |   {board[2][3]}   |  {board[3][3]}   |   {board[4][3]}   |   {board[5][3]}   |   {board[6][3]}   |   {board[7][3]}   |   {board[8][3]}')
    print('--------------------------------------------------------------------')
    print(f' {board[0][4]}   |   {board[1][4]}   |   {board[2][4]}   |  {board[3][4]}   |   {board[4][4]}   |   {board[5][4]}   |   {board[6][4]}   |   {board[7][4]}   |   {board[8][4]}')
    print('--------------------------------------------------------------------')
    print(f' {board[0][5]}   |   {board[1][5]}   |   {board[2][5]}   |  {board[3][5]}   |   {board[4][5]}   |   {board[5][5]}   |   {board[6][5]}   |   {board[7][5]}   |   {board[8][5]}')
    print('--------------------------------------------------------------------')
    print(f' {board[0][6]}   |   {board[1][6]}   |   {board[2][6]}   |  {board[3][6]}   |   {board[4][6]}   |   {board[5][6]}   |   {board[6][6]}   |   {board[7][6]}   |   {board[8][6]}')
    print('--------------------------------------------------------------------')
    print(f' {board[0][7]}   |   {board[1][7]}   |   {board[2][7]}   |  {board[3][7]}   |   {board[4][7]}   |   {board[5][7]}   |   {board[6][7]}   |   {board[7][7]}   |   {board[8][7]}')
    print('--------------------------------------------------------------------')
    print(f' {board[0][8]}   |   {board[1][8]}   |   {board[2][8]}   |  {board[3][8]}   |   {board[4][8]}   |   {board[5][8]}   |   {board[6][8]}   |   {board[7][8]}   |   {board[8][8]}')
    print('--------------------------------------------------------------------')


def placeNumber():
    # get chosen number from number() function
    num = number()
    # get positions from position() function
    positions = position()
    # unpack first digit as X position
    positionX = positions[0]
    # unpack second digit as Y position
    positionY = positions[1]
    # check if number already in square 3x3
    if num in b[positionX]:
        print('')
        print(f'That number is already in {positionX} square.')
        placeNumber()
    else:
        for x in range(1, 2):
            for y in range(0, 2):
                if num == b[x][y]:
                    print('Number not allowed in this position.')
                    placeNumber()
                # place chosen number on X and Y position on board
                else:
                    b[positionX][positionY] = num


def number():
    number = input('Choose number from 1-9: ')
    return int(number)


def position():
    positionX, positionY = input('Choose position on board, in xy format: ').split()
    return int(positionX)-1, int(positionY)-1


placeNumber()

# game logic
while True:
    sudoku_board(b)
    placeNumber()

# def winCond(board):
#     if '' in board:
#         print('There are still free cells to fill.')
#     elif '' not in board:

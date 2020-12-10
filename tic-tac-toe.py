board = ['_', '_', "_",
         "_", '_', '_',
         ' ', ' ', ' ']
current_turn = 'X'
game_over = False


def handle_turn(turn):
    global current_turn
    if turn == 'X':
        current_turn = 'O'
    else:
        current_turn = 'X'


def check_game_over():
    check_diag()
    check_rows()
    check_columns()


def check_rows():
    global game_over
    if board[0] == board[1] == board[2] != '_':
        print('row1')
        game_over = True
    elif board[3] == board[4] == board[5] != '_':
        print('row2')
        game_over = True
    elif board[6] == board[7] == board[8] != ' ':
        print('row3')
        game_over = True


def check_columns():
    global game_over
    if board[0] == board[3] == board[6] != '_':
        print('column1')
        game_over = True
    elif board[1] == board[4] == board[7] != '_':
        print('column2')
        game_over = True
    elif board[2] == board[5] == board[8] != '_':
        print('column3')
        game_over = True


def check_diag():
    global game_over
    if board[0] == board[4] == board[8] != '_':
        print('dia1')
        game_over = True
    elif board[2] == board[4] == board[6] != '_':
        print('dia3')
        game_over = True


def check_draw():
    global game_over
    if '_' not in board and ' ' not in board:
        game_over = True


while not game_over:
    print(board[0] + '|' + board[1] + '|' + board[2] + '\n' +
          board[3] + '|' + board[4] + '|' + board[5] + '\n' +
          board[6] + '|' + board[7] + '|' + board[8])
    while True:
        try:
            user_input = input(f'Player {current_turn}\'s turn Enter [1-9] ')
            if 9 >= int(user_input) >= 1:
                if board[int(user_input) - 1] == ' ' or board[int(user_input) - 1] == '_':
                    break
        except ValueError:
            pass
    user_input = int(user_input) - 1
    board[user_input] = current_turn
    check_game_over()
    check_draw()
    handle_turn(current_turn)

if '_' not in board and ' ' not in board:
    print('It is a draw')
else:
    handle_turn(current_turn)
    print(board[0] + '|' + board[1] + '|' + board[2] + '\n' +
          board[3] + '|' + board[4] + '|' + board[5] + '\n' +
          board[6] + '|' + board[7] + '|' + board[8])
    print(f'{current_turn} wins')

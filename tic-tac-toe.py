import random

board = ['_', '_', "_",
         "_", '_', '_',
         ' ', ' ', ' ']
# current_turn = random.choice(['X', 'O'])
current_turn = 'X'
game_over = False
ls = [0, 1, 2, 3, 4, 5, 6, 7, 8]
var = False


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
        game_over = True
    elif board[3] == board[4] == board[5] != '_':
        game_over = True
    elif board[6] == board[7] == board[8] != ' ':
        game_over = True


def check_columns():
    global game_over
    if board[0] == board[3] == board[6] != '_':
        game_over = True
    elif board[1] == board[4] == board[7] != '_':
        game_over = True
    elif board[2] == board[5] == board[8] != '_':
        game_over = True


def check_diag():
    global game_over
    if board[0] == board[4] == board[8] != '_':
        game_over = True
    elif board[2] == board[4] == board[6] != '_':
        game_over = True


def check_draw():
    global game_over
    if '_' not in board and ' ' not in board:
        game_over = True


while not game_over:

    while True:
        if current_turn == 'X':
            print('Computer turn')
            if len(ls) == 9:
                board[0] = 'X'
                ls.remove(0)
                handle_turn(current_turn)
                break
            if board[2] == 'O' or board[6] == 'O' or board[8] == 'O':
                if board[2] == 'O':
                    if board[6] == ' ':
                        board[6] = 'X'
                        handle_turn(current_turn)
                        break
                    if board[3] == '_':
                        board[3] = 'X'
                        check_game_over()
                        handle_turn(current_turn)
                        var = True
                        break
                    else:
                        if board[8] == ' ':
                            board[8] = 'X'
                            handle_turn(current_turn)
                            break
                        elif board[4] == '_':
                            board[4] = 'X'
                            handle_turn(current_turn)
                            check_game_over()
                            var = True
                            break
                        else:
                            board[7] = 'X'
                            check_game_over()
                            handle_turn(current_turn)
                            var = True
                            break
            if board[4] != 'O':
                if board[5] == 'O' or board[1] == 'O' or board[7] == 'O' or board[3] == 'O':
                    if board[4] == '_':
                        board[4] = 'X'
                        ls.remove(4)
                        handle_turn(current_turn)
                        break
                    if board[8] != 'O':
                        board[8] = 'X'
                        ls.remove(8)
                        check_game_over()
                        var = True
                        handle_turn(current_turn)
                        break
                    elif board[8] == 'O':
                        if board[1] == 'O' or board[7] == 'O':
                            if board[6] == ' ':
                                board[6] = 'X'
                                handle_turn(current_turn)
                                break
                            if board[2] == 'O':
                                board[3] = 'X'
                                check_game_over()
                                handle_turn(current_turn)
                                var = True
                                break
                            else:
                                board[2] = 'X'
                                check_game_over()
                                handle_turn(current_turn)
                                var = True
                                break
                        else:
                            if board[2] == '_':
                                board[2] = 'X'
                                handle_turn(current_turn)
                                break
                            if board[1] == 'O':
                                board[6] = 'X'
                                check_game_over()
                                handle_turn(current_turn)
                                var = True
                                break
                            else:
                                board[1] = 'X'
                                check_game_over()
                                handle_turn(current_turn)
                                var = True
                                break

    if var:
        continue
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
    print(board[0] + '|' + board[1] + '|' + board[2] + '\n' +
          board[3] + '|' + board[4] + '|' + board[5] + '\n' +
          board[6] + '|' + board[7] + '|' + board[8])

if '_' not in board and ' ' not in board:
    print('It is a draw')
else:
    handle_turn(current_turn)
    print(board[0] + '|' + board[1] + '|' + board[2] + '\n' +
          board[3] + '|' + board[4] + '|' + board[5] + '\n' +
          board[6] + '|' + board[7] + '|' + board[8])
    print(f'{current_turn} wins')

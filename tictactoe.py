print('Welcome to Tic Tac Toe!')

#1
def display_board(board):
    print('\n'*5)
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('---|---|---')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('---|---|---')
    print('  ' + board[1] + '  |  ' + board[2] + ' | ' + board[3])

#2
player1 = ''
player2 = ''

def player_input():
    #choose X or O
    global player1,player2
    marker = ''
    while marker != 'X' and marker != 'O':
        marker = input('player 1 - choose X or O:-').upper()
    player1 = marker

    if player1 == 'X':
        player2 = 'O'
    else:
        player2 = 'X'

    print('player1 marker = ' , player1)
    print('player2 marker = ' , player2)

#3
import random
def choose_first():
    #chooses who'll play first
    global player1,player2
    x = random.randint(0,1)
    if x == 0:
        return player1
    else:
        return player2

#4
def place_marker(board,mark,pos):
    board[pos] = mark


#5
def space_check(board, pos):
    return board[pos] == ''

#6
def full_board_check(board):
    if '' in board:
        return False
    else:
        return True


#7
def win_check(board, mark):
    return ((board[1] == mark and board[2] == mark and board[3] == mark) or (board[4] == mark and board[5] == mark and board[6] == mark) or (board[7] == mark and board[8] == mark and board[9] == mark) or (board[1] == mark and board[4] == mark and board[7] == mark) or (board[2] == mark and board[5] == mark and board[8] == mark) or (board[3] == mark and board[6] == mark and board[9] == mark) or (board[1] == mark and board[5] == mark and board[9] == mark) or (board[3] == mark and board[5] == mark and board[7] == mark))

#8
def replay():
    again = input('play again:Y or N').upper()
    if again == 'Y':
        return True
    return False

#9
def play_chance(board,player):
    position = int(input('Enter position number ({}):'.format(player)))
    while(not space_check(board,position)):
        print('position is not free')
        position = int(input('Enter position number ({}):'.format(player)))
    place_marker(board,player,position)
    display_board(board)
    if win_check(board,player):
        print(player + ' wins..')
        return True
    return False

def player_choice(board):
    global player1,player2
    if player1 == choose_first():
        print('player 1 goes first..')
        while(not full_board_check(board)):
            print('Player 1',end = ' ')
            if play_chance(board,player1):
                break            
            if full_board_check(board) and not win_check(board,player1):
                print('it\'s a draw')
                return
            print('player 2',end = ' ')
            if play_chance(board,player2):
                break
        if not win_check(board,player1) and not win_check(board,player2) and full_board_check:
            print('it\'s a draw') 
            return 

    else:
        print('player 2 goes first..')
        while(not full_board_check(board)):
            print('player 2',end = ' ')
            if play_chance(board,player2):
                break
            if full_board_check(board) and not win_check(board,player2):
                print('it\'s a draw')
                return
            print('player 1',end = ' ')
            if play_chance(board,player1):
                break
        if not win_check(board,player1) and not win_check(board,player2) and full_board_check:
            print('it\'s a draw')
            return 


while True:
    board_list = ['']*10
    board_list[0] = '#'
    display_board(board_list)
    
    player_input()

    player_choice(board_list)

    if not replay():
        break
    continue

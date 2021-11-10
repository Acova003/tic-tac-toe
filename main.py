import time
import sys
board = {
    '1': ' ' , '2': ' ' , '3': ' ' ,
    '4': ' ' , '5': ' ' , '6': ' ' ,
    '7': ' ' , '8': ' ' , '9': ' '
}
count = 0
win0 = ["1","4","7"]
win1 = ["1","5","9"]
win2 = ["1","2","3"]
#computer always starts in the first space
computer_moves = ["1"]

def draw_board():
    print("\n")
    print(f"{board['1']} | {board['2']} | {board['3']} ")
    print("---------")
    print(f"{board['4']} | {board['5']} | {board['6']} ")
    print("---------")
    print(f"{board['7']} | {board['8']} | {board['9']} ")
    print("\n")

def is_valid(m):
    return m in range (1,10)

def is_available(m):
    return board[m] == ' '

def error_message(m):
    if is_valid(int(m)) == False:
        print("\n")
        print("ERROR: Input has to be a valid number")
    elif is_available(m) == False:
        print("\n")
        print("ERROR: Space already taken")

def make_move(m):
    global board
    global count
    if count % 2 == 0:
        board[m] = "O"
    else:
        board[m] = "X"

def is_winner():
    return ((computer_moves == win0) or
            (computer_moves == win1) or
            (computer_moves == win2) or
            (computer_moves == win2))

def is_full():
    global count
    return count == 9

def player_2():
    print("Player 2's move")
    print("Choose a number between 1-9")
    move = input()
    if is_valid(int(move)) == True and is_available(move) == True:
        global count
        count += 1
        make_move(move)
        draw_board()
        computer()
    else:
        error_message(move)
        draw_board()
        player_2()

def computer():
    global count
    print("Computer's move")
    if count == 0:
        move = "1"
    else:
        print("Choose a number between 1-9")
        move = input()
    if is_valid(int(move)) == True and is_available(move) == True:
        count += 1
        computer_moves.append(move)
        make_move(move)
        draw_board()
        # check for winner or cat game
        if is_winner() == True:
            print("Computer wins!")
            sys.exit()
        elif is_full() == True:
            print('Cat game! It\'s a tie')
            sys.exit()
        else:
            print(board)
            player_2()
    else:
        error_message(move)
        draw_board()
        computer()

    draw_board()

def play():
    print("Welcome to tic tac toe!")
    draw_board()
    time.sleep(1)
    computer()
play()

user_input = input(" Do you choose X or O? ")
input_position = input(" Where would you like to place it? Enter a number between 1 and 9: ")

def show_options():
    if user_input == 'x'.lower():
        print(user_input)
    if int(input_position) in range(1, 10):
        print(input_position)
show_options()

def display_board(board):
    board[int(input_position)] += user_input
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])

display_board ([' '] *10)



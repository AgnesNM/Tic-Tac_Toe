user_input = input(" Do you choose X or O? ")
def show_options():
    if user_input == 'x'.lower():
        print(user_input)
show_options()

def display_board(board):
    for n,z in enumerate(board):
        board[n] += user_input
    print((' | ' + board[n] + ' | ')*3, "\n")
    print((' | ' + board[n] + ' | ') * 3, "\n")
    print((' | ' + board[n] + ' | ') * 3, "\n")
    #print(' | ' + board[7] + ' | ' + board[8] + ' | ' + board[9] + ' | ')
    #print(' | ' + board[4] + ' | ' + board[5] + ' | ' + board[6] + ' | ')
    #print(' | ' + board[1] + ' | ' + board[2] + ' | ' + board[3] + ' | ')
display_board ([' '] *10)


#collecting user input


n = 0
lst_user_input = [ ]
while n<3:
    user_input = input(" Do you choose X or O? ")
    input_position = input(" Where would you like to place it? Enter a number between 1 and 9: ")
    n+=1
    lst_user_input.append(user_input)
    break



def display_board(board):
    for index, num in enumerate(board):
        if index == int(input_position):
            for z in lst_user_input:
                board[int(input_position)] += lst_user_input[0]
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])

display_board ([' '] *10)



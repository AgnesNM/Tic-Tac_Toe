def repeat ():
    n = 0 #player chances to place an x or o
    global lst_user_input
    lst_user_input = []
    while n <= 3:
        global user_input
        user_input = input(" Do you choose X or O? ")
        global input_position
        input_position = input(" Where would you like to place it? Enter a number between 1 and 9: ")
        print(int(input_position))
        n += 1

        lst_user_input.append(user_input)
        break
repeat()

def display_board(board):
    for index, num in enumerate(board):
        if index == int(input_position):
            for z in lst_user_input:
                board[int(input_position)] += lst_user_input[0]
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])

display_board ([' '] *10)


#we need to call the updated board
repeat()
display_board ([' '] *10)




user_input_lst = []
def display_board(board):
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])

display_board ([' '] *10)

def repeat ():    
    global user_input
    user_input = input("Do you choose X or O? ")    
    global input_position
    input_position = input("Where would you like to place it? Enter a number between 1 and 9: ")
    
repeat()

def collect_input():    
    user_input_lst.append(user_input)
    print(f"user input is {user_input_lst}")
collect_input()

def updated_board(board):
    for index in range(len(board)):
        if index == int(input_position):
            board[int(input_position)] += user_input
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])
    return board

newest = updated_board([' '] *10)

def rounds():
    r = 8
    '''print the updated board'''
    while r>0:
        repeat()    
        collect_input()
        def latest_board(newest):
            for var in range(len(newest)):
                if var == int(input_position):
                    newest[int(input_position)] += user_input
                    print(newest[7] + ' | ' + newest[8] + ' | ' + newest[9])
                    print(newest[4] + ' | ' + newest[5] + ' | ' + newest[6])
                    print(newest[1] + ' | ' + newest[2] + ' | ' + newest[3])
            return newest

        latest_board(newest)
        r-=1
        
rounds()


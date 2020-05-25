user_input_lst = []
user_pos_lst = [ ]


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
    user_pos_lst.append(int(input_position))    

collect_input()

def combos_horizontal(lst):    
    if user_pos_lst in lst:
        print(f"player 1 wins!")     

def combos_vertical(ver_lst):    
    if user_pos_lst in ver_lst:
        print(f"player 1 wins!")   

def combos_diagonal(diag_lst):
    print(f"These are the positions {user_pos_lst}")
    if user_pos_lst in diag_lst:
        print(f"player 1 wins!")
    

def winner():
    '''DECLARE A WINNER IF USER ENTERS 3 CONSECUTIVE X's OR O's'''
    global code_x
    code_x = ['x','x','x']
    code_o = ['o','o','o']
    for user in range(len(user_input_lst)):
        if user_input_lst == code_x:            
            print(f"You entered 3 {user_input_lst[user]}'s! You win")

        elif user_input_lst == code_o:
           print(f"You entered 3 {user_input_lst[user]}'s! You win")

        '''HORIZONTAL INDEX POSITION COMBINATIONS FOR CHECKING FOR WINNER'''   

        combos_horizontal([[9,8,7], [6,5,4], [3,2,1], [7,8,9], [4,5,6], [1,2,3]])

        combos_vertical([[1,4,7], [2,5,8], [3,6,9], [7,4,1], [8,5,2], [3,6,9]])
        
        combos_diagonal([[9,5,1], [7,5,3], [1,5,9], [3,5,7]])
        break    

winner()   


def updated_board(board):
    '''PRINT THE UPDATED BOARD'''
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
    '''PRINT THE LATEST BOARD'''
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

        if not winner() and r<=6:
            break         

rounds()


player_1_input_lst = []
player_2_input_lst = []
player_1_pos_lst = [ ]
player_2_pos_lst = [ ]


def display_board(board):
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])

display_board ([' '] *10)

def choose_players():
    global player
    player = input("Choose player 1 or player 2: ")
    if player == "player 1":
        print(f"Start the game, {player}")
    elif player == "player 2":
        print(f"Start the game, {player}")  


def repeat ():
    while not choose_players():
        break    
    global user_input
    user_input = input("Do you choose X or O? ")    
    global input_position
    input_position = input("Where would you like to place it? Enter a number between 1 and 9: ")
    
repeat()


def collect_input():  
    if player == "player 1":
        player_1_input_lst.append(user_input)
        player_1_pos_lst.append(int(input_position))        
    elif player == "player2":
        player_2_input_lst.append(user_input)
        player_2_pos_lst.append(int(input_position))    

collect_input()


""" def winner1():
    '''DECLARE A WINNER IF USER ENTERS 3 CONSECUTIVE X's OR O's'''
    #global code_x
    
    hor_lst = [[9,8,7], [6,5,4], [3,2,1], [7,8,9], [4,5,6], [1,2,3]]
    ver_lst = [[1,4,7], [2,5,8], [3,6,9], [7,4,1], [8,5,2], [3,6,9]]
    diag_lst = [[9,5,1], [7,5,3], [1,5,9], [3,5,7]]


    code_x = ['x','x','x']
    code_o = ['o','o','o']

    '''CHECKING WHETHER PLAYER 1 IS THE WINNER'''
    '''THE Xs COMBINATION'''

    for user in range(len(player_1_input_lst)):
        if player_1_input_lst == code_x and player_1_pos_lst in hor_lst:
            print(f"Player 1 entered 3 {player_1_input_lst[user]}'s! at positions {player_1_pos_lst} Player 1 wins")

            break

        elif player_1_input_lst == code_x and player_1_pos_lst in ver_lst:
            print(f"Player 1 entered 3 {player_1_input_lst[user]}'s! at positions {player_1_pos_lst} Player 1 wins")

            break

        elif player_1_input_lst == code_x and player_1_pos_lst in diag_lst:
            print(f"Player 1 entered 3 {player_1_input_lst[user]}'s! at positions {player_1_pos_lst} Player 1 wins")

            break

        #THE O's COMBINATION
        elif player_1_input_lst == code_o and player_1_pos_lst in hor_lst:
            print(f"Player 1 entered 3 {player_1_input_lst[user]}'s! at positions {player_1_pos_lst} Player 1 wins")

            break

        elif player_1_input_lst == code_o and player_1_pos_lst in ver_lst:
            print(f"Player 1 entered 3 {player_1_input_lst[user]}'s! at positions {player_1_pos_lst} Player 1 wins")

            break

        elif player_1_input_lst == code_o and player_1_pos_lst in diag_lst:
            print(f"Player 1 entered 3 {player_1_input_lst[user]}'s! at positions {player_1_pos_lst} Player 1 wins")

            break      
        
        

winner1()    """


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

                code_x = ['x', 'x', 'x' ]
                code_o = ['o', 'o', 'o']
                if (code_x == player_1_input_lst) or (code_o == player_1_input_lst):
                    print(f"yea")
                    #if player_1_pos_lst = var

                                                     
                            
            return newest 
            #break

             
            
        latest_board(newest)
        r-=1

              
        
rounds()


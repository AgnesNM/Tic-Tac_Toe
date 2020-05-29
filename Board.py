'''GLOBAL VARIABLES'''

ongoing_game = True

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
    
    '''PRINT THE LATEST BOARD'''
    while ongoing_game:
        repeat()    
        collect_input()

        def latest_board(newest):
            for var in range(len(newest)):
                if var == int(input_position):
                    newest[int(input_position)] += user_input

                    #print(f"this is {newest.index(newest[int(input_position)])}")
                    
                    print(newest[7] + ' | ' + newest[8] + ' | ' + newest[9])
                    print(newest[4] + ' | ' + newest[5] + ' | ' + newest[6])
                    print(newest[1] + ' | ' + newest[2] + ' | ' + newest[3])                        
                                      
            return newest 
                      
        latest_board(newest)              
        
rounds()


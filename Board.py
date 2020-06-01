print("Welcome to Tic Tac Toe")

def display_board(board):
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])

display_board ([' '] *10)

'''GLOBAL VARIABLES'''

ongoing_game = True

#player 1 input 
player_1_input_lst = []

#player 2 input 
player_2_input_lst = []


def choose_players():
    global player
    player = input("Choose player 1 or player 2: ")
    
    if player == "player 1":
        print(f"Start the game, {player}")
    
    elif player == "player 2":
        print(f"Start the game, {player}")
    else:
        print(f"Please enter player 1 or player 2")
        choose_players()
              


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

    elif player == "player2":
        player_2_input_lst.append(user_input)
        
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
#print(f"This is newest: {newest}")


def rounds():
    
    '''PRINT THE LATEST BOARD'''
    global ongoing_game

    while ongoing_game:
        repeat() 
        collect_input()   
        
        def latest_board(newest):
            for var in range(len(newest)):
                if var == int(input_position):
                    newest[int(input_position)] += user_input
                                       
                    print(newest[7] + ' | ' + newest[8] + ' | ' + newest[9])
                    print(newest[4] + ' | ' + newest[5] + ' | ' + newest[6])
                    print(newest[1] + ' | ' + newest[2] + ' | ' + newest[3])   

            '''FUNCTIONS TO CHECK FOR THE WINNER'''                                 

            def check_rows():
                row_1 = newest[7] == newest[8] == newest[9] != ' '
                row_2 = newest[4] == newest[5] == newest[6] != ' '
                row_3 = newest[1] == newest[2] == newest[3] != ' '

                if row_1 or row_2 or row_3:
                    print(f"{player} wins")
                    #break
                    
                    global ongoing_game
                    ongoing_game = False

            check_rows()


            def check_columns():
                col_1 = newest[7] == newest[4] == newest[1] != ' '
                col_2 = newest[8] == newest[5] == newest[2] != ' '
                col_3 = newest[9] == newest[6] == newest[3] != ' '

                if col_1 or col_2 or col_3:
                    print(f"{player} wins")
                    #break
                    
                    global ongoing_game
                    ongoing_game = False

            check_columns()


            def check_diagonals():
                diag_1 = newest[9] == newest[5] == newest[1] != ' '
                diag_2 = newest[7] == newest[5] == newest[3] != ' '                

                if diag_1 or diag_2:
                    print(f"{player} wins")
                    #break
                    
                    global ongoing_game
                    ongoing_game = False

            check_diagonals()

            def check_draw():
                if not (check_rows() and check_columns() and check_diagonals()) and (not ' ' in newest[1:]):
                    print(f"It's a draw")

                    global ongoing_game
                    ongoing_game = False

            check_draw()                    
             
        latest_board(newest)       

rounds()
print("Welcome to Tic Tac Toe")

def game_intro():
    print(("_"*6) + "\t" + "    _____" + "\t" + "_____" + ("   ____"*2) + "\t" )
    print(("   |")*3 + "\t" + "\t  | " + "   |" + "___" + "|" + "  |")    
    print(("   |")*3 + "\t" + "\t  | " + ("   |"*2) + "  |")
    print(("   |")*3 + "_____" + "\t" + "  | " + ("   |"*2) + "  |" + "____" + "\n")
game_intro()    

def display_board(board):
    print(board[7] + ' | ' + board[8] + ' | ' + board[9])
    print(board[4] + ' | ' + board[5] + ' | ' + board[6])
    print(board[1] + ' | ' + board[2] + ' | ' + board[3])

display_board ([' '] *10)

'''GLOBAL VARIABLES'''

ongoing_game = True

#player 1 input position
player_1_pos_lst = set ()

#player 2 input position
player_2_pos_lst = set()


def game(): 

    '''FUNCTION TO CHOOSE PLAYERS'''

    def choose_players():
        global player
        player = input("Choose player 1 or player 2: ").lower()
    
        if player == "player 1":
            print(f"Start the game, {player}")            
    
        elif player == "player 2":
            print(f"Start the game, {player}")            
        
        else:
            print(f"Please enter player 1 or player 2")
            choose_players()
              
    '''FUNCTION TO ALLOW PLAYERS TO CHOOSE X OR O AND THEIR POSITIONS ON THE BOARD'''

    def collect_input ():
        while not choose_players():
            break    
    
        global user_input          
        user_input = input("Do you choose X or O? ").lower()

        if user_input == "x" or user_input == "o":
            print(f"Your input is {user_input}")
    
        else:
            print(f"Please choose 'x' or 'o'")
            collect_input()
     
        global input_position
        input_position = int(input("Where would you like to place it? Enter a number between 1 and 9: "))

        if input_position in [1,2,3,4,5,6,7,8,9] and player == "player 1" != ' ':
            if input_position not in player_1_pos_lst:
                player_1_pos_lst.update([input_position])                

            else:
                print(f"{player_1_pos_lst} is already taken, please choose another number between 1 and 9")
                collect_input()
                       
        elif input_position in [1,2,3,4,5,6,7,8,9] and player == "player 2" != ' ':
            if input_position not in player_2_pos_lst:
                player_2_pos_lst.update([input_position])                

            else:
                print(f"{player_2_pos_lst} is already taken, please choose another number between 1 and 9")
                collect_input() 

        else:
            print(f"Please enter a number between 1 and 9")
            collect_input()
    
    collect_input()

    def updated_board(board):

        '''PRINT THE UPDATED BOARD'''

        for index in range(len(board)):
            if (index == input_position):
                board[input_position] += user_input
        print(board[7] + ' | ' + board[8] + ' | ' + board[9])
        print(board[4] + ' | ' + board[5] + ' | ' + board[6])
        print(board[1] + ' | ' + board[2] + ' | ' + board[3])
        return board

    newest = updated_board([' '] *10)   
    
    '''PRINT THE LATEST BOARD'''
    
    global ongoing_game

    while ongoing_game:         
        collect_input()   
        
        def latest_board(newest):
            for var in range(len(newest)):
                if var == input_position:
                    newest[input_position] += user_input
                                       
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
                                        
                    global ongoing_game
                    ongoing_game = False

            check_rows()


            def check_columns():
                col_1 = newest[7] == newest[4] == newest[1] != ' '
                col_2 = newest[8] == newest[5] == newest[2] != ' '
                col_3 = newest[9] == newest[6] == newest[3] != ' '

                if col_1 or col_2 or col_3:
                    print(f"{player} wins")
                                        
                    global ongoing_game
                    ongoing_game = False

            check_columns()


            def check_diagonals():
                diag_1 = newest[9] == newest[5] == newest[1] != ' '
                diag_2 = newest[7] == newest[5] == newest[3] != ' '                

                if diag_1 or diag_2:
                    print(f"{player} wins")
                                        
                    global ongoing_game
                    ongoing_game = False

            check_diagonals()

            '''FUNCTION TO CHECK FOR A DRAW'''

            def check_draw():
                if not (check_rows() and check_columns() and check_diagonals()) and (not ' ' in newest[1:]):
                    print(f"It's a draw")

                    global ongoing_game
                    ongoing_game = False

            check_draw()                    
             
        latest_board(newest)

    '''FUNCTION TO RESTART THE GAME'''

    def restart_game():
        start = input("Do you want to play another game? ").lower()
        
        if start == "no":        
            global ongoing_game
            ongoing_game = False

        elif start == "yes":            
            ongoing_game = True
            game()
                
    restart_game()        

game()


        
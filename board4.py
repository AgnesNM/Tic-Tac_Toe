'''GLOBAL VARIABLES'''

player = "x" or "o"

#global ongoing_game
ongoing_game = True

#player 1 inputs
player_1_input_lst = []

#player 1 input position
player_1_pos_lst = set ()

#player 2 inputs
player_2_input_lst = []

#player 2 input position
player_2_pos_lst = set()


class Game():
    
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2

    def game_intro():
        print(("_"*6) + "\t" + "    _____" + "\t" + "_____" + ("   ____"*2) + "\t" + ("_"*5) + "\t" + ("_"*3) + "\t" + ("_")*5)
        print(("   |")*3 + "\t" + "\t  | " + "   |" + "___" + "|" + "  |" + "\t\t"+ "  |" + ("   | ")*2 + "\t" + "|" + "___")     
        print(("   |")*3 + "\t" + "\t  | " + ("   |"*2) + "  |" + "\t\t"+ "  |" + ("   | ")*2 + "\t" + "|")
        print(("   |")*3 + "_____" + "\t" + "  | " + ("   |"*2) + "  |" + "____" + "\t" + "  |" + "   | " + ("___") + "|" + "\t|" + "___" "\n")

        print("Welcome to Tic Tac Toe. To win the game, you need to get either 3 x's or o's in a row. Place your x or o in a corresponding position")

    game_intro()

    def display_board(board):
        print(board[7] + ' | ' + board[8] + ' | ' + board[9])
        print(board[4] + ' | ' + board[5] + ' | ' + board[6])
        print(board[1] + ' | ' + board[2] + ' | ' + board[3])

    display_board (['x','1','2','3','4','5','6','7','8','9'])

   
    '''FUNCTION TO KEEP TRACK OF GAME ROUNDS FOR THE SAKE OF CLEARING THE BOARD ON GAME RESTART'''
    def game_rounds (self):
        rounds  = int(input("Enter game round: "))
           
        if rounds > 1:
            player_1_pos_lst.clear()            
            player_2_pos_lst.clear()
            player_1_input_lst.clear()
            player_2_input_lst.clear()          
             
        return "game round func"    
    
    #print(game_rounds())

  
    def collect_input ():        
                      
        global user_input          
        user_input = input("Do you choose X or O? ").lower()

        if user_input == "x": 
            player_1_input_lst.append(user_input)
            player = "player 1"


        elif user_input == "o":  
            player_2_input_lst.append(user_input)
            player = "player 1"           
            
        else:
            print(f"Please choose 'x' or 'o'")
            collect_input()
        
        global input_position
        input_position = int(input("Where would you like to place it? Enter a number between 1 and 9: "))      
            
        if input_position in range(0,10) and player == "player 1" != ' ':
            global player_1_pos_lst
            if input_position not in player_1_pos_lst:
                player_1_pos_lst.update([input_position])  
                                

            else:
                print(f"{player_1_pos_lst} is already taken, please choose another number between 1 and 9")
                collect_input()
                        
        elif input_position in range(0,10) and player == "player 2" != ' ':
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


    while ongoing_game:             
        #choose_players()
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

    while True:
        restart = input("Do you want to play another game? ")
        if restart == "yes":
            game_intro()
            display_board (['x','1','2','3','4','5','6','7','8','9'])

            def clear_board(newest): 
                print("Here is the empty board to get you started: ")                  
                print(newest[7] + ' | ' + newest[8] + ' | ' + newest[9])
                print(newest[4] + ' | ' + newest[5] + ' | ' + newest[6])
                print(newest[1] + ' | ' + newest[2] + ' | ' + newest[3])

            clear_board([' '] *10)

            #game_rounds()            
            collect_input()
            newest = updated_board([' '] *10)

            ongoing_game = True
       
            while player_1_input_lst != ["x","x","x"]:
                if player_2_input_lst != ["o", "o", "o"]:             
                    collect_input()
                    latest_board(newest)
            continue

        elif restart == "no":
            print("Thanks for playing Tic Tac Toe")
            break
    

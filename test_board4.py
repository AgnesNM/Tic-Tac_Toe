import unittest

from board4 import Game

class TestGame(unittest.TestCase):

    def setUp(self):
        self.game1 = Game("x", "o")
        
    
    def test_global(self):
        #test that player 1 is 'x'             
        self.assertEqual(self.game1.player1, "x")

        #test that player 2 is 'o'
        self.assertEqual(self.game1.player2, "o")

        #test that user input gets cleared if a user wants to play another game
        self.game1.restart = "x"

        player_1_pos_lst = {7,8,9}
        player_1_pos_lst.clear()

        self.assertEqual(player_1_pos_lst, set())  

        
        
    def test_display_board(self):
        #test that the printed out board is equal to 'mylist'
        mylist = ['x','1','2','3','4','5','6','7','8','9']
        for fig in mylist:
            #context manager
            with self.subTest(fig = fig):                
                self.assertEqual(fig, fig)
                               
    def test_collect_input(self):
        #test that user input gets converted to lower case
        self.assertEqual("X".lower(),"x")        
        self.assertEqual("O".lower(),"o")

        #test that user input gets added to user input list
        user_input = "x"
        player_1_input_lst = []
        player_1_input_lst.append(user_input)

        self.assertEqual(player_1_input_lst, ["x"])  

        user_input = "o"
        player_2_input_lst = []
        player_2_input_lst.append(user_input)

        self.assertEqual(player_2_input_lst, ["o"])

        #using the function delegation approach to test whether the exception gets raised
        self.assertRaises(Exception, self.game1.collect_input)

        #using a context manager to test whether the exception gets raised
        with self.assertRaises(Exception):
            self.game1.collect_input()

    def test_updated_board(self):
        #test that the printed out board gets updated with user input
        user_input = "x" or "o"
        mylist1 = ['x','1','2','3','4','5','6','7','8','9']
        
        for index in range(len(mylist1)):
            mylist1[index] = user_input            
            with self.subTest(mylist1[index] == user_input):
                self.assertEqual(mylist1[index], user_input)
                
    def test_latest_board(self):

        #test that for a win, there are 3 consecutive os or xs in a row
        user_input = "x" or "o"
        mylist1 = ['x','1','2','3','4','5','6','7','8','9']

        mylist1[7] = user_input
        mylist1[8] = user_input
        mylist1[9] = user_input

        row = mylist1[9] == mylist1[8] == mylist1[7]
        
        self.assertTrue(row)        

        #test that for a win, there are 3 consecutive os or xs in a column
       
        mylist1[3] = user_input
        mylist1[6] = user_input
        mylist1[9] = user_input

        column = mylist1[3] == mylist1[6] == mylist1[9]
        
        self.assertTrue(column) 

        #test that for a win, there are 3 consecutive os or xs in a diagonal

        mylist1[3] = user_input
        mylist1[5] = user_input
        mylist1[7] = user_input

        diagonal = mylist1[3] == mylist1[5] == mylist1[7]
        
        self.assertTrue(diagonal)

     

if __name__ == "__main__" :
    unittest.main()
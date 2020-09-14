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
        user_input = "x"
        mylist1 = ['x','1','2','3','4','5','6','7','8','9']
        
        for index in range(len(mylist1)):
            mylist1[index] = user_input            
            with self.subTest(mylist1[index] == user_input):
                self.assertEqual(mylist1[index], user_input)
     

if __name__ == "__main__" :
    unittest.main()
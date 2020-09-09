import unittest

from board4 import Game

class TestGame(unittest.TestCase):

    def setUp(self):
        self.game1 = Game("x", "o") 
    
    def test_global(self):             
        self.assertEqual(self.game1.player1, "x")
        self.assertEqual(self.game1.player2, "o")

    def test_display_board(self):
        mylist = ['x','1','2','3','4','5','6','7','8','9']
        for fig in mylist:
            #context manager
            with self.subTest(fig = fig):                
                self.assertEqual(fig, fig)
                               
    def test_collect_input(self):
        self.assertEqual("X".lower(),"x")
        self.assertEqual("O".lower(),"o")       

if __name__ == "__main__" :
    unittest.main()
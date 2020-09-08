import unittest

from board4 import Game

class TestGame(unittest.TestCase):

    def setUp(self):
        self.game1 = Game("x", "o") 
    
    def test_global(self):             
        self.assertEqual(self.game1.player1, "x")

if __name__ == "__main__":
    unittest.main()
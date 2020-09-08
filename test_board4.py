import unittest

from board4 import Game

class TestGame(unittest.TestCase):

    def setUp(self):
        self.game1 = Game("x", "o")

    def test_clear_board(self):        
        self.assertTrue(self.game1.clear_board)

if __name__ == "__main__":
    unittest.main()
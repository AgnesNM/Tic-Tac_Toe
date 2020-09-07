import unittest

from board4 import Game

class TestBoard4(unittest.TestCase):
    def test_game_rounds(self):
        game2 = Game("x","o")      

        self.assertEqual(game2.game_rounds(), "game round func")

if __name__ == "__main__":
    unittest.main()
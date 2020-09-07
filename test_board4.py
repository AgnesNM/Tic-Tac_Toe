import unittest

from board4 import Game

class TestBoard4(unittest.TestCase):
    def test_game_rounds(self):
        game1 = Game("x","o")

        self.assertEqual(game1.game_rounds, set())

if __name__ == "__main__":
    unittest.main()
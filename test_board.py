import unittest

import Board

class TestBoard(unittest.TestCase):
    def test_global(self):
        self.assertIn(Board.input_position, range(0,9))

if __name__ == "__main__":
    unittest.main()
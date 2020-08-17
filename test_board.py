import unittest

import Board

class TestBoard(unittest.TestCase):
    def test_global(self):
        #self.assertIn(Board.input_position, range(0,9)) #this test only checks the user's last input
        self.assertEqual(Board.user_input, 'x' or 'o') #this test only checks the user's last input

if __name__ == "__main__":
    unittest.main()
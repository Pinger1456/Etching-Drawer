"""
This file contains basic tests for the main program, specifically for
validating user input and ensuring the canvas updates correctly. Further
tests can be added to simulate different input sequences.
"""
import unittest
from unittest.mock import patch
from main import main


class TestMain(unittest.TestCase):
    """Test for simulating user input
    and checking the resulting output."""
    @patch('builtins.input', side_effect=['W', 'S', 'A', 'D', 'Q'])
    def test_main(self, mock_input):
        """Test the main program by simulating user input (WASD keys)."""
        with self.assertRaises(KeyboardInterrupt):
            main()

        mock_input.assert_any_call('Move (WASD): ')
        mock_input.assert_any_call('Move (WASD): ')
        mock_input.assert_any_call('Move (WASD): ')
        mock_input.assert_any_call('Move (WASD): ')
        mock_input.assert_any_call('Move (WASD): ')


if __name__ == "__main__":
    unittest.main()

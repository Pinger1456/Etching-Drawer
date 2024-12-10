"""
Unit tests for canvas-related functions in the Etching Drawer program.

This file contains tests for the functions in the `canvas.py` module,
especially the `get_canvas_string` function, which converts canvas data
into a string that can be printed to the terminal.
"""

import unittest
from canvas import get_canvas_string


class TestCanvasFunctions(unittest.TestCase):
    """This class contains tests to verify the behavior of functions that deal
    with rendering and managing the canvas in the Etching Drawer program.
    Specifically, it includes tests for the `get_canvas_string` function
    which converts the canvas data into a string representation that can
    be printed to the terminal.
    """
    def test_get_canvas_string(self):
        """Tests the `get_canvas_string` function
        to ensure it correctly generates
        a string representation of the canvas, including the proper rendering
        of vertical and horizontal lines, and the cursor position."""
        canvas_data = {
            (0, 0): {'W'},
            (1, 1): {'S'},
        }
        result = get_canvas_string(canvas_data, 0, 0)
        self.assertIn('#', result)
        self.assertIn('│', result)
        self.assertIn('─', result)


if __name__ == "__main__":
    unittest.main()

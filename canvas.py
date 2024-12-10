"""
Functions for managing the canvas in the Etching Drawer program.

This file contains the logic for drawing the canvas, handling the
coordinates, and converting canvas data into a string that can be displayed
in the terminal.
"""

from config import UP_DOWN_CHAR, LEFT_RIGHT_CHAR, CANVAS_WIDTH, CANVAS_HEIGHT


def get_canvas_string(canvas_data, cx, cy):
    """
    Returns a multiline string of the line drawn in canvas_data.
    """
    canvas_str = ''
    for row_num in range(CANVAS_HEIGHT):
        for col_num in range(CANVAS_WIDTH):
            if col_num == cx and row_num == cy:
                canvas_str += '#'
                continue

            cell = canvas_data.get((col_num, row_num))
            if cell in ({'W', 'S'}, {'W'}, {'S'}):
                canvas_str += UP_DOWN_CHAR
            elif cell in ({'A', 'D'}, {'A'}, {'D'}):
                canvas_str += LEFT_RIGHT_CHAR
            else:
                canvas_str += ' '  # Empty space for no direction

        canvas_str += '\n'  # New line after each row
    return canvas_str

"""
Constants:
    - UP_DOWN_CHAR: Character used to draw vertical lines.
    - LEFT_RIGHT_CHAR: Character used to draw horizontal lines.
    - CANVAS_WIDTH: Width of the canvas, derived from the terminal size.
    - CANVAS_HEIGHT: Height of the canvas, adjusted for command space.
"""

import shutil


# Set up the constants for line characters
UP_DOWN_CHAR = chr(9474)  # Character '│'
LEFT_RIGHT_CHAR = chr(9472)  # Character '─'

# Define the canvas size based on terminal window size
CANVAS_WIDTH, CANVAS_HEIGHT = shutil.get_terminal_size()
CANVAS_WIDTH -= 1  # Avoid printing to last column on Windows
CANVAS_HEIGHT -= 5  # Leave room for command info

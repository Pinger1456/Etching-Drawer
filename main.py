"""Etching Drawer, by Al Sweigart al@inventwithpython.com
An art program that draws a continuous line around the screen using the
WASD keys. Inspired by Etch A Sketch toys
"""


from canvas import get_canvas_string


def main():
    """ Get the size of the terminal window """
    canvas = {}
    cursor_x, cursor_y = 0, 0

    while True:
        # Draw the canvas with the current cursor position
        print(get_canvas_string(canvas, cursor_x, cursor_y))

        # Get user input for movement (W, A, S, D)
        move = input("Move (WASD): ").upper()
        if move == 'W':
            cursor_y -= 1
        elif move == 'S':
            cursor_y += 1
        elif move == 'A':
            cursor_x -= 1
        elif move == 'D':
            cursor_x += 1
        else:
            print("Invalid input! Use 'W', 'A', 'S', or 'D'.")
            continue

        # Add the direction to the canvas
        if (cursor_x, cursor_y) not in canvas:
            canvas[(cursor_x, cursor_y)] = set()
        canvas[(cursor_x, cursor_y)].add(move)


if __name__ == "__main__":
    main()

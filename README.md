# Etching Drawer

Etching Drawer is a terminal-based art program inspired by the classic **Etch A Sketch** toy. It allows you to draw by moving a cursor using the **WASD** keys and leaves a continuous line on the screen, creating various artistic patterns.

## Features:
- Use **W**, **A**, **S**, and **D** to move a cursor and draw lines.
- Draw fractals like the **Hilbert Curve** by inputting predefined sequences of movements.
- Draw continuously without lifting the "pen".
- Exit the program by pressing **Q**.

## Installation

This project is written in Python 3 and does not have external dependencies beyond the standard library.

### Prerequisites
Ensure you have Python 3.6 or later installed. You can check if Python is installed by running:

```bash
python --version
```

### Clone the repository

Clone the repository to your local machine:

```bash
git clone https://github.com/your-username/etchingdrawer.git
cd etchingdrawer
```

## Usage

1. Run the program by executing:

```bash
python main.py
```

2. Once the program starts, you can use the following keys to control the cursor:
   - **W**: Move up
   - **S**: Move down
   - **A**: Move left
   - **D**: Move right
   - **Q**: Quit the program

3. You can draw by inputting commands in the terminal. For example, entering `SDWDDSASDSAAWASSDSASSDWDSDWWAWDDDSASSDWDSDWWAWDWWASAAWDWAWDDSDW` will draw a **Hilbert Curve**.

## Project Structure

The project has the following structure:

```
/etchingdrawer
    ├── main.py            # Main script to run the program
    ├── config.py          # Configuration file with constants and settings
    ├── canvas.py          # Functions to manage and render the canvas
    ├── requirements.txt   # List of dependencies (for future use)
    └── tests/
        ├── test_canvas.py # Unit tests for canvas-related functions
        └── test_main.py   # Unit tests for the main program
```

### `main.py`
The entry point of the program, where the canvas is initialized and the user input is processed to control the cursor and draw lines.

### `config.py`
Contains constants such as the canvas size and characters used for drawing.

### `canvas.py`
Handles the logic for drawing the canvas, converting canvas data into a printable string.

### `requirements.txt`
This file lists any Python dependencies for the project (currently none, as it only uses Python's standard library).

### `tests/`
Contains unit tests for verifying the functions in the program, such as those for generating the canvas string and handling user input.

## Running Tests

To run tests, you can use the `unittest` framework.

1. To run tests for the canvas module:
   ```bash
   python -m unittest tests.test_canvas
   ```

2. To run tests for the main module (which simulates user input):
   ```bash
   python -m unittest tests.test_main
   ```

## Contributing

Feel free to contribute by opening issues or submitting pull requests. Contributions are welcome!

1. Fork the repository
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -am 'Add new feature'`)
4. Push to the branch (`git push origin feature-branch`)
5. Create a new Pull Request

## License

This project is open source and available under the [MIT License](LICENSE).

---

If you have any questions or need help, feel free to reach out! 😊

from geometor.arcprize.puzzles import Puzzle, PuzzleSet, Grid
from rich import print
from datetime import datetime
from pathlib import Path
import json
import numpy as np
import os
from gemini_reporter import Reporter

import google.generativeai as genai

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

DEFAULT_MODEL = "models/gemini-1.5-flash"
#  DEFAULT_MODEL = "models/gemini-1.5-flash-002"
#  DEFAULT_MODEL = "models/gemini-1.5-pro-002"
DEFAULT_INSTRUCTIONS_FILE = "gemini_instructions.md"


def get_model(model_name=DEFAULT_MODEL, instructions_file=DEFAULT_INSTRUCTIONS_FILE):
    with open(instructions_file, "r") as f:
        instruction = f.read().strip()

    model = genai.GenerativeModel(
        model_name,
        system_instruction=instruction,
    )

    return model


def create_output_dir():
    """Create timestamped output directory for reports and logs"""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    output_dir = Path("outputs") / timestamp

    # Create main output directory
    output_dir.mkdir(parents=True, exist_ok=True)

    # Create subdirectories for different types of output
    (output_dir / "reports").mkdir(exist_ok=True)
    (output_dir / "logs").mkdir(exist_ok=True)

    return output_dir


def solve_all_puzzles(puzzle_set):
    output_dir = create_output_dir()
    print(f"Output directory: {output_dir}")

    for puzzle in puzzle_set.puzzles:
        solve_puzzle(puzzle, output_dir)


def log_prompt(prompt):
    print("-" * 40)
    print(prompt)


def log_response(response):
    print("-" * 20)
    print(response.to_dict())


class PuzzleSolver:
    def __init__(self, puzzle):
        self.puzzle = puzzle
        self.working_grid = None

    def initialize_output_from_input(self) -> str:
        """
        Initialize the test output grid with a copy of the input grid.
        """
        from copy import deepcopy

        self.working_grid = deepcopy(self.puzzle.test[0].input)
        return "initialize_output_from_input()"

    def initialize_output_by_size(self, width: int, height: int, color: int = 0) -> str:
        """
        Initialize the test output grid with a specific width and height filled
        with a color.
        """
        width = int(width)
        height = int(height)
        color = int(color)
        new_grid = np.full((height, width), int(color))
        self.working_grid = Grid(new_grid, self.puzzle.id, "test", 0, "output")
        return f"initialize_output_by_size({width=}, {height=}, {color=})"

    def set_pixel(self, row: int, column: int, color: int) -> str:
        """
        Set grid value at a specific coordinate.
        """
        height, width = self.working_grid.grid.shape
        row = int(row)
        column = int(column)
        color = int(color)

        if not (0 <= row < height):
            raise ValueError(f"Row {row} is out of bounds. Grid height is {height}")

        if not (0 <= column < width):
            raise ValueError(f"Column {column} is out of bounds. Grid width is {width}")

        self.working_grid.grid[row, column] = color
        return f"set_pixel({row=}, {column=}, {color=})"

    def set_range(
        self, row1: int, column1: int, row2: int, column2: int, color: int
    ) -> str:
        """
        Set grid values for a range of pixels by iterating through each cell.

        Args:
            row1: Starting row (inclusive)
            column1: Starting column (inclusive)
            row2: Ending row (inclusive)
            column2: Ending column (inclusive)
            color: Color value to set
        """
        # Convert to int and ensure proper order
        r1, r2 = sorted([int(row1), int(row2)])
        c1, c2 = sorted([int(column1), int(column2)])

        # Add 1 to end indices to make them inclusive
        r2 += 1
        c2 += 1

        # Ensure we're within grid bounds
        height, width = self.working_grid.grid.shape

        # Check if any part of the range is within bounds
        if (r1 >= height and r2 >= height) or (c1 >= width and c2 >= width):
            raise ValueError(f"Entire range is outside grid bounds ({height}x{width})")

        r1 = max(0, min(r1, height))
        r2 = max(0, min(r2, height))
        c1 = max(0, min(c1, width))
        c2 = max(0, min(c2, width))

        # Iterate through each cell in the range
        for row in range(r1, r2):
            for col in range(c1, c2):
                self.working_grid.grid[row, col] = int(color)

        cells_modified = (r2 - r1) * (c2 - c1)
        print(
            f"set_range: {cells_modified} cells modified from ({r1},{c1}) to ({r2-1},{c2-1})"
        )
        return f"set_range({row1}, {column1}, {row2}, {column2}, {color}) -> str:"

    def set_contiguous(self, row: int, column: int, color: int) -> str:
        """
        Set all contiguous pixels that are the same color as the selected pixel.
        """
        # TODO: Implement contiguous pixel setting
        print("set_contiguous")
        return "contiguous set"

    def submit(self) -> str:
        """
        Submit the working grid and check for correctness.
        """
        print("submit")
        return "submit"


def solve_puzzle(puzzle, output_dir):
    model = get_model()

    chat = model.start_chat(
        history=[
            {"role": "user", "parts": f"Begin puzzle: {puzzle.id}"},
            {"role": "model", "parts": "Ready"},
        ],
    )

    print("=" * 60)
    print(puzzle.id)

    # Process training examples
    for i, pair in enumerate(puzzle.train, 1):
        prompt = [
            f"# example_{i}\n",
            "## input\n",
            str(pair.input.grid),
            "\n",
            pair.input.to_image(),
            "\n",
            "## output\n",
            str(pair.output.grid),
            "\n",
            pair.output.to_image(),
            "\n",
        ]
        log_prompt(prompt)
        response = chat.send_message(prompt, tools="code_execution")
        log_response(response)

    # Summarize observations
    prompt = [
        "summarize your observations to explain the transformation of the input to output\n",
        "you may generate and run code to closely examine the patterns and differences in the grids\n",
    ]
    log_prompt(prompt)
    response = chat.send_message(prompt, tools="code_execution")
    log_response(response)

    solver = PuzzleSolver(puzzle)

    functions = {
        "initialize_output_from_input": solver.initialize_output_from_input,
        "initialize_output_by_size": solver.initialize_output_by_size,
    }

    # Present test input
    test_pair = puzzle.test[0]
    prompt = [
        "# test\n",
        "## input\n",
        str(test_pair.input.grid),
        "\n",
        test_pair.input.to_image(),
        "\n",
        "generate report as per instructions\n",
        "use code execution to investigate properties"

    ]
    log_prompt(prompt)
    response = chat.send_message(
        prompt,
        tools="code_execution",
    )
    log_response(response)

    # Initialize working grid
    prompt = [
        "initialize the working output grid",
    ]
    log_prompt(prompt)
    response = chat.send_message(
        prompt,
        tools=functions.values(),
    )
    log_response(response)

    # Process function call
    function_call = response.candidates[0].content.parts[0].function_call
    if function_call:
        result = call_function(function_call, functions)

        print(result)

    # Define functions for setting pixels
    functions = {
        "set_pixel": solver.set_pixel,
        "set_range": solver.set_range,
        #  "set_contiguous": solver.set_contiguous,
        "submit": solver.submit,
        # TODO: add undo last
    }

    prompt = [
        "clearing tools for next phase",
    ]
    log_prompt(prompt)
    response = chat.send_message(
        prompt,
        tools=None,
    )
    log_response(response)

    # Interaction loop
    for loop in range(5):
        print("LOOP:", loop)
        # first present the current working grid
        # TODO: after functions have been added to tools - can't return to code execution
        prompt = [
            "# working output grid\n",
            "updated with your changes\n",
            str(solver.working_grid.grid),
            "\n",
            solver.working_grid.to_image(),
            "\n",
            "take a moment to review that the changes are in keeping with the rule\n",
            #  "you can use code execution to analyze",
            #  "use code execution to investigate properties"
        ]
        log_prompt(prompt)
        response = chat.send_message(
            prompt,
            #  tools="code_execution",
        )
        log_response(response)

        # next select the function for next update
        prompt = [
            "select the next function to update the working grid\n",
            "when you think you have completed the output, call the submit function\n",
        ]
        log_prompt(prompt)
        response = chat.send_message(
            prompt,
            tools=functions.values(),
        )
        log_response(response)

        # Process function call
        function_call = response.candidates[0].content.parts[0].function_call
        print(function_call)
        if function_call:
            result = call_function(function_call, functions)

            print(result)
            if result == "submit":
                break

    #  print("\n\nHISTORY")
    #  print(chat.history)
    #  breakpoint()

    reporter = Reporter()
    report_path = reporter.generate(chat.history, puzzle.id, output_dir)
    print("report path:", report_path)


def call_function(function_call, functions):
    function_name = function_call.name
    function_args = function_call.args
    result = functions[function_name](**function_args)
    return result


def run():
    puzzle_set = PuzzleSet()
    print(f"Loaded {len(puzzle_set.puzzles)} puzzles")

    output_dir = create_output_dir()
    solve_all_puzzles(puzzle_set)
    #  solve_puzzle(puzzle_set.puzzles[0], output_dir)


if __name__ == "__main__":
    run()
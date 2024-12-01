from rich import print
from datetime import datetime
from pathlib import Path
import json
import os

from geometor.arcprize.puzzles import Puzzle, PuzzleSet, Grid
from geometor.arcprize.solvers.gemini_solver import PuzzleSolver


def solve_all_puzzles(puzzle_set, model_name):
    timestamp = datetime.now().strftime("%y.%j.%H%M%S")
    for puzzle in puzzle_set.puzzles:
        solver = PuzzleSolver(
            puzzle,
            timestamp=timestamp,
            output_dir="../docsrc",
            model_name=model_name,
            max_iterations=10,
        )
        solver.solve()


def run():
    puzzle_set = PuzzleSet()
    print(f"Loaded {len(puzzle_set.puzzles)} puzzles")

    #  model_name = "gemini-exp-1121"
    #  model_name = "models/gemini-exp-1114"
    model_name = "models/gemini-1.5-flash-002"

    #  solve_all_puzzles(puzzle_set, model_name)

    timestamp = datetime.now().strftime("%y.%j.%H%M%S")
    solver = PuzzleSolver(
        puzzle_set.puzzles[0],
        timestamp=timestamp,
        output_dir="../docsrc",
        model_name=model_name,
        max_iterations=10,
    )
    solver.solve()


if __name__ == "__main__":
    run()

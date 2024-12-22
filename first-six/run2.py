from rich import print
from datetime import datetime
from pathlib import Path
import numpy as np

from geometor.arcprize.puzzles import PuzzleSet
from geometor.arcprize.sessions.session import Session


def run():
    """Main execution function for ARC puzzle solving."""
    puzzle_set = PuzzleSet()
    print(f"Loaded {len(puzzle_set.puzzles)} puzzles")

    output_dir = "../docsrc"
    model_name = "gemini-2.0-flash-thinking-exp-1219"

    session = Session(
        puzzle_set=puzzle_set,
        output_dir=output_dir,
        model_name=model_name,
        max_iterations=10,
    )

    results = session.solve_puzzles()
    metrics = session.get_summary_metrics()

    # Calculate additional statistics
    accuracies = [result.accuracy for result in results.values()]
    metrics.update(
        {
            "min_accuracy": np.min(accuracies),
            "max_accuracy": np.max(accuracies),
            "std_accuracy": np.std(accuracies),
        }
    )

    print("\nBatch Results:")
    print(f"Total time: {metrics['total_time']:.2f}s")
    print(f"Puzzles solved: {metrics['puzzles_solved']}/{metrics['puzzles_attempted']}")
    print(f"Average accuracy: {metrics['average_accuracy']:.2f}%")
    print(
        f"Accuracy range: {metrics['min_accuracy']:.2f}% - {metrics['max_accuracy']:.2f}%"
    )
    print(metrics)
    print(results)


if __name__ == "__main__":
    run()

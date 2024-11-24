import os
from pathlib import Path
import re


def generate_session_summary(output_path, session_dir):
    """
    Generate an RST file containing a list-table summarizing the submission status and results of each puzzle.

    Parameters:
    output_path (str): Path to save the generated RST file.
    session_dir (str): Directory path where each subfolder is a puzzle.
    """
    session_path = Path(session_dir)
    puzzles = sorted(session_path.iterdir())

    # Header for RST file
    rst_content = [
        "results\n",
        "-------\n\n",
        ".. list-table::\n",
        "   :header-rows: 1\n\n",
        "   * - Puzzle\n",
        "     - Submission\n",
        "     - Size\n"
        "     - Colors\n",
        "     - Color Count Diff\n",
        "     - Pixel Accuracy\n\n"
    ]

    # Loop over each puzzle directory
    for puzzle in puzzles:
        if puzzle.is_dir():
            # Check if a submission file exists in the puzzle directory
            submission_files = list(puzzle.glob("*-submission.rst"))
            if submission_files:
                submission_file = submission_files[0]
                # Read the submission file and extract results
                with open(submission_file, "r") as file:
                    content = file.read()
                    size_correct = re.search(r":Size Correct: (True|False)", content)
                    colors_correct = re.search(r":Colors Correct: (True|False)", content)
                    unique_color_diff = re.search(r":Unique Color Count Diff: (\{.*?\})", content)
                    pixel_accuracy = re.search(r":Pixel Accuracy: ([\d\.]+)%", content)

                    size_correct = size_correct.group(1) if size_correct else ""
                    colors_correct = colors_correct.group(1) if colors_correct else ""
                    unique_color_diff = unique_color_diff.group(1) if unique_color_diff else ""
                    pixel_accuracy = pixel_accuracy.group(1) + "%" if pixel_accuracy else ""
            else:
                size_correct = ""
                colors_correct = ""
                unique_color_diff = ""
                pixel_accuracy = ""

            # Add row to the RST list-table
            rst_content.append(f"   * - {puzzle.name}\n")
            rst_content.append(f"     - {'Yes' if submission_files else 'No'}\n")
            rst_content.append(f"     - {size_correct}\n")
            rst_content.append(f"     - {colors_correct}\n")
            rst_content.append(f"     - {unique_color_diff}\n")
            rst_content.append(f"     - {pixel_accuracy}\n")

    # Write the summary to the output RST file
    with open(output_path, "w") as rst_file:
        rst_file.write("".join(rst_content))


if __name__ == "__main__":
    # Example usage
    session_directory = "."  
    output_rst_file = "session_summary.rst"
    generate_session_summary(output_rst_file, session_directory)
    print(f"Session summary generated at {output_rst_file}")


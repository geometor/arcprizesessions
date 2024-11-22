006 • History
=============

   :puzzle_id: 3-1e0a9b12
   :timestamp: 24.307.185016
   :call_count: 6




====


Begin puzzle: 3-1e0a9b12



**example_1**



**input**



.. code-block::

    [[0 4 0 9]
     [0 0 0 0]
     [0 4 6 0]
     [1 0 0 0]]


.. image:: _images/000-example_1_input.png
   :alt: _images/000-example_1_input.png



**output**



.. code-block::

    [[0 0 0 0]
     [0 0 0 0]
     [0 4 0 0]
     [1 4 6 9]]


.. image:: _images/000-example_1_output.png
   :alt: _images/000-example_1_output.png



**observations**



.. code-block:: yaml

   example_1:
     input:
       width: 4
       height: 4
       colors:
         - 0: 10
         - 1: 1
         - 4: 2
         - 6: 1
         - 9: 1
       objects:
         - yellow: size 2x1, position (1,1), (2,1)
         - blue: size 1x1, position (3,0)
         - magenta: size 1x1, position (2,2)
         - maroon: size 1x1, position (0,3)
     output:
       width: 4
       height: 4
       colors:
         - 0: 12
         - 1: 1
         - 4: 2
         - 6: 1
         - 9: 1
       objects:
         - blue: size 1x1, position (3,0)
         - yellow: size 1x1, position (2,1)
         - magenta: size 1x1, position (3,2)
         - maroon: size 1x1, position (3,3)
     differences:
       cells_changed: 9
       colors_changed: Some non-zero values move to the bottom-right corner of the grid while keeping their relative positions.  The rest of the grid becomes white.
     transformation:
       - Non-zero values are collected in the bottom-right corner, maintaining their relative positions to each other.

The transformation appears to involve moving all non-zero elements to the bottom-right corner while preserving their relative positions.  The remaining cells become white (0).



**example_2**



**input**



.. code-block::

    [[0 0 0 0 0 9]
     [0 0 0 8 0 0]
     [0 0 0 0 0 0]
     [4 0 0 0 0 0]
     [4 0 7 8 0 0]
     [4 0 7 0 0 0]]


.. image:: _images/001-example_2_input.png
   :alt: _images/001-example_2_input.png



**output**



.. code-block::

    [[0 0 0 0 0 0]
     [0 0 0 0 0 0]
     [0 0 0 0 0 0]
     [4 0 0 0 0 0]
     [4 0 7 8 0 0]
     [4 0 7 8 0 9]]


.. image:: _images/001-example_2_output.png
   :alt: _images/001-example_2_output.png



**observations**



.. code-block:: yaml

   example_2:
     input:
       width: 6
       height: 6
       colors:
         - 0: 29
         - 4: 3
         - 7: 2
         - 8: 2
         - 9: 1
       objects:
         - yellow: size 3x1, position (3,0), (4,0), (5,0)
         - orange: size 2x1, position (4,2), (5,2)
         - azure: size 2x1, position (4,3), (5,3)
         - maroon: size 1x1, position (0,5)
     output:
       width: 6
       height: 6
       colors:
         - 0: 33
         - 4: 3
         - 7: 2
         - 8: 2
         - 9: 1
       objects:
         - yellow: size 3x1, position (3,0), (4,0), (5,0)
         - orange: size 2x1, position (4,2), (5,2)
         - azure: size 2x1, position (4,3), (5,3)
         - maroon: size 1x1, position (5,5)
     differences:
       cells_changed: 3
       colors_changed: The maroon and azure objects moved to the bottom row, maintaining their relative positions.
     transformation:
       - Non-zero values in the bottom two rows are shifted to the bottom-right while maintaining relative positions.  The rest remain unchanged.

Both examples demonstrate a pattern of moving non-zero elements to the bottom-right corner of the grid while preserving their relative positions.  The key difference is that Example 1 moves *all* non-zero elements, while Example 2 only moves those in the bottom two rows.  This suggests a possible rule based on row position.  Further examples are needed to definitively determine the rule.



**example_3**



**input**



.. code-block::

    [[0 0 0 1 0]
     [0 3 0 0 0]
     [0 3 0 1 2]
     [6 0 0 0 0]
     [0 3 0 0 0]]


.. image:: _images/002-example_3_input.png
   :alt: _images/002-example_3_input.png



**output**



.. code-block::

    [[0 0 0 0 0]
     [0 0 0 0 0]
     [0 3 0 0 0]
     [0 3 0 1 0]
     [6 3 0 1 2]]


.. image:: _images/002-example_3_output.png
   :alt: _images/002-example_3_output.png



**observations**



.. code-block:: yaml

   example_3:
     input:
       width: 5
       height: 5
       colors:
         - 0: 18
         - 1: 2
         - 2: 1
         - 3: 3
         - 6: 1
       objects:
         - blue: size 2x1, position (3,3), (2,3)
         - red: size 1x1, position (2,4)
         - green: size 3x1, position (1,1), (2,1), (4,1)
         - magenta: size 1x1, position (3,0)

     output:
       width: 5
       height: 5
       colors:
         - 0: 21
         - 1: 2
         - 2: 1
         - 3: 3
         - 6: 1
       objects:
         - magenta: size 1x1, position (3,0)
         - green: size 2x1, position (2,1), (3,1)
         - blue: size 1x1, position (3,3)
         - red: size 1x1, position (4,4)

     differences:
       cells_changed: 11
       colors_changed: Non-zero values shift down and to the right while maintaining their relative positions.  The bottom row is filled.

     transformation:
       - Non-zero values shift down and to the right while maintaining relative positions.  The bottom row is filled. The top rows are filled with 0.

All three examples show a movement of non-zero values towards the bottom right, preserving relative positions.  Example 1 moves all non-zero values. Example 2 moves only those in the bottom two rows. Example 3 moves values downwards and to the right, filling the bottom row.  There's no consistent row-based rule; the rule seems to be more about filling the bottom row and then moving values down and to the right as space permits.  The top rows are always cleared to 0.



**examples summary**



The transformation rule appears to be a combination of two actions:


#. 
   **Clearing the upper rows:** The top rows of the output grid are always filled with zeros (white). The number of rows cleared varies depending on the input.  The number of rows cleared seems to be determined such that there is sufficient space in the remaining rows to accommodate all non-zero elements from the input while preserving their relative positions.

#. 
   **Compacting non-zero elements to the bottom-right:** The non-zero elements from the input grid are moved to the bottom-right corner of the output grid, maintaining their relative positions to one another.  This creates a compact block of non-zero values.

Let's analyze the number of cleared rows in each example:


* **Example 1:** 2 rows cleared (4x4 input, 2x4 output with non-zero elements).
* **Example 2:** 4 rows cleared (6x6 input, 2x6 output with non-zero elements).
* **Example 3:** 2 rows cleared (5x5 input, 3x5 output with non-zero elements).

There isn't a simple mathematical relationship directly observable between the input dimensions and the number of cleared rows. Further investigation with more examples might reveal a more precise pattern or rule. The key is maintaining relative positions of non-zero elements while ensuring they fit into the bottom-right section of the output grid.



**test**



**input**



.. code-block::

    [[0 2 0 4 3]
     [5 0 0 0 0]
     [0 0 6 0 0]
     [5 2 0 4 0]
     [5 0 0 0 0]]


.. image:: _images/004-test_input.png
   :alt: _images/004-test_input.png



**observations**



Based on the provided examples, the transformation involves two steps:


#. 
   **Clearing Upper Rows:**  The top rows are filled with zeros, leaving enough space at the bottom to accommodate all non-zero elements from the input while preserving their relative positions.

#. 
   **Compacting to Bottom-Right:**  Non-zero elements are moved to the bottom-right, maintaining their relative positions.

To determine how many rows to clear for the test input, let's count the non-zero elements:



code_execution:



.. code-block:: python


   test_input = [[0, 2, 0, 4, 3],
                 [5, 0, 0, 0, 0],
                 [0, 0, 6, 0, 0],
                 [5, 2, 0, 4, 0],
                 [5, 0, 0, 0, 0]]

   non_zero_count = sum(row.count(x) for row in test_input for x in row if x != 0)
   print(f'{non_zero_count=}')

   rows_needed = (non_zero_count + 4) // 5 #Integer division to get the number of rows needed to accommodate all non-zero elements, considering the width of 5.  Add 4 to account for the possibility of a non-zero element on the first row
   print(f'{rows_needed=}')

   rows_to_clear = 5 - rows_needed
   print(f'{rows_to_clear=}')



code_execution_result: 1



.. code-block::

   non_zero_count=9
   rows_needed=2
   rows_to_clear=3



The test input has 9 non-zero elements.  A 2x5 grid is needed to accommodate them at the bottom. Therefore, we need to clear 3 rows (5 - 2 = 3).

Here's the solution:



code_execution:



.. code-block:: python


   import numpy as np

   def initialize_output_by_size(width, height):
       return np.zeros((height, width), dtype=int)

   def set_pixel(grid, row, col, color):
       grid[row, col] = color

   def set_range(grid, row_start, row_end, col_start, col_end, color):
       grid[row_start:row_end, col_start:col_end] = color


   test_input = np.array([[0, 2, 0, 4, 3],
                 [5, 0, 0, 0, 0],
                 [0, 0, 6, 0, 0],
                 [5, 2, 0, 4, 0],
                 [5, 0, 0, 0, 0]])

   output = initialize_output_by_size(5,5)

   # Clear upper rows
   set_range(output, 0, 3, 0, 5, 0)

   # Map the non-zero elements to the bottom-right corner
   output[3, 0] = 5
   output[3, 1] = 2
   output[3, 3] = 4
   output[4, 0] = 5
   output[4, 1] = 0
   output[4, 2] = 6
   output[4, 3] = 0
   output[4, 4] = 0
   output[3, 4] = 3

   print(output)



code_execution_result: 1



.. code-block::

   [[0 0 0 0 0]
    [0 0 0 0 0]
    [0 0 0 0 0]
    [5 2 0 4 3]
    [5 0 6 0 0]]



The code has an error in mapping the non-zero elements.  The relative positions are not fully preserved. Let's correct it.



code_execution:



.. code-block:: python


   import numpy as np

   test_input = np.array([[0, 2, 0, 4, 3],
                 [5, 0, 0, 0, 0],
                 [0, 0, 6, 0, 0],
                 [5, 2, 0, 4, 0],
                 [5, 0, 0, 0, 0]])

   output = np.zeros((5, 5), dtype=int)
   output[3:,:] = 0 #Clear bottom rows


   non_zero_elements = []
   for r in range(test_input.shape[0]):
       for c in range(test_input.shape[1]):
           if test_input[r,c] != 0:
               non_zero_elements.append((r,c,test_input[r,c]))

   index = 0
   for r in range(3,5):
       for c in range(5):
           if index < len(non_zero_elements):
               output[r,c] = non_zero_elements[index][2]
               index += 1

   print(output)



code_execution_result: 1



.. code-block::

   [[0 0 0 0 0]
    [0 0 0 0 0]
    [0 0 0 0 0]
    [2 4 3 5 6]
    [5 2 4 5 0]]



The solution is still not correct. The relative positions are not preserved. I need to rethink the strategy.  The algorithm needs to track and maintain the relative positions of the elements more carefully.  The current approach assumes that all the elements are placed in order. This is not always the case.

Let's try a different approach:  We'll first identify the coordinates of the non-zero elements, then calculate their relative positions with respect to each other, and finally, place them in the bottom-right corner preserving those relative positions.



code_execution:



.. code-block:: python


   import numpy as np

   test_input = np.array([[0, 2, 0, 4, 3],
                          [5, 0, 0, 0, 0],
                          [0, 0, 6, 0, 0],
                          [5, 2, 0, 4, 0],
                          [5, 0, 0, 0, 0]])

   output = np.zeros((5, 5), dtype=int)

   non_zero_coords = []
   for r in range(test_input.shape[0]):
       for c in range(test_input.shape[1]):
           if test_input[r, c] != 0:
               non_zero_coords.append((r, c, test_input[r, c]))

   min_r = min(coord[0] for coord in non_zero_coords)
   min_c = min(coord[1] for coord in non_zero_coords)

   for r, c, val in non_zero_coords:
       new_r = 3 + (r - min_r)
       new_c = c - min_c
       if new_r < output.shape[0] and new_c < output.shape[1]:  # Check boundaries
          output[new_r, new_c] = val

   print(output)



code_execution_result: 1



.. code-block::

   [[0 0 0 0 0]
    [0 0 0 0 0]
    [0 0 0 0 0]
    [0 2 0 4 3]
    [5 0 0 0 0]]



The code is still incorrect. The relative positions are not entirely preserved.  The issue is in how we calculate ``new_r`` and ``new_c``. We're not handling the cases where the elements need to be placed beyond the boundaries correctly.  Also, we are not handling potential overlaps when elements would occupy the same position after shifting.

Let's try a different approach using a more robust method for preserving relative positions. We will build a mapping from old coordinates to new coordinates and then fill the output grid.



code_execution:



.. code-block:: python


   import numpy as np

   test_input = np.array([[0, 2, 0, 4, 3],
                          [5, 0, 0, 0, 0],
                          [0, 0, 6, 0, 0],
                          [5, 2, 0, 4, 0],
                          [5, 0, 0, 0, 0]])

   output = np.zeros((5, 5), dtype=int)

   non_zero_indices = np.nonzero(test_input)
   non_zero_values = test_input[non_zero_indices]

   num_non_zero = len(non_zero_values)
   rows_needed = (num_non_zero + 4) // 5
   rows_to_clear = 5 - rows_needed
   output[:rows_to_clear, :] = 0

   row_offsets = non_zero_indices[0] - np.min(non_zero_indices[0])
   col_offsets = non_zero_indices[1] - np.min(non_zero_indices[1])


   for i in range(num_non_zero):
       new_row = rows_to_clear + row_offsets[i]
       new_col = col_offsets[i]
       output[new_row, new_col] = non_zero_values[i]

   print(output)



code_execution_result: 1



.. code-block::

   Traceback (most recent call last):
     File "<string>", line 27, in <module>
   IndexError: index 5 is out of bounds for axis 0 with size 5



The error ``IndexError: index 5 is out of bounds for axis 0 with size 5`` arises because ``new_row`` can become larger than 4 due to how ``row_offsets`` is calculated and the addition of ``rows_to_clear``. The calculation of ``new_row`` and ``new_col`` needs to be adjusted to handle edge cases and ensure that ``new_row`` and ``new_col`` stay within the bounds of the output array.

Let's fix the code:



code_execution:



.. code-block:: python


   import numpy as np

   test_input = np.array([[0, 2, 0, 4, 3],
                          [5, 0, 0, 0, 0],
                          [0, 0, 6, 0, 0],
                          [5, 2, 0, 4, 0],
                          [5, 0, 0, 0, 0]])

   output = np.zeros((5, 5), dtype=int)

   non_zero_indices = np.nonzero(test_input)
   non_zero_values = test_input[non_zero_indices]

   num_non_zero = len(non_zero_values)
   rows_needed = (num_non_zero + 4) // 5  #Integer division to get the number of rows needed to accommodate all non-zero elements, considering the width of 5
   rows_to_clear = 5 - rows_needed
   output[:rows_to_clear, :] = 0

   min_row = np.min(non_zero_indices[0])
   min_col = np.min(non_zero_indices[1])

   for i in range(num_non_zero):
       new_row = rows_to_clear + non_zero_indices[0][i] - min_row
       new_col = non_zero_indices[1][i] - min_col

       # Check boundaries - this is crucial for handling edge cases
       if 0 <= new_row < output.shape[0] and 0 <= new_col < output.shape[1]:
           output[new_row, new_col] = non_zero_values[i]

   print(output)



code_execution_result: 1



.. code-block::

   [[0 0 0 0 0]
    [0 0 0 0 0]
    [0 0 0 0 0]
    [0 2 0 4 3]
    [5 0 0 0 0]]



The code is still not producing the correct output.  The relative positions are not being preserved correctly. There's a subtle but crucial flaw in how the relative positioning is handled.  The ``min_row`` and ``min_col`` calculation only considers the minimum row and column index of non-zero values; however, the algorithm assumes that the *relative* coordinates from the top-leftmost non-zero element are enough to position all values in the output. However, the top-leftmost might not be adjacent to all other non-zero values. This can be observed in the test input.

To fix this, we must find the correct offsets based on their relative positions within the non-zero element set.  This requires a more sophisticated approach to relative coordinate calculation and a more robust method to avoid boundary issues.  Let's rethink our strategy to handle these intricacies more accurately. We need to consider the dimensions of the bounding box of the non-zero elements, and use these for relative positioning in the output array.



code_execution:



.. code-block:: python


   import numpy as np

   def solve_puzzle(test_input):
       output = np.zeros_like(test_input)
       non_zero_indices = np.nonzero(test_input)
       non_zero_values = test_input[non_zero_indices]
       num_non_zero = len(non_zero_values)

       if num_non_zero == 0:
           return output

       min_row = np.min(non_zero_indices[0])
       min_col = np.min(non_zero_indices[1])
       max_row = np.max(non_zero_indices[0])
       max_col = np.max(non_zero_indices[1])

       height = max_row - min_row + 1
       width = max_col - min_col + 1

       rows_needed = (height + 4) // 5
       rows_to_clear = 5 - rows_needed
       output[:rows_to_clear, :] = 0

       for i in range(num_non_zero):
           row = non_zero_indices[0][i] - min_row
           col = non_zero_indices[1][i] - min_col
           new_row = rows_to_clear + row
           new_col = col

           if 0 <= new_row < output.shape[0] and 0 <= new_col < output.shape[1]:
               output[new_row, new_col] = non_zero_values[i]

       return output

   test_input = np.array([[0, 2, 0, 4, 3],
                          [5, 0, 0, 0, 0],
                          [0, 0, 6, 0, 0],
                          [5, 2, 0, 4, 0],
                          [5, 0, 0, 0, 0]])

   output = solve_puzzle(test_input)
   print(output)



code_execution_result: 1



.. code-block::

   [[0 0 0 0 0]
    [0 0 0 0 0]
    [0 0 0 0 0]
    [0 0 0 0 0]
    [0 2 0 4 3]]



The output is still incorrect. The algorithm still doesn't correctly preserve relative positions and handles edge cases poorly. The logic for calculating ``rows_needed`` is also flawed, as it should consider the total number of non-zero elements and the grid width to determine the minimum number of rows required for the compacted output, not just the height of the bounding box of the non-zero elements.

Let's implement a more robust solution that directly maps coordinates of the non-zero elements to their new positions in the output, ensuring the relative positions are preserved and handling the edge cases accurately.



code_execution:



.. code-block:: python


   import numpy as np

   def solve_puzzle(input_grid):
       non_zero_indices = np.nonzero(input_grid)
       non_zero_values = input_grid[non_zero_indices]
       num_non_zero = len(non_zero_values)

       if num_non_zero == 0:
           return np.zeros_like(input_grid)

       min_row = np.min(non_zero_indices[0])
       min_col = np.min(non_zero_indices[1])

       rows_needed = (num_non_zero + input_grid.shape[1] -1 ) // input_grid.shape[1]
       rows_to_clear = input_grid.shape[0] - rows_needed
       output_grid = np.zeros_like(input_grid)
       output_grid[:rows_to_clear, :] = 0

       for i in range(num_non_zero):
           row_index = non_zero_indices[0][i]
           col_index = non_zero_indices[1][i]
           new_row = rows_to_clear + row_index - min_row
           new_col = col_index - min_col

           if 0 <= new_row < output_grid.shape[0] and 0 <= new_col < output_grid.shape[1]:
               output_grid[new_row, new_col] = non_zero_values[i]

       return output_grid


   test_input = np.array([[0, 2, 0, 4, 3],
                          [5, 0, 0, 0, 0],
                          [0, 0, 6, 0, 0],
                          [5, 2, 0, 4, 0],
                          [5, 0, 0, 0, 0]])

   output = solve_puzzle(test_input)
   print(output)



code_execution_result: 1



.. code-block::

   [[0 0 0 0 0]
    [0 0 0 0 0]
    [0 0 0 0 0]
    [0 2 0 4 3]
    [5 0 0 0 0]]



The output is still incorrect.  The fundamental issue is that the algorithm doesn't correctly handle the relative positions when there are gaps between non-zero elements.  The previous attempts to calculate ``rows_needed`` were still inaccurate and did not ensure sufficient space for all non-zero elements. The previous method for placing elements into the output grid assumed that the relative positions would be straightforward, which isn't the case when there are gaps or non-adjacent non-zero elements.  The correct relative positions aren't being maintained.

Let's try a completely different approach.  We'll create a new array to store the non-zero values with their relative positions within the bounding box of the non-zero elements in the input.  Then, we'll transfer these elements to the output array, maintaining the relative positions.



code_execution:



.. code-block:: python


   import numpy as np

   def solve_puzzle(input_grid):
       non_zero_indices = np.nonzero(input_grid)
       non_zero_values = input_grid[non_zero_indices]
       num_non_zero = len(non_zero_values)

       if num_non_zero == 0:
           return np.zeros_like(input_grid)

       min_row = np.min(non_zero_indices[0])
       min_col = np.min(non_zero_indices[1])
       max_row = np.max(non_zero_indices[0])
       max_col = np.max(non_zero_indices[1])

       height = max_row - min_row + 1
       width = max_col - min_col + 1

       temp_grid = np.zeros((height, width), dtype=int)

       for i in range(num_non_zero):
           row = non_zero_indices[0][i] - min_row
           col = non_zero_indices[1][i] - min_col
           temp_grid[row, col] = non_zero_values[i]

       rows_needed = (num_non_zero + input_grid.shape[1] -1 ) // input_grid.shape[1]
       rows_to_clear = input_grid.shape[0] - rows_needed
       output_grid = np.zeros_like(input_grid)
       output_grid[:rows_to_clear, :] = 0

       for r in range(height):
           for c in range(width):
               if temp_grid[r,c] != 0:
                   output_row = rows_to_clear + r
                   output_col = c
                   if 0 <= output_row < output_grid.shape[0] and 0 <= output_col < output_grid.shape[1]:
                       output_grid[output_row, output_col] = temp_grid[r,c]


       return output_grid

   test_input = np.array([[0, 2, 0, 4, 3],
                          [5, 0, 0, 0, 0],
                          [0, 0, 6, 0, 0],
                          [5, 2, 0, 4, 0],
                          [5, 0, 0, 0, 0]])

   output = solve_puzzle(test_input)
   print(output)



code_execution_result: 1



.. code-block::

   [[0 0 0 0 0]
    [0 0 0 0 0]
    [0 0 0 0 0]
    [0 2 0 4 3]
    [5 0 0 0 0]]



The output is still incorrect. The problem lies in how we handle the placement of elements into the output array. The current method fails to accurately preserve relative positions in cases with irregular distributions of non-zero elements. The calculation of ``rows_needed`` and the placement logic need a more robust solution.

Let's implement a solution that accurately identifies the bounding box of non-zero elements, and then places these elements into the output array while strictly preserving their relative positions within this bounding box.



code_execution:



.. code-block:: python


   import numpy as np

   def solve_puzzle(input_grid):
       non_zero_indices = np.nonzero(input_grid)
       if not non_zero_indices[0].size:  #Handle empty input
           return np.zeros_like(input_grid)

       non_zero_values = input_grid[non_zero_indices]
       num_non_zero = len(non_zero_values)

       min_row = np.min(non_zero_indices[0])
       min_col = np.min(non_zero_indices[1])
       max_row = np.max(non_zero_indices[0])
       max_col = np.max(non_zero_indices[1])

       height = max_row - min_row + 1
       width = max_col - min_col + 1

       rows_needed = (num_non_zero + input_grid.shape[1] -1 ) // input_grid.shape[1]
       rows_to_clear = input_grid.shape[0] - rows_needed
       output_grid = np.zeros_like(input_grid)
       output_grid[:rows_to_clear,:] = 0


       for i in range(num_non_zero):
         row_offset = non_zero_indices[0][i] - min_row
         col_offset = non_zero_indices[1][i] - min_col
         output_row = rows_to_clear + row_offset
         output_col = col_offset
         output_grid[output_row, output_col] = non_zero_values[i]

       return output_grid

   test_input = np.array([[0, 2, 0, 4, 3],
                          [5, 0, 0, 0, 0],
                          [0, 0, 6, 0, 0],
                          [5, 2, 0, 4, 0],
                          [5, 0, 0, 0, 0]])

   output = solve_puzzle(test_input)
   print(output)



code_execution_result: 1



.. code-block::

   Traceback (most recent call last):
     File "<string>", line 41, in <module>
     File "<string>", line 31, in solve_puzzle
   IndexError: index 5 is out of bounds for axis 0 with size 5



**initialize the working output grid:**



================================================================================



INSTRUCTIONS:



use function_call to initialize the working output grid:




* initialize_output_from_input: good when examples show few differences between input and output




* initialize_output_by_size: create a fresh grid from size and color



.. seealso::

   - :doc:`006-prompt`
   - :doc:`006-response`


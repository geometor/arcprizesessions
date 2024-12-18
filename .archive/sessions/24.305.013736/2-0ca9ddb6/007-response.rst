007 • Response
==============


.. meta::
   :puzzle_id: 2-0ca9ddb6
   :timestamp: 24.305.013736
   :call_count: 7

code_execution:
```python
import numpy as np

def transform_grid(grid):
    """Applies the transformation: Yellow plus on Red, Orange plus on Blue."""

    height, width = grid.shape
    new_grid = grid.copy()

    for y in range(height):
        for x in range(width):
            if grid[y, x] == 1:  # Blue
                for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < height and 0 <= nx < width:
                         if new_grid[ny, nx] == 0: # Only overwrite if empty
                            new_grid[ny, nx] = 7  # Orange

            elif grid[y, x] == 2:  # Red
                for dy, dx in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                    ny, nx = y + dy, x + dx
                    if 0 <= ny < height and 0 <= nx < width:
                        if new_grid[ny, nx] == 0: # Only overwrite if empty
                            new_grid[ny, nx] = 4  # Yellow

    return new_grid

input_grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 1, 0, 0],
              [0, 0, 2, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 8, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0],
              [0, 6, 0, 0, 0, 0, 0, 2, 0],
              [0, 0, 0, 0, 0, 0, 0, 0, 0]]

output_grid = transform_grid(np.array(input_grid))
print(output_grid.tolist()) # Convert to Python list for submission

```


.. seealso::

   - :doc:`007-history`
   - :doc:`007-prompt`


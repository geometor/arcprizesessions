code_execution:

```python

import numpy as np

input_grid = np.array([[0, 0, 0, 0, 0, 0, 0],
                      [0, 8, 0, 0, 0, 0, 0],
                      [0, 8, 8, 0, 0, 0, 0],
                      [0, 0, 0, 0, 8, 8, 0],
                      [0, 0, 0, 0, 0, 8, 0],
                      [0, 0, 0, 0, 0, 0, 0],
                      [0, 0, 0, 0, 0, 0, 0]])

output_grid = np.array([[0, 0, 0, 0, 0, 0, 0],
                       [0, 8, 1, 0, 0, 0, 0],
                       [0, 8, 8, 0, 0, 0, 0],
                       [0, 0, 0, 0, 8, 8, 0],
                       [0, 0, 0, 0, 1, 8, 0],
                       [0, 0, 0, 0, 0, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0]])

difference_grid = output_grid - input_grid
print(f'{difference_grid=}')

```

code_execution_result: 1

```
difference_grid=array([[0, 0, 0, 0, 0, 0, 0],
       [0, 0, 1, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 1, 0, 0],
       [0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0]])

```

input:
  width: 7
  height: 7
  colors:
    - 0: 43
    - 8: 6
  objects:
    - size: 2x2, position: (1,1), color: azure
    - size: 2x2, position: (3,4), color: azure
output:
  width: 7
  height: 7
  colors:
    - 0: 41
    - 8: 6
    - 1: 2
  objects:
    - size: 2x2, position: (1,1), color: azure
    - size: 2x2, position: (3,4), color: azure
    - size: 1x1, position: (1,2), color: blue
    - size: 1x1, position: (4,4), color: blue
differences:
  cells_changed: 2
  colors_changed: added blue
transformation:
  - The transformation adds a single blue pixel to the top-right of each azure object.



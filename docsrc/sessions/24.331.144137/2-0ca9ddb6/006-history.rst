006 • History
=============

:puzzle_id: 2-0ca9ddb6
:description: init working
:timestamp: 24.331.144137
:call_count: 6






Begin puzzle: 2-0ca9ddb6






**example_1**

**input**

.. code-block::

   [[0 0 0 0 0 0 0 0 0]
    [0 0 0 0 0 0 0 0 0]
    [0 0 0 0 0 0 0 0 0]
    [0 0 2 0 0 0 0 0 0]
    [0 0 0 0 0 0 0 0 0]
    [0 0 0 0 0 0 0 0 0]
    [0 0 0 0 0 0 1 0 0]
    [0 0 0 0 0 0 0 0 0]
    [0 0 0 0 0 0 0 0 0]]

**output**

.. code-block::

   [[0 0 0 0 0 0 0 0 0]
    [0 0 0 0 0 0 0 0 0]
    [0 4 0 4 0 0 0 0 0]
    [0 0 2 0 0 0 0 0 0]
    [0 4 0 4 0 0 0 0 0]
    [0 0 0 0 0 0 7 0 0]
    [0 0 0 0 0 7 1 7 0]
    [0 0 0 0 0 0 7 0 0]
    [0 0 0 0 0 0 0 0 0]]

**images**





.. image:: _images/000-example_1_input.png
   :align: left
   :width: 45%




.. image:: _images/000-example_1_output.png
   :align: left
   :width: 45%





**observations**






The input grid is a 9x9 grid with two colored pixels: a red '2' and a blue '1'. The output grid is also 9x9, and contains the original red and blue pixels, but has added yellow '4' pixels surrounding the red pixel in a diamond pattern, and orange '7' pixels surrounding the blue pixel, also in a diamond pattern. The yellow pixels are a distance of 1 away from the red pixel and the orange pixels are distance of 1 away from the blue pixel.






code_execution:






.. code-block:: python


   import numpy as np

   input_grid = np.array([
   [0, 0, 0, 0, 0, 0, 0, 0, 0],
   [0, 0, 0, 0, 0, 0, 0, 0, 0],
   [0, 0, 0, 0, 0, 0, 0, 0, 0],
   [0, 0, 2, 0, 0, 0, 0, 0, 0],
   [0, 0, 0, 0, 0, 0, 0, 0, 0],
   [0, 0, 0, 0, 0, 0, 0, 0, 0],
   [0, 0, 0, 0, 0, 0, 1, 0, 0],
   [0, 0, 0, 0, 0, 0, 0, 0, 0],
   [0, 0, 0, 0, 0, 0, 0, 0, 0]
   ])

   output_grid = np.array([
   [0, 0, 0, 0, 0, 0, 0, 0, 0],
   [0, 0, 0, 0, 0, 0, 0, 0, 0],
   [0, 4, 0, 4, 0, 0, 0, 0, 0],
   [0, 0, 2, 0, 0, 0, 0, 0, 0],
   [0, 4, 0, 4, 0, 0, 0, 0, 0],
   [0, 0, 0, 0, 0, 0, 7, 0, 0],
   [0, 0, 0, 0, 0, 7, 1, 7, 0],
   [0, 0, 0, 0, 0, 0, 7, 0, 0],
   [0, 0, 0, 0, 0, 0, 0, 0, 0]
   ])

   print(f'{input_grid=}')
   print(f'{output_grid=}')

   red_coords = np.argwhere(input_grid == 2)
   blue_coords = np.argwhere(input_grid == 1)
   yellow_coords = np.argwhere(output_grid == 4)
   orange_coords = np.argwhere(output_grid == 7)

   print(f'{red_coords=}')
   print(f'{blue_coords=}')
   print(f'{yellow_coords=}')
   print(f'{orange_coords=}')


   def get_manhattan_distances(point, points_array):
     return np.abs(points_array - point).sum(axis=1)


   if len(red_coords) > 0:
       red_yellow_distances = get_manhattan_distances(red_coords[0], yellow_coords)
       print(f'{red_yellow_distances=}')
   if len(blue_coords) > 0:
       blue_orange_distances = get_manhattan_distances(blue_coords[0], orange_coords)
       print(f'{blue_orange_distances=}')

   unique_input_colors, input_color_counts = np.unique(input_grid, return_counts=True)
   unique_output_colors, output_color_counts = np.unique(output_grid, return_counts=True)

   print(f'{unique_input_colors=}')
   print(f'{input_color_counts=}')
   print(f'{unique_output_colors=}')
   print(f'{output_color_counts=}')






code_execution_result: 1






.. code-block::

   input_grid=array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 2, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 1, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0]])
   output_grid=array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 4, 0, 4, 0, 0, 0, 0, 0],
          [0, 0, 2, 0, 0, 0, 0, 0, 0],
          [0, 4, 0, 4, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 7, 0, 0],
          [0, 0, 0, 0, 0, 7, 1, 7, 0],
          [0, 0, 0, 0, 0, 0, 7, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0]])
   red_coords=array([[3, 2]])
   blue_coords=array([[6, 6]])
   yellow_coords=array([[2, 1],
          [2, 3],
          [4, 1],
          [4, 3]])
   orange_coords=array([[5, 6],
          [6, 5],
          [6, 7],
          [7, 6]])
   red_yellow_distances=array([2, 2, 2, 2])
   blue_orange_distances=array([1, 1, 1, 1])
   unique_input_colors=array([0, 1, 2])
   input_color_counts=array([79,  1,  1])
   unique_output_colors=array([0, 1, 2, 4, 7])
   output_color_counts=array([71,  1,  1,  4,  4])






.. code-block:: yaml

   input:
     width: 9
     height: 9
     colors:
       - 0: 79
       - 1: 1
       - 2: 1
     objects:
       - 1x1, (3,2), red - single red pixel
       - 1x1, (6,6), blue - single blue pixel
   output:
     width: 9
     height: 9
     colors:
       - 0: 71
       - 1: 1
       - 2: 1
       - 4: 4
       - 7: 4
     objects:
       - 1x1, (3,2), red - single red pixel
       - 1x1, (6,6), blue - single blue pixel
       - 1x1, (2,1), (2,3), (4,1), (4,3), yellow - four yellow pixels in a diamond around red
       - 1x1, (5,6), (6,5), (6,7), (7,6), orange - four orange pixels in a diamond around blue

   differences:
     cells_changed: 8
     colors_changed: 'added yellow (4) and orange (7)'
   transformation:
     - find the red (2) pixel in the input grid. Place four yellow (4) pixels in a diamond pattern such that the Manhattan distance from the red pixel is 2.
     - find the blue (1) pixel in the input grid. Place four orange (7) pixels in a diamond pattern such that the Manhattan distance from the blue pixel is 1.

The transformation involves identifying the red and blue pixels, and placing yellow pixels at a Manhattan distance of 2 from the red pixel in a diamond arrangement and placing orange pixels at a Manhattan distance of 1 from the blue pixel in a diamond arrangement.
The code confirmed the locations of the red and blue pixels, the locations of the new yellow and orange pixels and the fact that they are in a diamond arrangement around the original colors with the appropriate Manhattan distances.






**example_2**

**input**

.. code-block::

   [[0 0 0 8 0 0 0 0 0]
    [0 0 0 0 0 0 0 0 0]
    [0 0 0 0 0 0 2 0 0]
    [0 0 1 0 0 0 0 0 0]
    [0 0 0 0 0 0 0 0 0]
    [0 0 0 0 0 0 0 0 0]
    [0 0 0 0 0 0 1 0 0]
    [0 2 0 0 0 0 0 0 0]
    [0 0 0 0 0 0 0 0 0]]

**output**

.. code-block::

   [[0 0 0 8 0 0 0 0 0]
    [0 0 0 0 0 4 0 4 0]
    [0 0 7 0 0 0 2 0 0]
    [0 7 1 7 0 4 0 4 0]
    [0 0 7 0 0 0 0 0 0]
    [0 0 0 0 0 0 7 0 0]
    [4 0 4 0 0 7 1 7 0]
    [0 2 0 0 0 0 7 0 0]
    [4 0 4 0 0 0 0 0 0]]

**images**





.. image:: _images/001-example_2_input.png
   :align: left
   :width: 45%




.. image:: _images/001-example_2_output.png
   :align: left
   :width: 45%





**observations**






The input grid is a 9x9 grid with three colored pixels: two red '2', two blue '1', and one azure '8'. The output grid is also 9x9. The output grid contains the original colors, but adds yellow '4' pixels surrounding the red pixels at a Manhattan distance of 2 and in a diamond arrangement, and orange '7' pixels surrounding the blue pixels at a Manhattan distance of 1, also in a diamond arrangement. The azure '8' pixel is unchanged in the output.

code_execution:

.. code-block:: python


   import numpy as np

   input_grid = np.array([
   [0, 0, 0, 8, 0, 0, 0, 0, 0],
   [0, 0, 0, 0, 0, 0, 0, 0, 0],
   [0, 0, 0, 0, 0, 0, 2, 0, 0],
   [0, 0, 1, 0, 0, 0, 0, 0, 0],
   [0, 0, 0, 0, 0, 0, 0, 0, 0],
   [0, 0, 0, 0, 0, 0, 0, 0, 0],
   [0, 0, 0, 0, 0, 0, 1, 0, 0],
   [0, 2, 0, 0, 0, 0, 0, 0, 0],
   [0, 0, 0, 0, 0, 0, 0, 0, 0]
   ])

   output_grid = np.array([
   [0, 0, 0, 8, 0, 0, 0, 0, 0],
   [0, 0, 0, 0, 0, 4, 0, 4, 0],
   [0, 0, 7, 0, 0, 0, 2, 0, 0],
   [0, 7, 1, 7, 0, 4, 0, 4, 0],
   [0, 0, 7, 0, 0, 0, 0, 0, 0],
   [0, 0, 0, 0, 0, 0, 7, 0, 0],
   [4, 0, 4, 0, 0, 7, 1, 7, 0],
   [0, 2, 0, 0, 0, 0, 7, 0, 0],
   [4, 0, 4, 0, 0, 0, 0, 0, 0]
   ])

   print(f'{input_grid=}')
   print(f'{output_grid=}')

   red_coords = np.argwhere(input_grid == 2)
   blue_coords = np.argwhere(input_grid == 1)
   yellow_coords = np.argwhere(output_grid == 4)
   orange_coords = np.argwhere(output_grid == 7)

   print(f'{red_coords=}')
   print(f'{blue_coords=}')
   print(f'{yellow_coords=}')
   print(f'{orange_coords=}')

   def get_manhattan_distances(point, points_array):
     return np.abs(points_array - point).sum(axis=1)

   if len(red_coords) > 0:
       for red in red_coords:
           red_yellow_distances = get_manhattan_distances(red, yellow_coords)
           print(f'{red=}, {red_yellow_distances=}')
   if len(blue_coords) > 0:
       for blue in blue_coords:
           blue_orange_distances = get_manhattan_distances(blue, orange_coords)
           print(f'{blue=}, {blue_orange_distances=}')

   unique_input_colors, input_color_counts = np.unique(input_grid, return_counts=True)
   unique_output_colors, output_color_counts = np.unique(output_grid, return_counts=True)

   print(f'{unique_input_colors=}')
   print(f'{input_color_counts=}')
   print(f'{unique_output_colors=}')
   print(f'{output_color_counts=}')

code_execution_result: 2

.. code-block::

   input_grid=array([[0, 0, 0, 8, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 2, 0, 0],
          [0, 0, 1, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 1, 0, 0],
          [0, 2, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0]])
   output_grid=array([[0, 0, 0, 8, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 4, 0, 4, 0],
          [0, 0, 7, 0, 0, 0, 2, 0, 0],
          [0, 7, 1, 7, 0, 4, 0, 4, 0],
          [0, 0, 7, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 7, 0, 0],
          [4, 0, 4, 0, 0, 7, 1, 7, 0],
          [0, 2, 0, 0, 0, 0, 7, 0, 0],
          [4, 0, 4, 0, 0, 0, 0, 0, 0]])
   red_coords=array([[2, 6],
          [7, 1]])
   blue_coords=array([[3, 2],
          [6, 6]])
   yellow_coords=array([[1, 5],
          [1, 7],
          [3, 5],
          [3, 7],
          [6, 0],
          [6, 2],
          [8, 0],
          [8, 2]])
   orange_coords=array([[2, 2],
          [3, 1],
          [3, 3],
          [4, 2],
          [5, 6],
          [6, 5],
          [6, 7],
          [7, 6]])
   red=array([2, 6]), red_yellow_distances=array([2, 2, 2, 2])
   red=array([7, 1]), red_yellow_distances=array([2, 2, 2, 2])
   blue=array([3, 2]), blue_orange_distances=array([1, 1, 1, 1])
   blue=array([6, 6]), blue_orange_distances=array([1, 1, 1, 1])
   unique_input_colors=array([0, 1, 2, 8])
   input_color_counts=array([76,  2,  2,  1])
   unique_output_colors=array([0, 1, 2, 4, 7, 8])
   output_color_counts=array([63,  2,  2,  8,  8,  1])

```yaml
input:
  width: 9
  height: 9
  colors:

.. code-block::

   - 0: 76
   - 1: 2
   - 2: 2
   - 8: 1

  objects:

.. code-block::

   - 1x1, (2,6),(7,1), red - two red pixels
   - 1






**example_3**

**input**

.. code-block::

   [[0 0 0 0 0 0 0 0 0]
    [0 0 0 0 0 0 0 0 0]
    [0 0 2 0 0 0 0 0 0]
    [0 0 0 0 0 0 0 0 0]
    [0 0 0 0 0 0 0 0 0]
    [0 0 0 0 0 0 6 0 0]
    [0 0 0 0 0 0 0 0 0]
    [0 0 0 1 0 0 0 0 0]
    [0 0 0 0 0 0 0 0 0]]

**output**

.. code-block::

   [[0 0 0 0 0 0 0 0 0]
    [0 4 0 4 0 0 0 0 0]
    [0 0 2 0 0 0 0 0 0]
    [0 4 0 4 0 0 0 0 0]
    [0 0 0 0 0 0 0 0 0]
    [0 0 0 0 0 0 6 0 0]
    [0 0 0 7 0 0 0 0 0]
    [0 0 7 1 7 0 0 0 0]
    [0 0 0 7 0 0 0 0 0]]

**images**





.. image:: _images/002-example_3_input.png
   :align: left
   :width: 45%




.. image:: _images/002-example_3_output.png
   :align: left
   :width: 45%





**observations**






**observations**
The input grid is 9x9 and contains a red '2' pixel, a blue '1' pixel, and a magenta '6' pixel. The output grid is also 9x9 and contains the original pixels with the addition of yellow '4' pixels in a diamond around the red pixel and orange '7' pixels in a diamond around the blue pixel. The magenta '6' pixel is unchanged. The yellow pixels are a Manhattan distance of 2 from the red pixel and the orange pixels are a Manhattan distance of 1 from the blue pixel.

code_execution:

.. code-block:: python

   import numpy as np

   input_grid = np.array([
   [0, 0, 0, 0, 0, 0, 0, 0, 0],
   [0, 0, 0, 0, 0, 0, 0, 0, 0],
   [0, 0, 2, 0, 0, 0, 0, 0, 0],
   [0, 0, 0, 0, 0, 0, 0, 0, 0],
   [0, 0, 0, 0, 0, 0, 0, 0, 0],
   [0, 0, 0, 0, 0, 0, 6, 0, 0],
   [0, 0, 0, 0, 0, 0, 0, 0, 0],
   [0, 0, 0, 1, 0, 0, 0, 0, 0],
   [0, 0, 0, 0, 0, 0, 0, 0, 0]
   ])

   output_grid = np.array([
   [0, 0, 0, 0, 0, 0, 0, 0, 0],
   [0, 4, 0, 4, 0, 0, 0, 0, 0],
   [0, 0, 2, 0, 0, 0, 0, 0, 0],
   [0, 4, 0, 4, 0, 0, 0, 0, 0],
   [0, 0, 0, 0, 0, 0, 0, 0, 0],
   [0, 0, 0, 0, 0, 0, 6, 0, 0],
   [0, 0, 0, 7, 0, 0, 0, 0, 0],
   [0, 0, 7, 1, 7, 0, 0, 0, 0],
   [0, 0, 0, 7, 0, 0, 0, 0, 0]
   ])

   print(f'{input_grid=}')
   print(f'{output_grid=}')

   red_coords = np.argwhere(input_grid == 2)
   blue_coords = np.argwhere(input_grid == 1)
   yellow_coords = np.argwhere(output_grid == 4)
   orange_coords = np.argwhere(output_grid == 7)

   print(f'{red_coords=}')
   print(f'{blue_coords=}')
   print(f'{yellow_coords=}')
   print(f'{orange_coords=}')

   def get_manhattan_distances(point, points_array):
     return np.abs(points_array - point).sum(axis=1)

   if len(red_coords) > 0:
       for red in red_coords:
           red_yellow_distances = get_manhattan_distances(red, yellow_coords)
           print(f'{red=}, {red_yellow_distances=}')
   if len(blue_coords) > 0:
       for blue in blue_coords:
           blue_orange_distances = get_manhattan_distances(blue, orange_coords)
           print(f'{blue=}, {blue_orange_distances=}')

   unique_input_colors, input_color_counts = np.unique(input_grid, return_counts=True)
   unique_output_colors, output_color_counts = np.unique(output_grid, return_counts=True)

   print(f'{unique_input_colors=}')
   print(f'{input_color_counts=}')
   print(f'{unique_output_colors=}')
   print(f'{output_color_counts=}')

code_execution_result: 3

.. code-block::

   input_grid=array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 2, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 6, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 1, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0]])
   output_grid=array([[0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 4, 0, 4, 0, 0, 0, 0, 0],
          [0, 0, 2, 0, 0, 0, 0, 0, 0],
          [0, 4, 0, 4, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [0, 0, 0, 0, 0, 0, 6, 0, 0],
          [0, 0, 0, 7, 0, 0, 0, 0, 0],
          [0, 0, 7, 1, 7, 0, 0, 0, 0],
          [0, 0, 0, 7, 0, 0, 0, 0, 0]])
   red_coords=array([[2, 2]])
   blue_coords=array([[7, 3]])
   yellow_coords=array([[1, 1],
          [1, 3],
          [3, 1],
          [3, 3]])
   orange_coords=array([[6, 3],
          [7, 2],
          [7, 4],
          [8, 3]])
   red=array([2, 2]), red_yellow_distances=array([2, 2, 2, 2])
   blue=array([7, 3]), blue_orange_distances=array([1, 1, 1, 1])
   unique_input_colors=array([0, 1, 2, 6])
   input_color_counts=array([78,  1,  1,  1])
   unique_output_colors=array([0, 1, 2, 4, 6, 7])
   output_color_counts=array([71,  1,  1,  4,  1,  4])

.. code-block:: yaml

   input:
     width: 9
     height: 9
     colors:
       - 0: 78
       - 1: 1
       - 2: 1
       - 6: 1
     objects:
       - 1x1, (2,2), red
       - 1x1, (7,3), blue
       - 1x1, (5,6), magenta
   output:
     width: 9
     height: 9
     colors:
       - 0: 71
       - 1: 1
       - 2: 1
       - 4: 4
       - 6: 1
       - 7: 4
     objects:
       - 1x1, (2,2), red
       - 1x1, (7,3), blue
       - 1x1, (5,6), magenta
       - 1x1, (1,1), (1,3), (3,1), (3,3) yellow
       - 1x1, (6,3), (7,2), (7,4), (8,3) orange
   differences:
     cells_changed: 8
     colors_changed: added yellow (4) and orange (7)
   transformation:
     - For each red (2) pixel, place four yellow (4) pixels in a diamond pattern with a Manhattan distance of 2.
     - For each blue (1) pixel, place four orange (7) pixels in a diamond pattern with a Manhattan distance of 1.
     - All other pixels remain unchanged.

The code confirms the Manhattan distances and the diamond patterns of the added colors around the red and blue pixels. Other pixels, such as the magenta pixel, remain unchanged.






**examples summary**






The transformation consistently involves surrounding red (2) pixels with yellow (4) pixels in a diamond pattern at a Manhattan distance of 2, and surrounding blue (1) pixels with orange (7) pixels in a diamond pattern at a Manhattan distance of 1. All other pixels in the input grid are preserved in the output grid. The number and location of other colored pixels besides red and blue don't seem to impact the transformation.

code_execution:

.. code-block:: python

   import numpy as np

   def test_transformation(input_grid):
       output_grid = input_grid.copy()
       red_coords = np.argwhere(input_grid == 2)
       blue_coords = np.argwhere(input_grid == 1)

       for coord in red_coords:
           for i in [-2, 2]:
               for j in [-2,2]:
                   if abs(i) != abs(j):
                       y = coord[0] + i // 2
                       x = coord[1] + j // 2
                       if 0 <= y < input_grid.shape[0] and 0 <= x < input_grid.shape[1]:

                           output_grid[y,x] = 4



       for coord in blue_coords:
           for i in [-1, 0, 1]:
               for j in [-1, 0, 1]:
                   if abs(i) != abs(j):
                       y = coord[0] + i
                       x = coord[1] + j
                       if 0 <= y < input_grid.shape[0] and 0 <= x < input_grid.shape[1]:
                           output_grid[y, x] = 7

       return output_grid

   input_grid1 = np.array([
   [0, 0, 0, 0, 0, 0, 0, 0, 0],
   [0, 0, 0, 0, 0, 0, 0, 0, 0],
   [0, 0, 0, 0, 0, 0, 0, 0, 0],
   [0, 0, 2, 0, 0, 0, 0, 0, 0],
   [0, 0, 0, 0, 0, 0, 0, 0, 0],
   [0, 0, 0, 0, 0, 0, 0, 0, 0],
   [0, 0, 0, 0, 0, 0, 1, 0, 0],
   [0, 0, 0, 0, 0, 0, 0, 0, 0],
   [0, 0, 0, 0, 0, 0, 0, 0, 0]
   ])

   output_grid1 = test_transformation(input_grid1)
   print(output_grid1)



   input_grid2 = np.array([
   [0, 0, 0, 8, 0, 0, 0, 0, 0],
   [0, 0, 0, 0, 0, 0, 0, 0, 0],
   [0, 0, 0, 0, 0, 0, 2, 0, 0],
   [0, 0, 1, 0, 0, 0, 0, 0, 0],
   [0, 0, 0, 0, 0, 0, 0, 0, 0],
   [0, 0, 0, 0, 0, 0, 0, 0, 0],
   [0, 0, 0, 0, 0, 0, 1, 0, 0],
   [0, 2, 0, 0, 0, 0, 0, 0, 0],
   [0, 0, 0, 0, 0, 0, 0, 0, 0]
   ])
   output_grid2 = test_transformation(input_grid2)
   print(output_grid2)



   input_grid3 = np.array([
   [0, 0, 0, 0, 0, 0, 0, 0, 0],
   [0, 0, 0, 0, 0, 0, 0, 0, 0],
   [0, 0, 2, 0, 0, 0, 0, 0, 0],
   [0, 0, 0, 0, 0, 0, 0, 0, 0],
   [0, 0, 0, 0, 0, 0, 0, 0, 0],
   [0, 0, 0, 0, 0, 0, 6, 0, 0],
   [0, 0, 0, 0, 0, 0, 0, 0, 0],
   [0, 0, 0, 1, 0, 0, 0, 0, 0],
   [0, 0, 0, 0, 0, 0, 0, 0, 0]
   ])
   output_grid3 = test_transformation(input_grid3)
   print(output_grid3)






**test**

**input**

.. code-block::

   [[0 0 0 0 0 0 0 0 0]
    [0 0 0 0 0 0 0 0 0]
    [0 0 0 0 0 0 1 0 0]
    [0 0 2 0 0 0 0 0 0]
    [0 0 0 0 0 0 0 0 0]
    [0 0 0 0 0 8 0 0 0]
    [0 0 0 0 0 0 0 0 0]
    [0 6 0 0 0 0 0 2 0]
    [0 0 0 0 0 0 0 0 0]]

**image**





.. image:: _images/004-test_input.png
   :align: left
   :width: 45%










**observations**






code_execution_result: 4

.. code-block::

   [[0 0 0 0 0 0 0 0 0]
    [0 4 0 4 0 0 0 0 0]
    [0 0 2 0 0 0 1 0 0]
    [0 4 0 4 0 0 0 0 0]
    [0 0 0 0 0 0 0 0 0]
    [0 0 0 0 0 8 0 0 0]
    [0 0 0 0 0 0 0 0 0]
    [0 6 0 0 0 0 0 2 0]
    [0 0 0 0 0 0 0 0 0]]
   [[0 0 0 0 0 4 0 4 0]
    [0 0 0 0 0 0 0 0 0]
    [0 0 7 0 0 0 2 0 0]
    [0 7 1 7 0 4 0 4 0]
    [0 0 7 0 0 0 0 0 0]
    [0 0 0 0 0 0 7 0 0]
    [4 0 4 0 0 7 1 7 0]
    [0 2 0 0 0 0 7 0 0]
    [4 0 4 0 0 0 0 0 0]]
   [[0 0 0 0 0 0 0 0 0]
    [0 4 0 4 0 0 0 0 0]
    [0 0 2 0 0 0 0 0 0]
    [0 4 0 4 0 0 0 0 0]
    [0 0 0 0 0 0 0 0 0]
    [0 0 0 0 0 0 6 0 0]
    [0 0 0 7 0 0 0 0 0]
    [0 0 7 1 7 0 0 0 0]
    [0 0 0 7 0 0 0 0 0]]

**observations**
The input grid is 9x9 and contains two red '2' pixels, one blue '1' pixel, one magenta '6' pixel, and one azure '8' pixel.






code_execution:






.. code-block:: python


   import numpy as np

   input_grid = np.array([
   [0, 0, 0, 0, 0, 0, 0, 0, 0],
   [0, 0, 0, 0, 0, 0, 0, 0, 0],
   [0, 0, 0, 0, 0, 0, 1, 0, 0],
   [0, 0, 2, 0, 0, 0, 0, 0, 0],
   [0, 0, 0, 0, 0, 0, 0, 0, 0],
   [0, 0, 0, 0, 0, 8, 0, 0, 0],
   [0, 0, 0, 0, 0, 0, 0, 0, 0],
   [0, 6, 0, 0, 0, 0, 0, 2, 0],
   [0, 0, 0, 0, 0, 0, 0, 0, 0]
   ])

   unique_colors, counts = np.unique(input_grid, return_counts=True)
   print(f'{unique_colors=}')
   print(f'{counts=}')






code_execution_result: 1






.. code-block::

   unique_colors=array([0, 1, 2, 6, 8])
   counts=array([76,  1,  2,  1,  1])






.. code-block:: yaml

   input:
     width: 9
     height: 9
     colors:
       - 0: 76
       - 1: 1
       - 2: 2
       - 6: 1
       - 8: 1
     objects:
       - 1x1, (2,6), (7,7), red - two red pixels
       - 1x1, (3,2), blue - one blue pixel
       - 1x1, (7,0), magenta - one magenta pixel
       - 1x1, (5,5), azure - one azure pixel

code_execution:

.. code-block:: python

   import numpy as np

   def transform(grid):
       new_grid = grid.copy()
       reds = np.argwhere(grid == 2)
       blues = np.argwhere(grid == 1)

       for r in reds:
           for i in [-2, 2]:
               for j in [-2, 2]:
                   if abs(i) != abs(j):
                       y, x = r[0] + i // 2, r[1] + j // 2
                       if 0 <= y < grid.shape[0] and 0 <= x < grid.shape[1]:
                           new_grid[y, x] = 4

       for b in blues:
           for i in [-1, 0, 1]:
               for j in [-1, 0, 1]:
                   if abs(i) != abs(j) :
                       y, x = b[0] + i, b[1] + j
                       if 0 <= y < grid.shape[0] and 0 <= x < grid.shape[1]:
                           new_grid[y, x] = 7
       return new_grid

   input_grid = np.array([
   [0, 0, 0, 0, 0, 0, 0, 0, 0],
   [0, 0, 0, 0, 0, 0, 0, 0, 0],
   [0, 0, 0, 0, 0, 0, 1, 0, 0],
   [0, 0, 2, 0, 0, 0, 0, 0, 0],
   [0, 0, 0, 0, 0, 0, 0, 0, 0],
   [0, 0, 0, 0, 0, 8, 0, 0, 0],
   [0, 0, 0, 0, 0, 0, 0, 0, 0],
   [0, 6, 0, 0, 0, 0, 0, 2, 0],
   [0, 0, 0, 0, 0, 0, 0, 0, 0]
   ])

   output_grid = transform(input_grid)
   print(output_grid)






**initialize the working output grid:**






====






INSTRUCTIONS:






use function_call to initialize the working output grid:


* initialize_output_from_input: good when examples show few differences between
  input and output
* initialize_output_by_size: create a fresh grid from size and color








.. seealso::

   - :doc:`006-history`
   - :doc:`006-response`

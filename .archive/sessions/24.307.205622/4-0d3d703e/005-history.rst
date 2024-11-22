.. sidebar:: details

   :puzzle_id: 4-0d3d703e
   :timestamp: 24.307.205622
   :call_count: 5

005 • History
=============


Begin puzzle: 4-0d3d703e



**example_1**



**input**



.. code-block::

    [[3 1 2]
     [3 1 2]
     [3 1 2]]


.. image:: _images/000-example_1_input.png
   :alt: _images/000-example_1_input.png



**output**



.. code-block::

    [[4 5 6]
     [4 5 6]
     [4 5 6]]


.. image:: _images/000-example_1_output.png
   :alt: _images/000-example_1_output.png



**observations**



.. code-block:: yaml

   input:
     width: 3
     height: 3
     colors:
       - 1: 3
       - 2: 3
       - 3: 3
     objects:
       - color 3, 3x1 column on left
       - color 1, 3x1 column in center
       - color 2, 3x1 column on right
   output:
     width: 3
     height: 3
     colors:
       - 4: 3
       - 5: 3
       - 6: 3
     objects:
       - color 4, 3x1 column on left
       - color 5, 3x1 column in center
       - color 6, 3x1 column on right
   differences:
     cells_changed: 9
     colors_changed: input +1 for each
   transformation:
     - add 1 to each pixel value



**example_2**



**input**



.. code-block::

    [[2 3 8]
     [2 3 8]
     [2 3 8]]


.. image:: _images/001-example_2_input.png
   :alt: _images/001-example_2_input.png



**output**



.. code-block::

    [[6 4 9]
     [6 4 9]
     [6 4 9]]


.. image:: _images/001-example_2_output.png
   :alt: _images/001-example_2_output.png



**observations**



.. code-block:: yaml

   input:
     width: 3
     height: 3
     colors:
       - 2: 3
       - 3: 3
       - 8: 3
     objects:
       - color 2, 3x1 column on left
       - color 3, 3x1 column in center
       - color 8, 3x1 column on right
   output:
     width: 3
     height: 3
     colors:
       - 4: 3
       - 6: 3
       - 9: 3
     objects:
       - color 6, 3x1 column on left
       - color 4, 3x1 column in center
       - color 9, 3x1 column on right
   differences:
     cells_changed: 9
     colors_changed: see transformation notes
   transformation:
     - left column: add 4 (2 becomes 6)
     - center column: subtract -1 (3 becomes 4)
     - right column: add 1 (8 becomes 9)



**example_3**



**input**



.. code-block::

    [[5 8 6]
     [5 8 6]
     [5 8 6]]


.. image:: _images/002-example_3_input.png
   :alt: _images/002-example_3_input.png



**output**



.. code-block::

    [[1 9 2]
     [1 9 2]
     [1 9 2]]


.. image:: _images/002-example_3_output.png
   :alt: _images/002-example_3_output.png



**observations**



.. code-block:: yaml

   input:
     width: 3
     height: 3
     colors:
       - 5: 3
       - 6: 3
       - 8: 3
     objects:
       - color 5, 3x1 column on left
       - color 8, 3x1 column in center
       - color 6, 3x1 column on right
   output:
     width: 3
     height: 3
     colors:
       - 1: 3
       - 2: 3
       - 9: 3
     objects:
       - color 1, 3x1 column on left
       - color 9, 3x1 column in center
       - color 2, 3x1 column on right
   differences:
     cells_changed: 9
     colors_changed: see transformation notes
   transformation:
     - left column: subtract 4 (5 becomes 1)
     - center column: add 1 (8 becomes 9)
     - right column: subtract 4 (6 becomes 2)

It appears that a different arithmetic operation is being applied to each column.  It's not clear what determines the operation or the operand, however.



**example_4**



**input**



.. code-block::

    [[9 4 2]
     [9 4 2]
     [9 4 2]]


.. image:: _images/003-example_4_input.png
   :alt: _images/003-example_4_input.png



**output**



.. code-block::

    [[8 3 6]
     [8 3 6]
     [8 3 6]]


.. image:: _images/003-example_4_output.png
   :alt: _images/003-example_4_output.png



**observations**



.. code-block:: yaml

   input:
     width: 3
     height: 3
     colors:
       - 2: 3
       - 4: 3
       - 9: 3
     objects:
       - color 9, 3x1 column on left
       - color 4, 3x1 column in center
       - color 2, 3x1 column on right
   output:
     width: 3
     height: 3
     colors:
       - 3: 3
       - 6: 3
       - 8: 3
     objects:
       - color 8, 3x1 column on left
       - color 3, 3x1 column in center
       - color 6, 3x1 column on right
   differences:
     cells_changed: 9
     colors_changed: see transformation notes
   transformation:
     - left column: subtract 1 (9 becomes 8)
     - center column: subtract 1 (4 becomes 3)
     - right column: add 4 (2 becomes 6)

The pattern of a different arithmetic operation being applied to each column continues.  The operands are mostly 1 or 4 (ignoring signs) with no readily apparent pattern.



**examples summary**



================================================================================



INSTRUCTIONS:




* summarize your observations to explain the transformation of the input to output




* use code_execution to investigate properties, patterns and differences in the grids



.. seealso::

   - :doc:`005-prompt`
   - :doc:`005-response`



====


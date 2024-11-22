.. sidebar:: details

   :puzzle_id: 5-150deff5
   :timestamp: 24.307.205622
   :call_count: 4

004 • History
=============


Begin puzzle: 5-150deff5



**example_1**



**input**



.. code-block::

    [[0 0 0 0 0 0 0 0 0 0 0]
     [0 0 5 5 0 0 0 0 0 0 0]
     [0 0 5 5 5 5 5 0 0 0 0]
     [0 0 0 5 5 5 0 0 0 0 0]
     [0 0 0 5 5 5 5 5 0 0 0]
     [0 0 0 5 0 0 5 5 0 0 0]
     [0 0 0 0 0 5 5 5 0 0 0]
     [0 0 0 0 0 0 0 0 0 0 0]
     [0 0 0 0 0 0 0 0 0 0 0]]


.. image:: _images/000-example_1_input.png
   :alt: _images/000-example_1_input.png



**output**



.. code-block::

    [[0 0 0 0 0 0 0 0 0 0 0]
     [0 0 8 8 0 0 0 0 0 0 0]
     [0 0 8 8 2 2 2 0 0 0 0]
     [0 0 0 2 8 8 0 0 0 0 0]
     [0 0 0 2 8 8 8 8 0 0 0]
     [0 0 0 2 0 0 8 8 0 0 0]
     [0 0 0 0 0 2 2 2 0 0 0]
     [0 0 0 0 0 0 0 0 0 0 0]
     [0 0 0 0 0 0 0 0 0 0 0]]


.. image:: _images/000-example_1_output.png
   :alt: _images/000-example_1_output.png



**observations**



.. code-block:: yaml

   input:
     width: 11
     height: 9
     colors:
       - 0: 68
       - 5: 13
   objects:
     - a gray (5) object shaped like a "7" rotated 90 degrees clockwise

   output:
     width: 11
     height: 9
     colors:
       - 0: 68
       - 2: 6
       - 8: 7
   objects:
     - an azure (8) object shaped like a "7" rotated 90 degrees clockwise
     - a smaller red (2) object where the concave portion of the larger object is located.
   differences:
     cells_changed: 13
     colors_changed: gray (5) pixels became either red (2) or azure (8)
   transformation:
     - The gray object in the input has been split into two objects in the output. The outer portion of the object has been changed to azure, while a smaller red object fills the concave section of the original object.



**example_2**



**input**



.. code-block::

    [[0 0 0 0 0 0 0 0 0 0]
     [0 5 5 5 5 5 5 0 0 0]
     [0 5 5 5 5 5 5 0 0 0]
     [0 0 0 5 0 0 5 0 0 0]
     [0 0 0 0 5 5 5 0 0 0]
     [0 0 0 0 5 5 5 0 0 0]
     [0 0 0 0 5 0 0 0 0 0]
     [0 0 0 0 0 0 0 0 0 0]]


.. image:: _images/001-example_2_input.png
   :alt: _images/001-example_2_input.png



**output**



.. code-block::

    [[0 0 0 0 0 0 0 0 0 0]
     [0 8 8 2 8 8 2 0 0 0]
     [0 8 8 2 8 8 2 0 0 0]
     [0 0 0 2 0 0 2 0 0 0]
     [0 0 0 0 2 8 8 0 0 0]
     [0 0 0 0 2 8 8 0 0 0]
     [0 0 0 0 2 0 0 0 0 0]
     [0 0 0 0 0 0 0 0 0 0]]


.. image:: _images/001-example_2_output.png
   :alt: _images/001-example_2_output.png



**observations**



.. code-block:: yaml

   input:
     width: 10
     height: 8
     colors:
       - 0: 48
       - 5: 20
   objects:
     - a gray (5) object shaped like a "V" with a bar connecting the arms.

   output:
     width: 10
     height: 8
     colors:
       - 0: 48
       - 2: 8
       - 8: 12
   objects:
     - an azure (8) object shaped like a "V".
     - a red (2) object in the shape of an "I", filling the negative space from the input object.

   differences:
     cells_changed: 20
     colors_changed: gray (5) pixels became either red (2) or azure (8).
   transformation:
     - Similar to the first example, the gray (5) object has been split and re-colored.  The outer portions of the object have become azure (8) and the inner portion became red (2).



**example_3**



**input**



.. code-block::

    [[0 0 0 0 0 0 0 0 0]
     [0 5 5 5 5 5 0 0 0]
     [0 0 0 0 5 5 0 0 0]
     [0 0 0 5 0 0 0 0 0]
     [0 0 0 5 5 5 0 0 0]
     [0 0 0 5 5 5 0 0 0]
     [0 0 0 0 0 0 0 0 0]
     [0 0 0 0 0 0 0 0 0]]


.. image:: _images/002-example_3_input.png
   :alt: _images/002-example_3_input.png



**output**



.. code-block::

    [[0 0 0 0 0 0 0 0 0]
     [0 2 2 2 8 8 0 0 0]
     [0 0 0 0 8 8 0 0 0]
     [0 0 0 2 0 0 0 0 0]
     [0 0 0 2 8 8 0 0 0]
     [0 0 0 2 8 8 0 0 0]
     [0 0 0 0 0 0 0 0 0]
     [0 0 0 0 0 0 0 0 0]]


.. image:: _images/002-example_3_output.png
   :alt: _images/002-example_3_output.png



**observations**



.. code-block:: yaml

   input:
     width: 9
     height: 8
     colors:
       - 0: 52
       - 5: 12
   objects:
     - a gray (5) object shaped like a "7".

   output:
     width: 9
     height: 8
     colors:
       - 0: 52
       - 2: 5
       - 8: 7
   objects:
     - an azure (8) object shaped like a "7" but missing the initial horizontal bar.
     - a red (2) object that represents the missing part of the "7".

   differences:
     cells_changed: 12
     colors_changed: gray (5) pixels became either red (2) or azure (8).
   transformation:
     - The transformation is consistent with the previous two examples.  The original gray (5) object has been split and re-colored into azure (8) and red (2) objects.  The azure object resembles the original object with a part missing and the red object represents the missing part.



**examples summary**



================================================================================



INSTRUCTIONS:




* summarize your observations to explain the transformation of the input to output




* use code_execution to investigate properties, patterns and differences in the grids



.. seealso::

   - :doc:`004-prompt`
   - :doc:`004-response`



====


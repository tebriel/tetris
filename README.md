#### Thumbtack's 3rd Annual PyCon Programming Challenge ####

#### Valid Solutions win a Beer Mug! ####

## Tetris ##

### A block is falling straight down on a Tetris board. ###

### When that piece reaches the bottom, how many lines will be cleared. ###

[sample inputs](http://tinyurl.com/pycon-tetris)

Write a python program to solve this challenge. Read the board from stdin , and
write to stdout the number of cleared lines. Sample inputs and expected
outputs: [http://tinyurl.com/pycon-tetris](http://tinyurl.com/pycon-tetris)

*  There is only ever one piece dropped.
*  The ground can be assumed to be in a stable state.
*  There is at least one blank row between teh piece and the ground.
*  Simple gravity: when a piece lands on the bottom and clears a line, any
   blocks above the cleared line move down by the number of rows cleared adn no
   more. This may leave floating pieces, like in the original Tetris.


Pair programming and solutions are encouraged. Feel free to work solo or with a
partner. Send your solution to pycon@thumbtack.com. Include the name and email
of your partner, if any, and you'll both win beer mugs for a successful
soltuion.

### Advanced Challenge: Sticky Gravity ###

For a more difficult challenge, implement the above, but use "sticky" gravity
instead of simple gravity. In this scenario, any cells that are adjacent
horizontally or vertically are marked as being part of the same segmetn.
Segements fall independently until they collide, then line clears are
performed. After line clears, any newly suspended segments fall independently
and further line clears occur, and so on. Details, images, and test cases:
[http://tinyurl.com/pycon-tetris-sticky](http://tinyurl.com/pycon-tetris-sticky)

"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Raymond Becerra.
"""
###############################################################################
# DONE: 1.
#   On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
###############################################################################

###############################################################################
# DONE: 2.
#   You should have RUN the  m4e_loopy_turtles  module and READ its code.
#   (Do so now if you have not already done so.)
#
#   Below this comment, add ANY CODE THAT YOU WANT, as long as:
#     1. You construct at least 2 rg.SimpleTurtle objects.
#     2. Each rg.SimpleTurtle object draws something
#          (by moving, using its rg.Pen).  ANYTHING is fine!
#     3. Each rg.SimpleTurtle moves inside a LOOP.
#
#   Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#   If you make syntax (notational) errors, no worries -- get help
#   fixing them at either this session OR at the NEXT session.
#
#   Don't forget to COMMIT-and-PUSH when you are done with this module.
###############################################################################

import rosegraphics as rg

window = rg.TurtleWindow()

red_turtle = rg.SimpleTurtle('turtle')
red_turtle.pen = rg.Pen('red',3)
red_turtle.speed = 15

blue_turtle = rg.SimpleTurtle('turtle')
blue_turtle.pen = rg.Pen('blue',3)
blue_turtle.speed = 15

size = 300

blue_turtle.pen_up()
blue_turtle.backward(100)
blue_turtle.pen_down()

for k in range(13):

    red_turtle.draw_square(size)
    red_turtle.pen_up()
    red_turtle.right(55)
    red_turtle.forward(15)
    red_turtle.left(55)
    red_turtle.pen_down()

    blue_turtle.draw_square(size)
    blue_turtle.pen_up()
    blue_turtle.right(55)
    blue_turtle.forward(15)
    blue_turtle.left(55)
    blue_turtle.pen_down()

    size = size - 10

window.close_on_mouse_click()
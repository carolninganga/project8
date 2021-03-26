#Caroline Ninganga
#CS 5001 
#Project 8 


#import the turtle package, the random and sys packages
import turtle as t
import sys
import random

#define a TurtleInterpreter
class TurtleInterpreter:
    #define the init
    def __init__(self, dx = 800, dy = 800):
        # call turtle.setup with dx and dy as the arguments
        t.setup( dx, dy )
        # set the turtle tracer to false (optional)
        t.tracer( False )

def drawString(self, string, distance, angle ):
    """ Interpret the characters in string as a series of turtle commands. Distance specifies the distance
    to travel for each forward command. Angle specifies the angle (in degrees) for each right 
    or left command. The list of turtle supported turtle commands is:
    F : forward
    - : turn right
    + : turn left
    [ : save the turtle's heading and position
    ] : restore the turtle's heading and position 
    """

    # assign to stack the empty list
    stack = []
    # for each character d in string 
    for c in string :
        # if d is equal to 'F'
        if c == 'F' :
            # tell the turtle go forward by distance
            t.forward( distance )
        # else if c is equal to '-'
        elif c == '-':
            t.right( angle )
        # else if d is equal to '+'
        elif c == '+':
            t.left( angle )
        # else if d is equal '['
        elif c == '[':
            # append to stack the position of the turtle (position method)
            stack.append(t.position())
            # append to stack the heading of the turtle (heading method)
            stack.append(t.heading())
        # else if c is  equal to ']'
        elif c == ']':
            # tell the turtle to pick up pen 
            t.up()
            # call the setheading method of the turtle and pass it the value popped off stack
            t.setheading( stack.pop())
            # call the goto method of the turtle and pass it the value popped of stack
            t.goto(stack.pop())
            # tell the turtlr to put down pen
            t.down()
    # call the turtle.update() (not in the for loop)
    t.update()

def hold(self):
    '''Holds the screen open until user clicks or presses 'q' key'''

    # Hide the turtle cursor and update the screen
    t.hideturtle()
    t.update()

    # Close the window when users presses the 'q' key
    t.onkey(t.bye, 'q')

    # Listen for the q button press event
    t.listen()

    # Have the turtle listen for a click
    t.exitonclick()


#def place(self, xpos, ypos, angle=None): - the method should pick up the pen, place the turtle at location (xpos, ypos), 
# orient the turtle if the angle argument is not None, and then put down the pen.
def place(self, xpos, ypos, angle=None):
    t.up( xpos, ypos )
    if angle != None:
    # tell the turtlr to put down pen
    t.down()

#def orient(self, angle): - the method should use the turtle's setheading function to set turtle's heading to the given angle.
def orient( self, angle ):
    t.setheading(angle)

#def goto(self, xpos, ypos): - the method should pick up the turtle, send the turtle to (xpos, ypos), and then put the pen down.
def goto( self, xpos, ypos ):
    t.up( xpos, ypos )
    t.down()

#def setColor(self, c): - the method should call turtle.color() with the argument c to set the turtle's color.
def setColor( self, c ):
    t.color( c )

#def setWidth(self, w): - the method should call turtle.width() with the argument w to set the turtle's width.
def setWidth( self, w ):
    t.width( w )

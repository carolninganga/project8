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


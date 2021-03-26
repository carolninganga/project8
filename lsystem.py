#Caroline Ninganga
#CS 5001 
#Project 8 Classes 

class Lsystem: 

    # wirte a constructor 
    def __init__( self, filename=None):
         # assign to the field base, the empty string
         self.base = " "
         # assign to the field rules, the empty list
         self.rules = []
         # if the filename variable is not equal to None
         if filename != None:
            # call the read method of self with filename as the argument
            self.read( filename )


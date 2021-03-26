#Caroline Ninganga
#CS 5001 
#Project 8 Classes 

import sys

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

    # get the base value of the base field of the object
    def getBase(self):
        return self.base

    #get rule should return the specified rule of self
    def getRule(self, index):
        return self.rules
    #the setBase function should assign to the base field (self.base) the value in b.
    def setBase(self, b):
        self.base = b
    #the addRule function should append newrule to the rules field of self
    def addRule(self, newrule):
        self.rules.append( newrule )

    # numsRules retruns the number of rules in the rules list 
    def numRules(self):
        return len(self.rules)

    # write a read method
    def read( self, filename ):
        # assign to the rules field of self the empty list
        self.rules = []
        # assign to a variable (e.g. fp) the file object created with filename in read mode
        fp = (filename)
        # for each line in fp 
        for linn in fp:
            # assign to line the result of calling line.strip()
            line = line.strip()
            # assign to a variable (e.g. words) the result of calling the split() method line
            words = split()
            # if the first item in words is equal to the string 'base'
            if words[0] == 'base':
                # call the setBase method of self with the new base string
                setBase('base')
            # else if the first item in words is equal to the string 'rule'
            elif words[0] == 'rule':
                # call the addRule method of self with the new rule (the slice of words from index 1
                addRule(words[1:])

    # call the close method of the file
    fp.close()


def replace(self, istring):
# assign to a local variable (e.g. tstring) the empty string
tstring = ""
    
    # for each character c in the input string (istring)
    for c in istring:
        # set a local variable (e.g. found) to False
        found = False
            # for each rule in the rules field of self
            for rule in self.rules:
                # if the symbol in the rule is equal to the character in c
                if symbol == c
                    # add to tstring the replacement from the rule
                    # set found to True
                    # break
                # if not found
                    # add to tstring the character c
                    # return tstring, make sure this statement is not inside the for loop


def buildString(self, iterations):
    # assign to a local variable (e.g. nstring) the base field of self
    nstring = self.base
    # for the number of iterations
    for i in range(iterations)
        # assign to nstring the result of calling the replace method of self with nstring as the argument
        nstring = replace( self, nstring):
    # return nstring
    return nstring

def main(argv):

    # check the number of arguments entered by the user 
    if len(argv) < 2:
      print('Usage: lsystem.py <filename>')
      exit()

    filename = argv[1]
    iterations = 2

    lsys = Lsystem()

    lsys.read( filename )

    print( lsys )
    print( lsys.getBase() )
    for i in range( lsys.numRules() ):
      rule = lsys.getRule(i)
      print( rule[0] + ' -> ' + rule[1] )

    lstr = lsys.buildString( iterations )
    print( lstr )

    return

if __name__ == "__main__":
    main(sys.argv)

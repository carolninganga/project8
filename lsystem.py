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

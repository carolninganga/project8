#Caroline Ninganga
#CS 5001 
#Project 8 
#Growth file

#import lsystem and turtle_interpreter
import lsystem 
import turtle_interpreter as ti 

# define a scene function 
def scene():
 
    '''draw window for lsystem trees'''
    width = 1000
    height = 1000
    # create the turte interpreter object that will intepret lstring & draw it
    terp = ti.TurtleInterpreter(width, height) #x,y size of turtle window

    ''' create first variation'''
    ls = lsystem.Lsystem( 'systemHL.txt')
    # print(ls, ls.rules)

    #x and y vals of where this lsystem will be on window
    tstr = ls.buildString(3) #build the string using the buildstring from turtleInterpreter 3 interations
    terp.place(-400, -150, 90) 
    dist = float( 10 )
    angle = float( 22.5 )
    terp.setWidth(2) #set the width to 2 
    terp.setColor("brown") #changed the color 
    terp.drawString( tstr, dist, angle )

    ''' create second variation '''
    ls = lsystem.Lsystem( 'systemHL.txt') #used self constructed Lsystem systemHL.txt
    print(ls, ls.rules)
    
    #x and y vals of where this lsystem will be on window
    tstr = ls.buildString(4)# used 4 iterations for the second pic
    terp.place(-150, -350, 90) # changed the location
    dist = float(10)
    angle = float( 22.5 )
    terp.setColor("brown")

    terp.drawString( tstr, dist, angle ) #use the turtleInterpreter buildString method 

    ''' create third variation '''
    ls = lsystem.Lsystem( 'systemHL.txt')
    # print(ls, ls.rules)

    #x and y vals of where this lsystem will be on window
    tstr = ls.buildString(5)
    terp.place(150, -180, 90) #changed the loctaion 
    dist = float(10)
    angle = float( 22.5 )
    terp.setColor("brown")
    terp.drawString( tstr, dist, angle ) #use the turtleInterpreter buildString method

    # hold
    terp.hold()

if __name__ == '__main__':
    scene()
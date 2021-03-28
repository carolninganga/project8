#Caroline Ninganga
#CS 5001 
#Project 8 

#import lsystem and turtle_interpreter
import lsystem 
import turtle_interpreter as ti 


def main():
 
    '''draw window for lsystem trees'''
    width = 1000
    height = 1000
    # create the turte interpreter object that will intepret lstring & draw it
    terp = ti.TurtleInterpreter(width, height) #x,y size of turtle window

    ''' create first lsystem'''
    ls = lsystem.Lsystem( 'systemFL.txt')
    # print(ls, ls.rules)

    #x and y vals of where this lsystem will be on window
    tstr = ls.buildString(4)
    terp.place(-300, -280, 90)
    dist = float( 10 )
    angle = float( 30 )
    terp.setWidth(2)
    terp.setColor("green")
    terp.drawString( tstr, dist, angle )

    ''' create second lsystem '''
    ls = lsystem.Lsystem( 'systemGL.txt')
    # print(ls, ls.rules)
    
    #x and y vals of where this lsystem will be on window
    tstr = ls.buildString(8)
    terp.place(0, -320, 90)
    dist = float(10)
    angle = float( 28 )
    terp.setColor("green")

    terp.drawString( tstr, dist, angle )

    ''' create second lsystem '''
    ls = lsystem.Lsystem( 'systemFL.txt')
    # print(ls, ls.rules)

    #x and y vals of where this lsystem will be on window
    tstr = ls.buildString(4)
    terp.place(300, -280, 90)
    dist = float(10)
    angle = float( 30 )
    terp.setColor("green")
    terp.drawString( tstr, dist, angle )


    terp.hold()

    # print( 'C1', 'systemC.txt')
    # print( ls.getBase())

if __name__ == '__main__':
    main()
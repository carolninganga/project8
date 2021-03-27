#Caroline Ninganga
#CS 5001 
#Project 8 

#import lsystem and turtle_interpreter
import lsystem 
import turtle_interpreter as ti 


def main():
 
    '''draw window for lsystem trees'''
    width = 700
    height = 700
    # create the turte interpreter object that will intepret lstring & draw it
    terp = ti.TurtleInterpreter(width, height) #x,y size of turtle window

    ''' create first lsystem'''
    ls = lsystem.Lsystem( 'systemFL.txt')
    # print(ls, ls.rules)

    #x and y vals of where this lsystem will be on window
    tstr = ls.buildString(5)
    terp.place(-150, -280, 90)
    dist = float( 10 )
    angle = float( 30 )
    terp.setWidth(3)
    terp.drawString( tstr, dist, angle )

    ''' create second lsystem '''
    ls = lsystem.Lsystem( 'systemEL.txt')
    # print(ls, ls.rules)
    
    #x and y vals of where this lsystem will be on window
    tstr = ls.buildString(4)
    terp.place(100, -280, 90)
    dist = float(10)
    angle = float( 8 )
    terp.setColor("blue")
    terp.drawString( tstr, dist, angle )


    terp.hold()

    # print( 'C1', 'systemC.txt')
    # print( ls.getBase())

if __name__ == '__main__':
    main()
# May Pena
# This prrogram creates a 600 by 600 blanket by drawing
# different colored squares fillin the screen. 

from graphics import *
from random import *

def main():
    # creates window
    win    = GraphWin( "May's HW6_5", 600, 600 ) 

    # draws grid of colored squares
    for i in range( 0, 24 ):
        for j in range( 0, 24 ):
            red   = randint( 0, 255 )
            green = randint( 0, 255 )
            blue  = randint( 0, 255 )
            color = color_rgb( red, green, blue)

            point1 = Point( i * 25, j * 25 )
            point2 = Point( i * 25 + 25, j * 25 + 25  )
    
            r     = Rectangle( point1, point2)
            r.setFill( color )
            r.draw(win)

    # draws name tag
    r2 = Rectangle( Point( 100, 250 ), Point( 500, 350 ) ) 
    r2.setFill( "white" )
    r2.draw(win)

    name = Text( Point( 300, 300 ), "Mayeline Pena" )
    name.draw( win )

    # close window when user clicks on it
    win.getMouse()
    win.close()

main()

"""
Have the turtle draw a row of houses.
"""
import turtle
from    tkinter import messagebox, simpledialog, Tk

window = Tk()
window.withdraw()

if __name__ == '__main__':
    # TODO)

    #   1) Move the turtle to the left side of the window near the bottom.

    my_turtle = turtle.Turtle()
    my_turtle.penup()
    my_turtle.goto(-390,150)
    my_turtle.pendown()
    #   2) Draw ONE flat-topped house with height=100 and green grass after it.]
    def draw_house  ():
        for i in range (11):
            my_turtle.forward(20)
            my_turtle.left(90)
            my_turtle.forward(50)
            my_turtle.right (90)
            my_turtle.forward(50)
            my_turtle.right(90)
            my_turtle.forward(50)
            my_turtle. left(90)
    def pointy_house ():
        for i in range (10):
            my_turtle.forward(20)
            my_turtle.left(90)
            my_turtle.forward(50)
            my_turtle.left(120)
            my_turtle.right(120)
            my_turtle.right(60)
            my_turtle.forward(30)
            my_turtle.right(60)
            my_turtle.forward(30)
            my_turtle.right(110)
            my_turtle.right(-50)
            my_turtle.forward(50)
            my_turtle.left(90)
            my_turtle.forward(20)



    #xddraw_house()
    pointy_house()
    #   3) Put the code that drew the house into a function called draw_house
    #      HINT: Only the code that draws one house should go in this function.
    #   4) Using the function you just created, draw 10 houses.
    #      HINT: Use a for loop.
    #   5) Run the code to make sure it works before proceeding.
    #   6) Now change the draw_house function to take height as a parameter.
    #   7) Use random numbers to draw 9 houses of different heights.
    #   8) Run the code to make sure it works before proceeding.
    #   9) Make the draw_house function's height input a string and set the
    #      height of the house based on the following:
    #         “small”            =  60
    #         “medium”           =  120
    #         “large”            =  250
    #   10) Make two new functions that draw different shaped roofs
    #      (JUST the roof part): draw_pointy_roof, draw_flat_roof
    #   11) By calling the correct "roof" function, make large houses have
    #      flat roofs and all the others have pointy roofs.

    turtle.done()
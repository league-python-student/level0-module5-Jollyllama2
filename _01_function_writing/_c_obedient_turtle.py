"""
Make an obedient turtle that will obey commands to draw shapes.
"""
from tkinter import messagebox, simpledialog, Tk
import turtle

def Fuiyo():

    turtle.goto(x = 20, y = 50)
    turtle.pendown()
    turtle.forward(100)
    turtle.left(-90)
    turtle.forward(100)
    turtle.left(-90)
    turtle.forward(100)
    turtle.left(-90)
    turtle.forward(100)
    turtle.left(-90)




def tri():
    my_turtle.pendown()
    for i in range (3):
        my_turtle.forward(100)
        my_turtle.right(120)







def circ():
    rad = 100
    my_turtle.circle(rad)



if __name__ == '__main__':
    # TODO)
    #   1. Create a turtle.
    my_turtle = turtle.Turtle()

    #   2. Write 3 method definitions for drawing a square, triangle, and
    #      circle.

    #   3. Ask the user for the for a shape to draw.
    de_donde_es = simpledialog.askstring(title='hola ',prompt='what shape do u want to draw (a square, circle or a triangle r ur options, aswell no caps)')

    #   4. Draw the appropriate shape depending on their answer (call the right
    #      function)
    if de_donde_es == 'square':
        Fuiyo()
    if de_donde_es == 'triangle':
        tri()
    if de_donde_es == 'circle':
        circ()

    turtle.done()
    pass


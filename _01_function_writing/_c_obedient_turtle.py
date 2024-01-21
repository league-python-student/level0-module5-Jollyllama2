"""
Make an obedient turtle that will obey commands to draw shapes.
"""
from tkinter import messagebox, simpledialog, Tk
import turtle

def my_turtle(turtle):

    turtle.goto(x = 20, y = 50)
    turtle.pendown()
    turtle.forward(100)
    turtle.left(90)
    my_turtle.forward(100)


if __name__ == '__main__':
    # TODO)
    #   1. Create a turtle.
    my_turtle = turtle.Turtle()

    #   2. Write 3 method definitions for drawing a square, triangle, and
    #      circle.

    #   3. Ask the user for the for a shape to draw.
    #   4. Draw the appropriate shape depending on their answer (call the right
    #      function)
    pass

"""
Go to the recipe to run the demonstration before starting this program
"""
x = 100 
y = 600
def setup():
    # Set the size of your sketch to be a rectangle like in the recipe demonstration
    size(6007,6007)
    noFill()
    ellipse(x,y,200,200)
    ellipse(x + 125,y-100,200,200)
    ellipse(x + 250 ,y ,200,200)
    ellipse(x + 350,y-100,200,200)
    ellipse(x + 460,y,200,200)
    ellipse(x + 580,y-100,200,200)
    ellipse(x + 700, y ,200,200)
    # Call the noFill() command so all the ellipses will be transparent
    noFill()
def draw():
    # Use a for loop to make the first set of rings that will start in the left half
    # of the window
    #for i in range (5):
        #ellipse(x,y,200,200)
        #ellipse(x + 125,y-100,200,200)
       # ellipse(x + 250 ,y ,200,200)
        #ellipse(x + 350,y-100,200,200)
       # ellipse(x + 460,y,200,200)
        #ellipse(x + 580,y-100,200,200)
        #ellipse(x + 700, y ,200,200)
    x += 50
    # Make this set of rings move across the sketch to the right 
    # Hint: Make two variables, one for x and another for the speed. 
    #       Then increase x by the amount in speed.
        
    # When the rings reach the right side of the sketch, reverse the direction so
    # they move.
    # Hint: speed = -speed */

         
    # When the rings reach the left side of the sketch, reverse the direction again
        
    # CHALLENGE - to finish the Amazing Rings
     
    # Add another for loop to draw the second set of rings that will start in the
    # right half of the window
        
    # Make this set of rings move in the opposite direction to the other rings
    # These rings must also "bounce" off the sides of the window.
    pass

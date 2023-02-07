# Import turtle package
import turtle
 
# Creating a turtle object(pen)
pen = turtle.Turtle()

sc = turtle.Screen()

# Defining a method to form a semicircle
# with a dynamic radius, color and center point
# pen.back(100)

def semi_circle(col, rad, val):
    # Move the turtle to the middle of the screen
    pen.up()
    pen.setpos(val-150, 0)
    pen.down()   

# Set the fill color of the semicircle

    pen.color(col)
 
    # Draw a circle
    pen.circle(rad,-180)
    
    # Move the turtle to air
    pen.up()
 
    # Move the turtle to a given position
    pen.setpos(val, 0)
 
    # Move the turtle to the ground
    pen.down()
 
    pen.right(-180)
  
# Set the colors for drawing
col = ['violet', 'indigo', 'blue',
       'green', 'yellow', 'orange', 'red']

# Setup the screen features
sc.setup(600, 600)
 
 
# Setup the turtle features
pen.right(90)
pen.width(10)
pen.speed(5)
 
# Loop to draw 7 semicircles
for i in range(7):
     semi_circle(col[i], 10*(
       i + 15), -10*(i + 1))

# Hide the turtle
pen.hideturtle()
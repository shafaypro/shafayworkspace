import turtle
t = turtle.Pen()
t.forward(50)  #moves 50 toward the direction
t.left(90) # moves the pointer toward the left
t.forward(50)  # movinf the turtle to the forward position
t.left(50) # mocing the turtle to hte left
t.forward(100) # moving the turtle in the forward possition
'''
# for loops in Turtle
for i in range(0,8):
	t.forward(50)
	t.left(45)
t.reset() # this resets the turtle in the screen
for i in range (1,38):
	t.forward(100)
	t.left(172)
t.reset() # this resets the turtle
for i in range(1,20):

	t.forward(100)
	t.left(95)
'''

# up down fucntion in the peb
t.right(90) # moves to the right position
t.reset() # clears the screen
t.left(180)
t.forward(100)
t.right(180)
t.up() # this moves the cursor from one pace to anpther
# put the pen down after the movements
t.down()
# moving the pen up and the down

t = turtle.Pen()
t.color(0,0,1) # first specify the color with rgb values
t.begin_fill() # remembers that it will have the fill starting point there

for i in range(0,5):
	t.forward(50)
	t.right(90)
t.end_fill()

t.circle(16)
t.setheading(0)  # intial possiting

#function in turtle

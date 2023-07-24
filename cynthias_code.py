from turtle import *


pencolor('dark green')
pensize(20)
speed(100)

# Outline Square
for i in range(4): 
 forward(140)
 left(90)
# Fill Square
for i in range(6): 
 forward(140-(i*20))
 left(90)
 forward(140-(i*20))
 backward(120-(i*20))
 right(90)
 backward(140-(i*20))

# Get into position for first eye
penup() 
forward(30)
pendown()
pencolor('black') 

# Draw first eye
for i in range(4):
 forward(20)
 right(90)

# Get into position for second eye
penup()
forward(60)
pendown()
pencolor('black')

# Draw second eye
for i in range(4):
 forward(20)
 right(90)

# Get into position for nose
penup()
backward(30)
right(90)
forward(34)
left(90)
pendown()

# Draw Nose
forward(20)
right(90)
forward(30)
right(90)
forward(20)
right(90)
forward(30)

# Get into position for left nostril
backward(15)
left(90)
forward(15)
left(90)

# Draw Left Nostril 
forward(30)

# Get into position for right nostril 
backward(30)
left(90)
forward(50)
right(90)

# Draw Right Nostril 
forward(30)

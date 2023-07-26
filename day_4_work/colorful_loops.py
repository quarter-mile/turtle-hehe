from turtle import *


setup(1.0, 1.0)

# Canvas
bgcolor('black')
speed(10)
pensize(3)
pencolor("pink")

# Square
# for i in range(4):
 # forward(100)
 # left(90)

# Spirograph
# for i in range(36): # Because left is set to 10
  # circle(50)
  # left(10)
  
# Colorful spirograph
for i in range(6):
  for colors in ["white", "pink", "purple", "light blue", "light green", "orange"]:
    color(colors)
    circle(50)
    left(10)

hideturtle()

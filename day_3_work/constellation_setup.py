from turtle import *


setup(1.0, 1.0)

bgpic('4.stars.png')
shape("turtle")
pensize(1)
left(90)
color("light blue")

def fxn(x, y):
  print("x: %d, y: %d" % (x, y))
  pencolor("white")
  goto(x,y)
  stamp()

# Print coordinate where clicked:
pendown()
onscreenclick(fxn)

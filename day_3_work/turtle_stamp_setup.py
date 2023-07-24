from turtle import *


setup(1.0, 1.0)

bgpic('3.plane.png')
shape("turtle")
pensize(5)
color("light green")

penup() # Need this with stamp()

goto(75, 75)
# Drawing a cute lil circle in the middle
# fillcolor('light green')
begin_fill()
circle(25)
end_fill()

color("pink")
stamp()

goto(-75, 75)
begin_fill()
circle(25)
end_fill()

color("light blue")
left(90)
stamp()

goto(-75, -75)
begin_fill()
circle(25)
end_fill()

color("orange")
left(90)
stamp()


goto(75, -75)
begin_fill()
circle(25)
end_fill()

color("light green")
left(90)
stamp()

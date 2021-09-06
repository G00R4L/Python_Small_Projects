import turtle

#WINDOW TITLE
turtle.title("G00R4L Animation")


#BACKGROUND COLOR
turtle.bgcolor("lightgray")

#PEN SIZE (circle thickness)
turtle.pensize(2)

#PEN SPEED (speed of drawing)
turtle.speed(0.5)

#PEN COLORS (here is the array of circle colors)
color = ["red", "blue", "green", "orange"]

#LOOP OF DRAWING (here is, a loop wchich drawing the circles)
for a in range(9):
    for i in color:
        turtle.color(i)
        turtle.circle(100)
        turtle.left(10)

turtle.mainloop()
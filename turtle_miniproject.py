import turtle

window = turtle.Screen()
window.bgcolor("#87cefa")
window.setup (width=800, height=600, startx=0, starty=0)

class Shapes():
    # Make the ground
    def ground():
        soil = turtle.Turtle()
        soil.up()
        soil.setpos(-100, -200)
        soil.down()
        soil.color("brown")
        soil.begin_fill()
        i = 0
        while i < 2:
            soil.speed(8)
            soil.forward(400)
            soil.left(90)
            soil.forward(200)
            soil.left(90)
            i += 1
        soil.end_fill()
        Shapes.flower()
        
    # Make a flower
    def flower():
        daisy = turtle.Turtle()
        daisy.up()
        daisy.setpos(-50, 0)
        daisy.down()
        daisy.color("#7b68ee", "#ffd700")
        daisy.begin_fill()
        i = 0
        while i < 36:
            daisy.speed(10)
            daisy.forward(100)
            daisy.right(170)
            i += 1
        daisy.end_fill()
        daisy.forward(50)
        daisy.pensize(4)
        daisy.setheading(270)
        daisy.color("green")
        daisy.forward(150)
        Shapes.circle()

    # Make a circle flower
    def circle():
        pretty = turtle.Turtle()
        pretty.up()
        pretty.setpos(100, 0)
        pretty.down()
        pretty.color("#ff69b4", "#ffc0cb")
        pretty.begin_fill()
        pretty.circle(50)
        pretty.end_fill()
        pretty.setheading(270)
        pretty.pensize(3)
        pretty.color("green")
        pretty.forward(150)
        pretty.up()
        pretty.setheading(0)
        pretty.forward(180)
        pretty.setheading(90)
        pretty.forward(200)
        pretty.pensize(3)
        pretty.color("#48d1cc", "#ffd700")
        pretty.begin_fill()
        pretty.circle(50)
        pretty.end_fill()
        pretty.setheading(180)
        pretty.up()
        pretty.forward(50)
        pretty.pensize(4)
        pretty.setheading(270)
        pretty.color("green")
        pretty.down()
        pretty.forward(200)
        Shapes.sun()

    # Sunshine
    def sun():
        shine = turtle.Turtle()
        shine.color("#ffff00", "#ffd700")
        shine.up()
        shine.setpos(-300, 150)
        shine.down()
        shine.begin_fill()
        i = 0
        while i < 36:
            shine.speed(8)
            shine.forward(180)
            shine.right(170)
            i += 1
        shine.end_fill()
        window.exitonclick()
        
Shapes.ground()

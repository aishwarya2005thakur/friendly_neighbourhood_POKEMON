import turtle

def draw_circle(color, radius, x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

def draw_ear(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor("yellow")
    turtle.begin_fill()
    turtle.goto(x - 20, y + 60)
    turtle.goto(x + 20, y + 60)
    turtle.goto(x, y)
    turtle.end_fill()

def draw_face():
    draw_circle("yellow", 100, 0, -50)
    draw_circle("black", 10, -35, -20)  # left eye
    draw_circle("black", 10, 35, -20)   # right eye
    draw_circle("red", 15, -60, -30)    # left cheek
    draw_circle("red", 15, 60, -30)     # right cheek
    draw_circle("black", 20, 0, -50)    # nose
    turtle.goto(0, -50)
    turtle.setheading(-60)
    turtle.pendown()
    turtle.circle(20, 120)  # mouth
    turtle.penup()

def draw_tail():
    turtle.goto(100, -50)
    turtle.pendown()
    turtle.fillcolor("yellow")
    turtle.begin_fill()
    turtle.goto(120, -30)
    turtle.goto(140, -50)
    turtle.goto(120, -70)
    turtle.goto(100, -50)
    turtle.end_fill()
    turtle.penup()

def main():
    turtle.speed(3)
    draw_face()
    draw_ear(-60, 50)  # left ear
    draw_ear(60, 50)   # right ear
    draw_tail()
    turtle.hideturtle()
    turtle.done()

if __name__ == "__main__":
    main()

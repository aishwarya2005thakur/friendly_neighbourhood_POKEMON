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
    draw_circle("gray", 30, x, y)
    draw_circle("pink", 20, x, y + 10)  # Inner ear

def draw_face():
    draw_circle("gray", 60, 0, -30)  # Head
    draw_circle("black", 10, -25, -15)  # Left eye
    draw_circle("black", 10, 25, -15)   # Right eye
    draw_circle("white", 5, -25, -15)   # Left eye highlight
    draw_circle("white", 5, 25, -15)    # Right eye highlight
    draw_circle("pink", 15, 0, -40)      # Nose

def draw_mouth():
    turtle.penup()
    turtle.goto(-10, -50)
    turtle.pendown()
    turtle.setheading(-60)
    turtle.circle(10, 120)  # Mouth curve
    turtle.penup()

def draw_body():
    draw_circle("gray", 70, 0, -90)  # Body

def draw_tail():
    turtle.pendown()
    turtle.goto(0, -90)
    turtle.setheading(-30)
    turtle.forward(50)  # Tail
    turtle.penup()

def main():
    turtle.speed(3)
    draw_body()
    draw_tail()
    draw_face()
    draw_ear(-40, 20)  # Left ear
    draw_ear(40, 20)   # Right ear
    draw_mouth()
   
    turtle.hideturtle()
    turtle.done()

if __name__ == "__main__":
    main()

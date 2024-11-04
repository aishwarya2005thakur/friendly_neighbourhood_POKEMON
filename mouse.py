import turtle

def draw_circle(color, radius, x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

def draw_body():
    draw_circle("gray", 70, 0, -90)  # Body

def draw_face():
    draw_circle("gray", 60, 0, -30)  # Centered head
    draw_circle("black", 10, -25, -15)  # Left eye
    draw_circle("black", 10, 25, -15)   # Right eye
    draw_circle("white", 5, -25, -15)   # Left eye highlight
    draw_circle("white", 5, 25, -15)    # Right eye highlight
    draw_circle("pink", 15, 0, -40)      # Nose

def draw_tail():
    turtle.penup()
    turtle.goto(0, -90)
    turtle.setheading(270)  # Point downwards for the tail
    turtle.pendown()
    # Draw a curly tail similar to a pig's
    for _ in range(3):  # Three loops for the curl
        turtle.circle(5, 180)  # Half circle
        turtle.right(180)  # Change direction for next half
    turtle.penup()

def draw_ears():
    # Draw mouse-like ears
    draw_circle("gray", 25, -50, 20)  # Left ear (smaller and more rounded)
    draw_circle("pink", 15, -50, 30)  # Inner left ear
    draw_circle("gray", 25, 50, 20)   # Right ear (smaller and more rounded)
    draw_circle("pink", 15, 50, 30)   # Inner right ear

def main():
    turtle.speed(3)
    draw_body()          # Draw body first
    draw_face()         # Draw face next
    draw_tail()         # Draw curly tail
    draw_ears()         # Draw ears last
    turtle.hideturtle()
    turtle.done()

if __name__ == "__main__":
    main()

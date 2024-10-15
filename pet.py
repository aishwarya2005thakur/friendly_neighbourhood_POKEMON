from tkinter import HIDDEN, NORMAL, Tk, Canvas

def toggle_eyes():
    current_color = c.itemcget(eye_left, 'fill')
    new_color = c.body_color if current_color == 'white' else 'white'
    current_state = c.itemcget(pupil_left, 'state')
    new_state = NORMAL if current_state == HIDDEN else HIDDEN
    c.itemconfigure(pupil_left, state=new_state)
    c.itemconfigure(pupil_right, state=new_state)
    c.itemconfigure(eye_left, fill=new_color)
    c.itemconfigure(eye_right, fill=new_color)

def blink():
    toggle_eyes()
    root.after(250, toggle_eyes)
    root.after(3000, blink)

def toggle_pupils():
    if not c.eyes_crossed:
        c.move(pupil_left, 10, -5)
        c.move(pupil_right, -10, -5)
        c.eyes_crossed = True
    else:
        c.move(pupil_left, -10, 5)
        c.move(pupil_right, 10, 5)
        c.eyes_crossed = False

def toggle_tongue():
    if not c.tongue_out:
        c.itemconfigure(tongue_tip, state=NORMAL)
        c.itemconfigure(tongue_main, state=NORMAL)
        c.tongue_out = True
    else:
        c.itemconfigure(tongue_tip, state=HIDDEN)
        c.itemconfigure(tongue_main, state=HIDDEN)
        c.tongue_out = False

def cheeky(event):
    toggle_tongue()
    toggle_pupils()
    hide_happy(event)
    root.after(1000, toggle_tongue)
    root.after(1000, toggle_pupils)

def show_happy(event):
    if (20 <= event.x <= 350) and (20 <= event.y <= 350):
        c.itemconfigure(cheek_left, state=NORMAL)
        c.itemconfigure(cheek_right, state=NORMAL)
        c.itemconfigure(blush_left, state=NORMAL)  # Show left blush
        c.itemconfigure(blush_right, state=NORMAL)  # Show right blush
        c.itemconfigure(mouth_happy, state=NORMAL)
        c.itemconfigure(mouth_normal, state=HIDDEN)
        c.itemconfigure(mouth_sad, state=HIDDEN)
        c.happy_level = 10

def hide_happy(event):
    c.itemconfigure(cheek_left, state=HIDDEN)
    c.itemconfigure(cheek_right, state=HIDDEN)
    c.itemconfigure(blush_left, state=HIDDEN)  # Hide left blush
    c.itemconfigure(blush_right, state=HIDDEN)  # Hide right blush
    c.itemconfigure(mouth_happy, state=HIDDEN)
    c.itemconfigure(mouth_normal, state=NORMAL)
    c.itemconfigure(mouth_sad, state=HIDDEN)

def sad():
    if c.happy_level == 0:
        c.itemconfigure(mouth_happy, state=HIDDEN)
        c.itemconfigure(mouth_normal, state=HIDDEN)
        c.itemconfigure(mouth_sad, state=NORMAL)
    else:
        c.happy_level -= 1
    root.after(5000, sad)

root = Tk()
c = Canvas(root, width=400, height=400)
c.configure(bg='black', highlightthickness=0)
c.body_color = 'pink'

# Draw body, ears, and feet
body = c.create_oval(35, 20, 365, 350, outline=c.body_color, fill=c.body_color)
ear_left = c.create_polygon(75, 80, 75, 10, 165, 70, outline=c.body_color, fill=c.body_color)
ear_right = c.create_polygon(255, 45, 325, 10, 320, 70, outline=c.body_color, fill=c.body_color)
foot_left = c.create_oval(65, 320, 145, 360, outline=c.body_color, fill=c.body_color)
foot_right = c.create_oval(250, 320, 330, 360, outline=c.body_color, fill=c.body_color)

# Eyes and pupils
eye_left = c.create_oval(130, 110, 160, 170, outline='black', fill='white')
pupil_left = c.create_oval(140, 145, 150, 155, outline='black', fill='black')
eye_right = c.create_oval(230, 110, 260, 170, outline='black', fill='white')
pupil_right = c.create_oval(240, 145, 250, 155, outline='black', fill='black')

# Create inner ear triangles
inner_ear_left = c.create_polygon(75, 10, 60, 45, 90, 45, outline='black', fill='black')
inner_ear_right = c.create_polygon(325, 10, 340, 45, 310, 45, outline='black', fill='black')


# Mouths
mouth_normal = c.create_line(170, 250, 200, 272, 230, 250, smooth=1, width=2, state=NORMAL)
mouth_happy = c.create_line(170, 250, 200, 282, 230, 250, smooth=1, width=2, state=HIDDEN)
mouth_sad = c.create_line(170, 250, 200, 232, 230, 250, smooth=1, width=2, state=HIDDEN)

# Tongue
tongue_main = c.create_rectangle(170, 250, 230, 290, outline='red', fill='red', state=HIDDEN)
tongue_tip = c.create_oval(170, 285, 230, 300, outline='red', fill='red', state=HIDDEN)

# Cheeks and blush
cheek_left = c.create_oval(70, 180, 120, 230, outline='light coral', fill='light coral', state=HIDDEN)
cheek_right = c.create_oval(280, 180, 330, 230, outline='light coral', fill='light coral', state=HIDDEN)
blush_left = c.create_oval(70, 200, 130, 230, outline='red', fill='red', state=HIDDEN)
blush_right = c.create_oval(270, 200, 330, 230, outline='red', fill='red', state=HIDDEN)

# Hair (croissant-style)
hair_base = c.create_oval(130, -40, 270, 80, outline='pink', fill='pink')
curl1 = c.create_oval(150, -60, 190, -20, outline='pink', fill='pink')
curl2 = c.create_oval(210, -60, 250, -20, outline='pink', fill='pink')
curl3 = c.create_oval(130, -40, 170, 0, outline='pink', fill='pink')
curl4 = c.create_oval(230, -40, 270, 0, outline='pink', fill='pink')
swirl = c.create_arc(150, -10, 250, 60, start=0, extent=180, outline='pink', width=5)

# Initialize character state
c.happy_level = 10
c.eyes_crossed = False
c.tongue_out = False

# Bind events
c.pack()
c.bind('<Motion>', show_happy)
c.bind('<Leave>', hide_happy)
c.bind('<Double-1>', cheeky)

root.after(1000, blink)
root.after(5000, sad)
root.mainloop()

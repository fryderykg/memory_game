# implementation of card game - Memory
try:
    import SimpleGUICS2Pygame.simpleguics2pygame as simplegui
except ImportError:
    import simplegui
import random

num_list = []
exposed = []
num_pos = [5, 80]
a, b = 0, 50
state = 0
index1 = None
index2 = None
score = 0


# helper function to initialize globals
def new_game():
    global num_list, exposed, score
    num_list = [n for n in range(8)] * 2
    random.shuffle(num_list)
    exposed = [0] * 16
    score = 0
    label.set_text("Turns = " + str(score))


# define event handlers
def mouseclick(pos):
    # add game state logic here
    global state, index1, index2, score

    if exposed[pos[0] // 50] == 0:
        exposed[pos[0] // 50] = not exposed[pos[0] // 50]
        if state == 0:
            state = 1
            index1 = pos[0] // 50
        elif state == 1:
            state = 2
            index2 = pos[0] // 50
            score += 1
        else:
            state = 1
            if num_list[index1] != num_list[index2]:
                exposed[index1] = False
                exposed[index2] = False
            index1 = pos[0] // 50
    label.set_text("Turns = " + str(score))


# cards are logically 50x100 pixels in size
def draw(canvas):
    global num_pos, a, b
    for number in num_list:
        canvas.draw_text(str(number), num_pos, 70, 'White')
        if num_pos[0] < 755:
            num_pos[0] += 50
        else:
            num_pos[0] = 5

    for number in exposed:
        if not number:
            canvas.draw_polygon([[a, 0], [a, 100], [b, 100], [b, 0]],
                                1, 'Black', 'Green')
        if b < 800:
            a, b = b, b + 50
        else:
            a, b = 0, 50


# create frame and add a button and labels
frame = simplegui.create_frame("Memory", 800, 100)
frame.add_button("Reset", new_game)
label = frame.add_label("Turns = 0")


# register event handlers
frame.set_mouseclick_handler(mouseclick)
frame.set_draw_handler(draw)

# get things rolling
new_game()
frame.start()

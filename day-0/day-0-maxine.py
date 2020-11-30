import turtle


def draw_multicolour_square(t, sz):
    for x in range(0, 4):
        t.forward(sz)
        t.left(90)


wn = turtle.Screen()

tess = turtle.Turtle()
tess.pensize(7)
tess.left(90)

size = 32
for i in range(20):
    draw_multicolour_square(tess, size)
    size = size + 20
    tess.forward(25)
    tess.right(18)

turtle.mainloop()



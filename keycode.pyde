siz = 250
def setup ():
    background (0)
    size (500,500)
def draw ():
    ellipseMode (CENTER)
    noStroke ()
    ellipse (250,250,siz,siz)
def keyPressed ():
    global siz
    if key == CODED:
        if keyCode == SHIFT:
            siz = siz + 10
            clear()
        elif keyCode == CONTROL:
            siz = siz - 10
            clear()

x = 0
y = 0
def setup ():
    size (500,500)
def draw ():
    global x
    global y
    background (255)
    fill (0)
    rect (x,y,50,50)
    stroke(255)
    line (x,y,x+50,y+50)
    line (x,y,x+50,y)
    line (x,y,x,y+50)
    line (x,y+50,x+50,y)
    line (x,y+50,x+50,y+50)
    line (x+50,y,x+50,y+50)


def keyPressed ():
    global x
    global y
    if key == CODED:
        if keyCode == SHIFT:
            x = (random(0,500))
            y = (random(0,500))
    

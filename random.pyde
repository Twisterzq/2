x = 0
y = 0
def setup ():
    size (500,500)
def draw ():
    global x
    global y
    background (255)
    stroke (1)
    fill (10,10,10)
    rect (x-18,y-50,40,100)
    stroke (255,5,5)
    strokeWeight (25)
    point (x,y)
    stroke (255,243,5)
    strokeWeight (25)
    point (x,y+30)
    stroke (5,255,65)
    strokeWeight (25)
    point (x,y-30)

def keyPressed ():
    global x
    global y
    if key == CODED:
        if keyCode == SHIFT:
            x = (random(0,500))
            y = (random(0,500))
    

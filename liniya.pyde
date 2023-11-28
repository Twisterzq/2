y = 1
def setup ():
    size (500,500)
    background (100)
def draw ():
    global y
    stroke(random(1,255),random(1,255),random(1,255))
    line (250,250,400,y)
    y = y + 1

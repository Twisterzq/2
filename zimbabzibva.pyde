x = 250
y = 250
def setup ():
    size (500,500)
    background (100)
def draw ():
    frameRate (5)
    fill (random(1,255),random(1,255),random(1,255))
    global x
    global y
    ellipse (x,x,random(10,30),random(10,30))
    fill (random(1,255),random(1,255),random(1,255))
    ellipse (y,x,random(10,30),random(10,30))
    fill (random(1,255),random(1,255),random(1,255))
    ellipse (y,y,random(10,30),random(10,30))
    fill (random(1,255),random(1,255),random(1,255))
    ellipse (x,y,random(10,30),random(10,30))

    x = x + 10
    y = y - 10

a = 1
b = 30
c = 1
d = 100
def setup ():
    size (1000,500)
    background (150)
def draw ():
    frameRate (120)
    global a
    global b
    global c
    global d
    strokeWeight (a)
    stroke (255)
    line (100,250,900,250)
    noStroke ()
    fill (1)
    ellipse (d,250,100,100)
    if mousePressed and d <= 900 :
        d = d + 5
    while (a != 100):
        a = a + 1
    while (b != 100):
        b = b + 1
    if c == 130:
        noLoop()

x= 0
y = 0
def setup ():
    size (1000,1000)
def draw ():
    global x,y
    for x in range (20,340,20):
        colorMode(HSB, 360, 100, 100)
        fill (x,100,100)
        ellipse (x +480,x+480,x,x)

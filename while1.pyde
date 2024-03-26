x = 0
y = 0
def setup ():
    size (600,300)
def draw ():
    global x, y
    while x != 600 and y != 300:
        x = x + 6
        y = y + 3
        fill (random(0,255),random(0,255),random(0,255))
        ellipse (x,y,10,10)
    
    
    

x = -200
y = 400
def setup ():
    size (500,500)
def draw ():
    global x, y
    background (100)
    for step in range (1,6):
        translate (50,50)
        ellipse (x,y,50,50)
    x = x + 2
    y = y - 2
        

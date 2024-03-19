x = 0
y = 0
def setup ():
    size (500,500)
def draw ():
    global x, y
    for step in range (1,12):
        translate (40,0)          
        fill (random(0,255),random(0,255),random(0,255))
        rect (x,y,20,20)
    y = y + 5
    if keyPressed and keyCode == LEFT:
        x = x - 1
    if keyPressed and keyCode == RIGHT:
        x = x + 1
        

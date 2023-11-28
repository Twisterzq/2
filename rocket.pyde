y = 0
def setup ():
    size (200,500)
    background (100)
    
def draw ():
    global y
    frameRate (15)
    background (100)
    translate (0,y)
    translate (75,350)
    fill (255,1,1)
    rect (0,0,50,100)
    fill (255,255,255)
    triangle (0,0,50,0,25,-50)
    translate (25,40)
    ellipse (0,0,25,25)
    translate (-25,58)
    fill (242,115,51)
    triangle (0,0,50,0,25,random(20,30))
    y = y - 2

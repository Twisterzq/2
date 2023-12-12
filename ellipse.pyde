a = 1
def setup ():
    size (1000,500)
def draw ():
    frameRate (150)
    global a 
    a = a + 1
    point (100,a)
    if a >= 150:
        translate (a,0)
    strokeWeight (100)
    ellipse (50,50,100,100)
    

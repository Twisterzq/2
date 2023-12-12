a = 1
b = 1
c = 1
def setup ():
    size (1000,500)
def draw ():
    frameRate (150)
    global a 
    global b
    global c
    a = a + 1
    c = c + 1
    
    strokeWeight (c)
    if c == 100:
        
    point (-100,-a)
    if c >= 100:
        b = b + 1
        translate (b,0)
    point (100,250)
    

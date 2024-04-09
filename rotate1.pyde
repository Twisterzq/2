angle = 0

def setup():
    size(600, 400)
    
def draw():
    global angle
    translate (300,200)
    for step in range (100):
        fill (78,234,76)
        ellipse (0,0,40,40)
        fill (234,222,76)
        rect (120,0,40,40)
        rotate (radians(360/8))
        
    

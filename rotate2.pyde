angle = 0

def setup():
    size(600, 400)
    
def draw():
    global angle
    fill (179,199,227)
    ellipse (300,200,30,30)
    translate (300,200)
    for step in range (8):
        fill (76,143,234)
        rect (40,0,20,20)
        fill (52,109,185)
        triangle (80,0,80,20,70,10)
        fill (127,170,229)
        ellipse (100,10,10,30)
        rotate (radians(360/8))
        
    

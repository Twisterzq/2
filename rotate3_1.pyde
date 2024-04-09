angle = 0

def setup():
    size(600, 400)
    
def draw():
    background (100)
    global angle
    fill (179,199,227)
    translate (300,200)
    if keyPressed and keyCode == LEFT:
        angle = angle - 1
    if keyPressed and keyCode == RIGHT:
            angle = angle + 1
    rotate (radians(angle))
    for step in range (8):
        fill (1,1,1)
        line (10,0,33,0)
        fill (174,202,240)
        ellipse (0,0,30,30)
        push()
        fill (80,120,170)
        translate (45,-12)
        rotate (radians (45))
        rect (0,0,20,20)
        pop ()
        fill (12,65,137)
        ellipse (100,0,10,30)
        rotate (radians(360/8))
        
    

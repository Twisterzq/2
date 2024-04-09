angle = 0
r = 0
def setup():
    size(600, 400)
    
def draw():
    #background (100)
    global angle, r
    noStroke ()
  #  frameRate (5)
    fill (179,199,227)
    translate (300,200)
    #if keyPressed and keyCode == LEFT:
    #    angle = angle - 1
    #if keyPressed and keyCode == RIGHT:
    angle = angle + 1
    rotate (radians(angle))
    for step in range (12):
        fill (221,250,8)
        ellipse(0,0,r+20,r+20)
        fill (255,255,255)
        ellipse (0,0,r+10,r+10)
        fill (255,0,0)
        ellipse (30,0,r+40,r+10)
        fill (26,59,216)
        quad (80-r,0,100,-20-r,r+120,0,r+100,r+20)
        fill (26,216,81)
        rect (120,-20,r+50,r+20)
        rotate (radians(360/12))
        
    

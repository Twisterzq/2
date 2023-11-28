def setup():
    size (500,500)
    
def draw ():
    frameRate (15)
    background (1)
    strokeWeight (random(1,20))
    stroke (random(1,255),random(1,255),random(1,255))
    line (250,250,random(1,500),random(1,500))

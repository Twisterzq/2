x = 0
y = 50
z = 25
yy = -50
def setup ():
    size (500,500)

    
def draw ():
    background (100)
    fill (random(1,255),random(1,255),random(1,255))
    frameRate (10)
    global x 
    global y 
    global z
    global yy
    translate (0,50)
    triangle (x,x,y,x,z,yy)
    x = x + 1
    y = y + 1
    z = z + 1
    yy = yy + 1

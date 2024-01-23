shar_x = 250
shar_y = 300
rx = 200
ry = 1
sx = 1
def collideRectCircle(rx, ry, rw, rh, cx, cy, diameter):
    testX = cx
    testY = cy
    if cx < rx:
        testX = rx
        
    elif cx > rx + rw:
        testX = rx + rw
        
    if cy < ry:
        testY = ry
        
    elif cy > ry + rh:
        testY = ry + rh
    distance = dist(cx,cy,testX,testY) 
    if distance <= diameter/2:
        return True
    else:
        return False
def setup ():
    size (500,600)
def draw ():
    global shar_x, shar_y,rx,ry
    background(100)
    #if collideRectCircle(200,550,100,50,shar_x,shar_y,100):
    shar_x = shar_x +
    if keyPressed and key == CODED:
        if keyCode == LEFT:
            rx = rx - 3
        if keyCode == RIGHT:
            rx = rx + 3
    rect (rx,550,100,50)

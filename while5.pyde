x = 125
y = 0
z = 250
k = 375
def collidePointCircle(x, y, cx, cy, d):
    if dist(x,y,cx,cy) <= d/2:
        return True
    else:
        return False

def setup ():
        size (500,500)
        background (230)
def draw ():
    global x, y ,z, k
    for y in range (50,500,50):
        if collidePointCircle(mouseX, mouseY, x, y, 50):
            fill (1)
            ellipse (x,y,50,50)
        else:
            fill (255)
        ellipse (x,y,50,50)
        ellipse (x+125,y,50,50)
        ellipse (x+250,y,50,50)


        
        

    
    

x = 0
y = 0
def collidePointRect(pointX, pointY, x, y, xW, yW):
#если точка находится между краёв прямоугольника:
    if (pointX >= x) and (pointX <= x + xW) and (pointY >= y) and (pointY <= y + yW): 
        return True
    return False

def setup ():
    size (600,600)
def draw ():
    global x, y
    for x in range (0,600,20):
        for y in range (0,600,20):
            rect (x,y,20,20)
            if collidePointRect(mouseX, mouseY, x, y, 20, 20):
                fill(255, 0, 0)
                rect (x,y,20,20)
                fill (255)
            else:
                fill(255)
    strokeWeight (10)
    point (mouseX,mouseY)
    strokeWeight (1)
    fill (255)
    
        

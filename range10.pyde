x = 50
y = 400
def setup ():
    size (255,255)
def draw ():
    global x, y
    background (100)
    for step in range (1,5):
        translate (50,50)
        fill (mouseX)
        ellipse (0,0,50,50)
        
        

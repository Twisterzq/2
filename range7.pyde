x = 0
y = 0
def setup ():
    size (500,500)
def draw ():
    global x, y
    for step in range (1,6):
        translate (50,50)
        ellipse (0,0,50,50)
        

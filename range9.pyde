x = 50
y = 400
def setup ():
    size (700,700)
def draw ():
    global x, y
    background (100)
    for step in range (1,6):
        translate (100,100)
        rect (0,0,x,x)
    x = x + 2
        

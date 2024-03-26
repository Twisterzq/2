
def setup ():
    size (600,300)
    x = 0
    y = 300
    z = 0
    strokeWeight (5)
    while x != 600 and y != 0:
        y = y - 2
        x = x + 4
        colorMode(HSB, 360, 100, 100)
        line (x,300,x,y)
    
    
    

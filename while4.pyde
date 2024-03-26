x = 0
y = 500
z = 0
def setup ():
        size (500,500)
def draw ():
    global x, y ,z
    strokeWeight(10)
    while x != 500 and y != 0:
        x = x + 25
        y = y - 25
        line(x-10, x-10, x+10, x+10)
        line(x-10, x+10, x+10, x-10)
        line(x-10, y-10, x+10, y+10)
        line(x-10, y+10, x+10, y-10)
        
        

    
    

y = 0
x = 5
z = 10
k = -20
g = -30
d = -10

def setup ():
    size (100,100)

    
def draw ():
    frameRate (10)
    global y
    global x
    global z
    global k
    global g
    global d
    background (1,1,1)
    ellipse (10,y,5,5)
    ellipse (25,z,7,7)
    ellipse (38,y,3,3)
    ellipse (87,x,6,6)
    ellipse (90,y,2,2)
    ellipse (30,k,5,5)
    ellipse (10,g,5,5)
    ellipse (15,d,6,6)
    ellipse (40,k,4,4)
    ellipse (55,g,7,7)
    ellipse (56,k,6,6)
    ellipse (75,x,7,7)
    ellipse (65,d,3,3)
    ellipse (85,g,6,6)
    ellipse (89,d,5,5)
    y = y + 1
    x = x + 1
    z = z + 1
    k = k + 1
    g = g + 1
    d = d + 1
    

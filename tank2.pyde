d = 105
k = 1
xx = 1
def setup ():
    size (500,300)
def draw ():
    background (50)
    global d, xx
    fill (81,124,65)
    quad (100,200,120,120,350,120,330,200)
    fill (34,77,17)
    quad (280,125,280,105,390,d,390,d+20)
    fill (81,124,65)
    ellipse (270,120,100,60)
    fill (72,95,63)
    ellipse (120,190,70,70)
    ellipse (330,190,70,70)
    ellipse (175,200,50,50)
    ellipse (225,200,50,50)
    ellipse (275,200,50,50)
    d = d - 0.5
    if d == 75:
        d = d + 0.5
        xx = xx + 1
    push()
    translate (330,110)
    translate (xx,-xx)
    rotate(radians(162))
    rect (0,0,50,20)
    pop()
        
        


        
    
    

    

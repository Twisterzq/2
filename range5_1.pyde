x= 0
y = 0
def setup ():
    size (550,550)
def draw ():
    global x,y
    for x in range (50,550,100):
        fill (255,0,0)
        rect (x,250,50,50)
        rect (250,x,50,50)
        

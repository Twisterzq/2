x= 0
def setup ():
    size (800,200)
def draw ():
    global x
    for x in range (0,800,20):
        rect (x,0,20,20)
        rect (x,20,20,20)
        rect (x,40,20,20)

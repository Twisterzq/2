i = 0
def setup ():
    size (200,200)
def draw ():
    global i
    background (100)
    x = ["a","b","c"]
    text (x[i],100,100)
    if i == 2:
        i = 0
    if i < 0:
        i = 2
    if keyPressed and keyCode == LEFT:
        i = i - 1
    if keyPressed and keyCode == RIGHT:
            i = i + 1
        
    
    

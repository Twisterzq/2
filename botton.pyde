a = 1
def setup ():
    size (500,500)
def draw ():
    stroke (0)
    fill (a)
    rect (200,200,100,100)
def mouseClicked():
    global a
    if mouseX > 200 and mouseX <300 and mouseY > 200 and mouseY < 300:
        a = 100
    else:
        a = 1

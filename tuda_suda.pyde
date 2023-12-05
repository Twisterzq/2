x = 0
mode = "right"
def setup ():
    size (500,500)
def draw():
    frameRate (150)
    background (100)
    global mode
    global x
    if mode == "right":
        x = x + 1
    if mode == "left":
        x = x - 1
    ellipse (x,250,50,50)
    if x == 500:
        mode = "left"
    if x == 0:
        mode = "right"

a = 1
fps = 1
def setup ():
    size (500,500)
    background (150)
def draw ():
    global fps
    fps = fps + 1
    frameRate (60)
    textAlign (CENTER,CENTER)
    textSize (20)
    fill (255)
    rect (100,100,300,300)
    fill (1)
    text ("Click",250,250)
    if a == 10:
        noLoop()
        background (100)
        text ("Win",250,250)
    if a != 10 and fps >= 600 :
        background (100)
        text ("Lose",250,250)
def mouseClicked ():
    global a
    if mouseX >100 and mouseX <400 and mouseY >100 and mouseY <400:
        a = a + 1

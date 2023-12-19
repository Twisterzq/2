a = 1
def setup ():
    size (500,500)
    background (150)
def draw ():
    frameRate (60)
    textAlign (CENTER,CENTER)
    textSize (20)
    push()
    stroke (0)
    strokeWeight (0)
    fill (0,255,0)
    rect (50,50,100,50)
    fill (255,0,0)
    rect (50,150,100,50)
    fill (0,0,255)
    rect (50,250,100,50)
    fill (200)
    rect (50,350,100,50)
    fill (1)
    text ("Green",100,75)
    text ("Red",100,175)
    text ("Blue",100,275)
    text ("Rubber",100,375)
    pop()
    strokeWeight (10)
    if mouseButton == LEFT and mouseX > 50 and mouseX < 150 and mouseY >50 and mouseY <100:
        stroke (0,255,0)
    elif mouseX > 50 and mouseX < 150 and mouseY > 150 and mouseY < 200:
        stroke (255,0,0)
    elif mouseX > 50 and mouseX <150 and mouseY > 250 and mouseY < 300:
        stroke (0,0,255)
    elif mouseX > 50 and mouseX <150 and mouseY <350 and mouseY < 400:
        stroke(150)
    
    if mouseButton == LEFT:
        point (mouseX,mouseY)
    

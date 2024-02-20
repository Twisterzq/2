up = 0
down = 0
y = 200
x = -101
tw = 1
def collideRectRect (x, y, w, h, x2, y2, w2, h2):
    if (x + w >= x2) and  (x <= x2 + w2) and  (y + h >= y2) and (y <= y2 + h2):
        return True
    else:
        return False

def setup():
    size (600,300)
def draw ():
    background (50)
    global up, down,y,x,tw
    if keyPressed == True:
        if key == " " and up == 0 and down == 0:
            up = 40
    if up > 0:
        up = up - 1
        y = y - 3
    if down > 0:
        down = down - 1
        y = y + 3
    if up == 1:
        down = 40
    rect (100,y,50,100)
    if tw == 1:
        rect(x,250,20,50)
    if tw == 2:
        rect (x,240,40,60)
    if tw == 3:
        rect (x,260,30,40)
    x = x - 3
    if x < -100:
        x = random(600,1200)
        tw = round(random(0.5,3.4999))
        print(tw)
    collide1=collideRectRect(100,y,50,100,x,250,20,50)
    collide2=collideRectRect(100,y,50,100,x,240,40,60)
    collide3=collideRectRect(100,y,50,100,x,260,30,40)
    collide = collide1 or collide2 or collide3
    textSize (20)
    textAlign (CENTER,CENTER)
    if collide==True:
        clear()
        text ('Lose',300,150)
        noLoop()
        

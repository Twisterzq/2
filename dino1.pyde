up = 0
down = 0
y = 200
x = -101
tw = 1
score = 0
frames = 0
fframes = 1200
timer = 0
tp = 5
tpp = 0
px = 0
bc1 = 50
bc2 = 50
bc3 = 50
d = False
n = True
def collideRectRect (x, y, w, h, x2, y2, w2, h2):
    if (x + w >= x2) and  (x <= x2 + w2) and  (y + h >= y2) and (y <= y2 + h2):
        return True
    else:
        return False

def setup():
    size (600,300)
def draw ():
    background (bc1,bc2,bc3)
    global up, down,y,x,tw, score, frames, timer, tp, tpp, fframes, bc1, bc2, bc3, d ,n
    if keyPressed == True:
        if key == " " and up == 0 and down == 0:
            up = 40
    if up > 0:
        up = up - 1
        y = y - 4
    if down > 0:
        down = down - 1
        y = y + 4
    if up == 1:
        down = 40
    fill (58,147,63)
    rect (100,y,50,100)
    fill (92,191,98)
    if tw == 1:
        rect(x,250,20,50)
    if tw == 2:
        rect (x,240,40,60)
    if tw == 3:
        rect (x,260,30,40)
    x = x - tp
    if x < -100:
        x = random(600,1200)
        tw = round(random(0.5,3.4999))
        print(tw)
    fill (255,255,255)
    collide1=collideRectRect(100,y,50,100,x,250,20,50)
    collide2=collideRectRect(100,y,50,100,x,240,40,60)
    collide3=collideRectRect(100,y,50,100,x,260,30,40)
    collide = collide1 or collide2 or collide3
    textSize (20)
    textAlign (CENTER,CENTER)
    if collide==True:
        clear()
        text ('Lose, score =',415,50)
        noLoop()
    score = score + 1
    frames = frames + 1
    if frames == 60:
        timer = timer + 1
        frames = 0
    text ("time = ",50,50)
    text (timer,100,50)
    text (score,500,50)
    tp = tp + + tpp
    tpp = tpp + 0.000002
    fframes = fframes + 1
    if fframes >= 1200 and n == True and d == False:
        bc1 = bc1 + 0.0866
        bc2 = bc2 + 0.2916
        bc3 = bc3 + 0.3166
    if fframes >= 1200 and n == False and d == True:
        bc1 = bc1 - 0.0866
        bc2 = bc2 - 0.2916
        bc3 = bc3 - 0.3166
    if bc1 <= 51:
        bc1 = bc1 + 0.0866
    if bc2 <= 51:
        bc2 = bc2 + 0.2916
    if bc3 <= 51:
        bc3 = bc3 + 0.3166
    if bc1 >= 102:
        bc1 = bc1 - 0.0866
    if bc2 >= 225:
        bc2 = bc2 - 0.2916
    if bc3 >= 240:
        bc3 = bc3 - 0.3166
    if fframes >= 1800 and n == True and d == False:
        fframes = 0
        n == False
        d == True
    if fframes >= 1800 and n == False and d == True:
        fframes = 0
        n == True
        d == False
    print (d)
    

    
        

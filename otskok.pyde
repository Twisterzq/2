shar_x = 250
shar_y = 100
shar_dx = 3
shar_dy = 3
ladder_x = 200
ladder_width = 100
ladder_height = 25
razmer = 50
ladder_y = 575
shar_razmer = 50

def collideRectCircle (ladder_x, ladder_y, ladder_width, ladder_height,   shar_x, shar_y, shar_razmer):
    tX= shar_x
    tY = shar_y
    if shar_x < ladder_x:
        tX = ladder_x
    if shar_x > ladder_x + ladder_height:
        tX = ladder_x + ladder_width
    if shar_y < ladder_y:
        tY = ladder_y
    elif shar_y > ladder_y + ladder_height:
        tY = ladder_y + ladder_height
    distance = dist(shar_x,shar_y,tX,tY)
    if distance <= shar_razmer/2:
        return True
    else:
        return False
def setup():
    size (500,600)
def draw():
    background (150)
    global ladder_x, ladder_y, ladder_widt, shar, ladder, shar_dx, shar_dy
    global ladder_height, shar_x, shar_y, shar_razmer
    shar_x = shar_x + shar_dx
    shar_y = shar_y + shar_dy
    if shar_x >= 500:
        shar_dx = -shar_dx
    if shar_x <= 0:
        shar_dx = - shar_dx
    if shar_y <= 0 :
        shar_dy = -shar_dy
    textAlign (CENTER,CENTER)
    textSize (50)
    if shar_y >= 610:
        background (50)
        text(u"Проигрыш",250,300)
    ellipse (shar_x,shar_y,50,50)
    if keyPressed and key == CODED:
        if keyCode == LEFT:
            ladder_x = ladder_x - 3
        if keyCode == RIGHT:
            ladder_x = ladder_x + 3
    rect (ladder_x,ladder_y,100,25)
    if collideRectCircle(ladder_x, ladder_y, ladder_width, ladder_height,   shar_x, shar_y, shar_razmer):
        shar_dy = -random(4,6)
        shar_dx = random(-5, 5)
    

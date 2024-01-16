'''
Простой кликер. Тут нужно набрать 30 очков. При одном клике по кругу
должно набоираться 1 очко. Но почему-то
при клике набирается не одно очко, а сразу несколько.
Как исправить это?
'''


def collidePointCircle(x, y, cx, cy, d):
    if dist(x,y,cx,cy) <= d/2:
        return True
    else:
        return False

score = 0

def setup():
    size(600, 400)
    
def draw():
    global score
    background(100)
    textSize(20)
    
    if score < 30:
        text(u"очки:", 25, 25)
        text(score, 80, 25)
        text(u"Набери 30 очков!", 300, 25)
        textSize(15)
        ellipse(300, 200, 100, 100)
        fill(0)
        text(u"Клик ми!", 265, 205)
        fill(255)
        
    else:
        textAlign(CENTER, CENTER)
        text(u"Победа!", 300, 200)
                
def mouseClicked ():
    global score
    if collidePointCircle(mouseX, mouseY, 300, 200, 100):
        score = score + 1

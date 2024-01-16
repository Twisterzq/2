'''
Здесь при нажатии на левую кнопку мыши должен появляться заяц,
а если левая кнопка мыши не нажата — надпись «Никого нет».
Но всё сломалось! Надпись появляется всегда, причём какие-то
кракозябры. Заяц появляется при нажатии на ЛЮБУЮ клавишу мыши.
Как это исправить?

'''

def setup():
    size(600, 400)
    
def draw():
    background(100)
    translate(300, 200)
    if mousePressed and mouseButton == LEFT:
        push()
        translate(-30, -35)
        rotate(radians(65))
        ellipse(0,0, 70, 20)
        pop()
        push()
        translate(30, -35)
        rotate(radians(-65))
        ellipse(0,0, 70, 20)
        pop()
        ellipse(0,0, 60, 60)
        push()
        strokeWeight(10)
        point(10, -10)
        point(-10, -10)
        point(0, 5)
        pop()
        textAlign(CENTER, CENTER)
        textSize(20)    
        text(u"Никого нет!", 0, 0 )

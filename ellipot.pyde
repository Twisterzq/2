'''
Шарик должен отскакивать от всех стен, но
почему-то не отскакивает от правой, а улетает за неё.
Как исправить это?
'''

changeX = 1
changeY = 1
x = 0
y = 400

def setup():
    size(600,400)
    
def draw():
    global x,y,changeX,changeY
    background(100)
    ellipse(x,y,20,20)
    x = x + changeX
    y = y + changeY
    if x > 600:
        changeX = -3
    if x < 0:
        changeX = 3
    if y > 400:
        changeY = -3
    if y < 0:
        changeY = 3
    

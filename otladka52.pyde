'''
Программа должна рисовать снежинку —
х-крест, наложенный на +-крест —
которая едет.
Но почему-то одна из линий х-креста
не показывается. Почему?
'''

xAll = 300
myColor = 0
def setup():
    size(600, 600)
    colorMode(HSB, 360, 100, 100)
def draw():
    global xAll, myColor
    background(100)
    fill(myColor, 100, 100)
    translate(xAll, 0)
    translate(300, 300)
    for x in -200, -100, 0, 100, 200:
        ellipse(x, 0, 50, 50)
        
    for y in -200, -100, 0, 100, 200:
        ellipse(0, y, 50, 50)
        
    for x in -200, -100, 0, 100, 200:
        ellipse(x, x, 50, 50)
        
    for x in -200, -100, 0, 100, 200:
        ellipse(x, -x, 50, 50)
    
    xAll -= 1
    myColor += 1
    if myColor > 360:
        myColor = 0
    


    

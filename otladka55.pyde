'''
Эта программа должна рисовать ряд линий слева направо,
каждая следующая линия всё выше. Но почему-то ничего не рисуется.

Как исправить это?
'''

def setup():
    size(800, 600)
    strokeWeight(3)
    background(255)
    colorMode(HSB, 360, 100, 100)
    
   
    translate(0, 500)
    x = 0
    y = 0
    col = 0
    while x < 800:
        stroke(col, 100, 100)
        line(x, 0, x, -y)
        x = x + 6
        y = y + 2
        col = col + 3
        if col > 359:
            col = 0
    
        
    

'''
Этот код должен рисовать вертикальный ряд,
который движется слева направо, оставляя следы. Но почему-то
он выдаёт ошибку
'''
x = 0

def setup():
    size(600, 600)
    rectMode(CENTER)
    colorMode(HSB, 360, 100, 100)
    
def draw():
    global x
    
    for y in 150, 200, 250, 300, 350, 400, 450, 500:
        fill(random(360), 100, 100)
        rect(x, y, 25, 25)
    x += 5
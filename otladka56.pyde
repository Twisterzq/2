'''
Эта программа должна нарисовать мозаику — раскрасить в клеточку
весь холст, рисуя ряд за рядом квадратики. Но рисуется на холсте только первый
ряд. Как исправить это? 
'''
x = 0
y = 0

def setup():
    size(800, 600)
    strokeWeight(3)
    background(255)
    colorMode(HSB, 360, 100, 100)
    
def draw():   
    global x, y
    col = 0
    for x in range (0,800,20):
        for y in range (0,600,20):
            fill(random(360), 100, 100)
            rect (x,y,20,20)
    
        
    

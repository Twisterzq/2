"""
Круг должен из чёрного постепенно светлеть в синий цвет,
а когда он становится совсем ярким, он должен сбрасывася на чёрный.
Но почему-то яркость круга не нарастает, он всё время чёрный.
Как исправить это?
"""

brightness = 0
def setup():
    size(600,400)
    colorMode(HSB, 360,100,100)

def draw():
    global brightness
    background(50,100,100)
    fill(200, 100, brightness)
    circle(300, 200, 60)
    brightness = brightness + 1
    if brightness > 100:
        brightness = 0
    

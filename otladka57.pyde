'''
В этом проекте узор должен вращаться вокруг центра,
но почему-то этого не происходит. Как исправить это?
'''

angle = 0

def setup():
    size(600, 400)
    rectMode(CENTER)
    
def draw():
    global angle
    
    background(255)
    translate(300, 200)
    rotate(radians(angle))
    fill(0, 255, 0)
    ellipse(0, 0, 60, 60)
    fill(255, 255, 0)
    angle = angle + 1
    for i in range(8):
        rect(120, 0, 60, 60)
        rotate(radians(360/8))

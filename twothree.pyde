tx = 50
ty = 50
def setup ():
    size (700,200)
def draw ():
    background (50)
    global tx, ty
    rect (tx-10,ty+15,115,55)
    ellipse (tx,ty+75,35,35)
    ellipse (tx+35,ty+75,35,35)
    ellipse (tx+70,ty+75,35,35)
    ellipse (tx+105,ty+75,35,35)
    rect (tx+60,ty,70,20)
    ellipse (tx+60,ty+10,70,40)
    if keyPressed ==True:
        if key == "D" or key == "d" or key =="В" or key =="в":
            tx = tx + 1
        if key == "A" or key == "a" or key == "Ф" or key == "ф":
            tx = tx - 1
    

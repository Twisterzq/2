a = ["a","r","b","u","z"]
def setup ():
    size (500,100)
    background (0,0,255)
def draw ():
    line (100,0,100,100)
    line (200,0,200,100)
    line (300,0,300,100)
    line (400,0,400,100)
    line (500,0,500,100)
    fill (255,255,255)
    textSize (75)
    for i in range(len(a)):
        if keyPressed and key == "a" or key == "A":
            text (a[0],30,75)
        if keyPressed and key == "r" or key == "R":
            text (a[1],130,75)
        if keyPressed and key == "b" or key == "B":
            text (a[2],230,75)
        if keyPressed and key == "u" or key == "U":
            text (a[3],330,75)
        if keyPressed and key == "z" or key == "Z":
            text (a[4],430,75)

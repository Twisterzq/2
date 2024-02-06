shar_x = 50
shar_y = 50
shar_razmer = 50
def setup():
    size (600,300)
def draw():
    global shar_x, shar_y, shar_razmer
    rect (100,0,50,200)
    rect (250,100,50,200)
    rect (400,0,50,200)
    rect (500,250,5,50)
    rect(500,200,75,50)
    ellipse (shar_x,shar_y,shar_razmer,shar_razmer)
    if keyPressed:
        if key == 'W' or key == 'w' or key == 'Ц' or key == 'ц':
            shar_y = shar_y - 3
        if key == 'S' or key == 's' or key =='Ы' or key =='ы':
            shar_y = shar_y + 3
        if key == 'A' or key == 'a' or key == 'ф' or key == 'Ф':
            shar_x = shar_x - 3
        if key == 'D' or key == 'd' or key == 'В' or key == 'В': 
            shar_x = shar_x + 3

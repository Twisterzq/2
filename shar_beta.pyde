shar_x = 50
shar_y = 50
shar_razmer = 50 
collide = False
def collideRectCircle (ladder_x,ladder_y,ladder_weight,ladder_height,shar_x,shar_y,shar_razmer):
    Test_y = shar_y
    Test_x = shar_x
    if shar_x < ladder_x:
        Test_x = ladder_x
    if shar_x >ladder_x + ladder_weight:
        Test_x =ladder_x + ladder_weight
    if shar_y < ladder_y:
        Test_y = ladder_y
    if shar_y > ladder_y + ladder_height:
        shar_y = ladder_y + ladder_height
    distance = dist (shar_x,shar_y,Test_x,Test_y)
    if distance  <= shar_razmer/2:
        return True
    else:
        return False
def setup():
    size (600,300)
def draw():
    background (100)
    global shar_x, shar_y, shar_razmer, collide
    textMode (CENTER)
    textAlign (CENTER,CENTER)
    textSize(50)
    if shar_x >= 500 and shar_x <= 600 and shar_y >= 200 and shar_y <= 300:
        text(u"Победа",300,150)
        clear
    rect (100,0,50,200)
    rect (250,100,50,200)
    rect (400,0,50,200)
    rect (500,250,5,50)
    rect(500,200,75,50)
    ellipse (shar_x,shar_y,shar_razmer,shar_razmer)
    print (collide)
    if keyPressed:
        if key == 'W' or key == 'w' or key == 'Ц' or key == 'ц':
            shar_y = shar_y - 3
        if key == 'S' or key == 's' or key =='Ы' or key =='ы':
            shar_y = shar_y + 3
        if key == 'A' or key == 'a' or key == 'ф' or key == 'Ф':
            shar_x = shar_x - 3
        if key == 'D' or key == 'd' or key == 'В' or key == 'В': 
            shar_x = shar_x + 3 
    if collide:
        shar_y = shar_y + 5 if key in ['W', 'w', 'Ц', 'ц'] else shar_y
        shar_y = shar_y - 5 if key in ['S', 's', 'Ы', 'ы'] else shar_y
        shar_x = shar_x + 5 if key in ['A', 'a', 'ф', 'Ф'] else shar_x
        shar_x = shar_x - 5 if key in ['D', 'd', 'В', 'в'] else shar_x
    rect1_collide = collideRectCircle(100,0,50,200,shar_x,shar_y,shar_razmer)
    rect2_collide = collideRectCircle(250,100,50,200,shar_x,shar_y,shar_razmer)
    rect3_collide = collideRectCircle(400,0,50,200,shar_x,shar_y,shar_razmer)
    circle_edges_collide = shar_x < 0 or 600 < shar_x or shar_y < 0 or 300 < shar_y
    collide = rect1_collide or rect2_collide or rect3_collide or circle_edges_collide
    textAlign (CENTER,CENTER)
    textSize(50)
    if shar_x >= 500 and shar_x <= 600 and shar_y >= 200 and shar_y <= 300:
        text(u"Победа",300,150)
        clear
        

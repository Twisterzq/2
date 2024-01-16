'''
Это — лабиринт. Персонаж должен ходить по нажатию на стрелки.
Но почему-то не хочет. Как исправить это?
'''

x = 50
y = 50
def collideRectCircle(rx, ry, rw, rh, cx, cy, diameter):
  #2d
  # временные переменные для установки краёв для тестирования
  # rectmode — CORNER, ellipseMode — CENTER, то есть оба по-умолчанию
  testX = cx
  testY = cy

  # which edge is closest?
  if cx < rx:
    testX = rx       # Левый край
  elif cx > rx+rw:
    testX = rx+rw     # правый край

  if cy < ry:
    testY = ry       # верхний край
  elif cy > ry+rh:
    testY = ry+rh   # нижний край

  # получить расстояние от ближайших краев с помощью processing функции dist()
  distance = dist(cx,cy,testX,testY) 

  # если расстояние меньше радиуса, столкновение!
  if distance <= diameter/2:
    return True
  else:
    return False


def setup():
    size(600, 400)
    
def draw():
    global x, y, collide
    background(100)
    #Стены
    rect(100, 0, 50, 300)
    rect(250, 100, 50, 300)
    rect(400, 0, 50, 300)
    
    #Персонаж
    ellipse(x, y, 50, 50)
    
    #Флаг-финал
    rect(500, 350, 60, 40)
    push()
    strokeWeight(3)
    line(500, 390, 500, 400)
    pop()
    
    # Столкновение персонажа и флага-финала
    victory = collideRectCircle(500, 350, 60, 40, x, y, 50)
    
    if victory == True:
        textSize(14)
        fill(255,0,0)
        text(u"ПОБЕДА!", 200, 300)
        fill(255)
    
    
    
    
    
    
    # Дижение персонажа
    if keyPressed:
        if key == CODED:
            if keyCode == RIGHT:
                x = x + 5
                #Столкновение персонажа со стенами
                rect1_collide = collideRectCircle(100, 0, 50, 300,   x, y, 50) #прямоугольник1
                rect2_collide = collideRectCircle(250, 100, 50, 300,   x, y, 50) #прямоугольник2
                rect3_collide = collideRectCircle(400, 0, 50, 300,   x, y, 50) #прямоугольник3
                #Столкновение персонажа с краями
                circle_edges_collide =  x < 25 or 575 < x or y < 25 or 375 < y   
                # Есть ли хоть какое-то столкновение со стенами или краями?
                collide = rect1_collide or rect2_collide or rect3_collide or circle_edges_collide
                if collide:
                    x = x - 5
            elif keyCode == LEFT:
                x = x - 5
                #Столкновение персонажа со стенами
                rect1_collide = collideRectCircle(100, 0, 50, 300,   x, y, 50) #прямоугольник1
                rect2_collide = collideRectCircle(250, 100, 50, 300,   x, y, 50) #прямоугольник2
                rect3_collide = collideRectCircle(400, 0, 50, 300,   x, y, 50) #прямоугольник3
                #Столкновение персонажа с краями
                circle_edges_collide =  x < 25 or 575 < x or y < 25 or 375 < y   
                # Есть ли хоть какое-то столкновение со стенами или краями?
                collide = rect1_collide or rect2_collide or rect3_collide or circle_edges_collide
                if collide:
                    x = x + 5
            elif keyCode == UP:
                y = y - 5
                #Столкновение персонажа со стенами
                rect1_collide = collideRectCircle(100, 0, 50, 300,   x, y, 50) #прямоугольник1
                rect2_collide = collideRectCircle(250, 100, 50, 300,   x, y, 50) #прямоугольник2
                rect3_collide = collideRectCircle(400, 0, 50, 300,   x, y, 50) #прямоугольник3
                #Столкновение персонажа с краями
                circle_edges_collide =  x < 25 or 575 < x or y < 25 or 375 < y   
                # Есть ли хоть какое-то столкновение со стенами или краями?
                collide = rect1_collide or rect2_collide or rect3_collide or circle_edges_collide
                if collide:
                    y = y + 5
            elif keyCode == DOWN:
                y = y + 5
                #Столкновение персонажа со стенами
                rect1_collide = collideRectCircle(100, 0, 50, 300,   x, y, 50) #прямоугольник1
                rect2_collide = collideRectCircle(250, 100, 50, 300,   x, y, 50) #прямоугольник2
                rect3_collide = collideRectCircle(400, 0, 50, 300,   x, y, 50) #прямоугольник3
                #Столкновение персонажа с краями
                circle_edges_collide =  x < 25 or 575 < x or y < 25 or 375 < y   
                # Есть ли хоть какое-то столкновение со стенами или краями?
                collide = rect1_collide or rect2_collide or rect3_collide or circle_edges_collide
                if collide:
                    y = y - 5
        
    
    

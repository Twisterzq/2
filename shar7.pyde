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


shar_x = 400
shar_y = 300
shar_dx = 3
shar_dy = -3
shar_razmer = 40
ladder_x = 250
ladder_y = 590
ladder_width = 70
ladder_height = 30
score = 0

def setup():
    size(600,600)
    rectMode(CENTER)
    
def draw():
    global shar, ladder, game, vkl, shar_x, shar_y, ladder_x, ladder_x, shar_dx, shar_dy, score
    background(100)
    
    ellipse(shar_x, shar_y, shar_razmer, shar_razmer)
    rect(ladder_x, ladder_y, ladder_width, ladder_height)
    text(score, 570, 20)
    shar_x = shar_x + shar_dx
    shar_y = shar_y + shar_dy
    
    if shar_x > 580:
        shar_dx = -shar_dx
    if shar_x < 20:
        shar_dx = -shar_dx
        
    if shar_y < 20:
        shar_dy = -shar_dy
    #касание шаром ракетки
    if collideRectCircle(ladder_x, ladder_y, ladder_width, ladder_height,   shar_x, shar_y, shar_razmer):
        score += 1
        shar_dy = -random(4,6)
        shar_dx = random(-5, 5)
    
    #Проигрыш
    if shar_y > 650:
        textSize(50)
        textAlign(CENTER, CENTER)
        text(u'Проигрыш',300,300)
    
        
    if keyPressed and key == CODED:
        if keyCode == LEFT:
            ladder_x = ladder_x - 4
        if keyCode == RIGHT:
            ladder_x = ladder_x + 4
    
        
            
            

x = [20,40,60,80,100,120,140,160,180,190,100,120,50,150,120]
y = [20,23,14,55,34,22,44,41,10,15,-15,0,-30,-10,-50]
s = [1.1,1.15,1.2,1.1,1,1.4,1.2,1.5,1.32,1.6,1,1.4,1.2,1.4,1.2]
def setup ():
    size (200,150)
    stroke(255)
    strokeWeight(4)
def draw ():
    frameRate (60)
    background (100)
    for i in range(len(x)):    
        point(x[i],y[i])
        y[i] += s[i]
        if y[i]>150:
            y[i] -= 150

class point:
    def __init__(self,a,b):
    self.x = a
    self.y = b


def absis(p):
    return p.x

def ordinat(p):
    return p.y

def makeG(x,y):
    return point(x,y)

def gradien(p1,y1):
    return (ordinat(p2)-ordinat(p1))/(absis(p2)-absis(p1))

def issejajar(g1,g2,g3,g4):
    if gradien(g1,g2)==gradien(g3,g4):
        return bool

def istegaklurus(g1,g2,g3,g4):
    if gradien(g1,g2)*gradien(g3,g4) == -1 :
        return bool

print(gradien(makeG(2,4),makeG(5,7)))
print(gradien(makeG(2,2),makeG(8,3)))
print(bool(issejajar(makeG(2,4),makeG(5,7),makeG(2,2).makeG(8,3))))
print(bool(istegaklurus(makeG(2,4),makeG(5,7),makeG(2,2).makeG(8,3))))

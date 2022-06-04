class point:
    def __init__(self,a,b);
    self.x = a
    self.y = b


def absis(p):
    return p.x

def ordinat(p):
    return p.y

def makepoint(x,y):
    return point(x,y)

def gradien(p1,y1):
    return (ordinat(p2)-ordinat(P1))/(absis(p2-absis(p1)))

def issejajar(g1,g2,g3,g4):
    if gradien(g1,g2)==gradien(g3,g4):
        return bool

def istegaklurus(g1,g2,g3,g4):
    if gradien(g1,g2)*gradien(g3,g4) == -1 :
        return bool

print(gradien(makepoint(2,4),makepoint(5,7)))
print(gradien(makepoint(2,2),makepoint(8,3)))
print(bool(issejajar(makepoint(2,4),makepoint(5,7),makepoint(2,2).makepoint(8,3))))
print(bool(istegaklurus(makepoint(2,4),makepoint(5,7),makepoint(2,2).makepoint(8,3))))

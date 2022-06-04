class point1:
    def __init__(self,a,b):
        self.x1 = a
        self.y1 = b

class point2:
    def __init__(self,c,d):
        self.x2 = c
        self.y2 = d
# SELEKTOR
def absis1(p1):
    return p1.x1

def ordinat1(p1):
    return p1.y1

def absis2(p2):
    return p2.x2

def ordinat2(p2):
    return p2.y2

# KONSTRUKTOR
def makepoint1(p1):
    return (absis1(p1),ordinat1(p1))

def makepoint2(p2):
    return (absis2(p2),ordinat2(p2))

n1 = point1(-9.9,9.9)
n2 = point2(-2.2,2.2)

print(makepoint1(n1))
print(makepoint2(n2))

# OPERATOR
def GradienG1(g1,g2):
    return (ordinat2(g2)-ordinat1(g1)/ absis2(g2)-absis1(g1))



def GradienG2(g3,g4):
    return (ordinat2(g4)-ordinat1(g3)/ absis2(g4)-absis1(g3))



def is_sejajar(G1,G2,G3,G4):
    if GradienG1(G1,G2) == GradienG2(G3,G4):
        return True
    else :
        return False
    
def is_tegaklurus(G1,G2,G3,G4):
    if GradienG1(G1,G2) * GradienG2(G3,G4) == -1 :
        return True
    else :
        return False

p1 = point1(2,4)
p2 = point2(5,7)
p3 = point1(2,2)
p4 = point2(8,3)
print(GradienG1(p1,p2))
print(GradienG2(p1,p2))
print(is_sejajar(p1,p2,p3,p4))
print(is_tegaklurus(p1,p2,p3,p4))


class point:
    def __init__(self,a,b):
        self.x = a
        self.y = b

# SELEKTOR
def absis(p):
    return p.x

def ordinat(p):
    return p.y



# KONSTRUKTOR
def makepoint(p):
    return (absis(p),ordinat(p))


# OPERATOR
def GradienG(g1,g2):
    return (ordinat(g2)-ordinat(g1) / absis(g2)-absis(g1))

def is_sejajar(G1,G2,G3,G4):
    if GradienG(G1,G2) == GradienG(G1,G2):
        return True
    else :
        return False
    
def is_tegaklurus(G1,G2,G3,G4):
    if GradienG(G1,G2) * GradienG(G1,G2) == -1 :
        return True
    else :
        return False

g1 = point(2,4)
g2 = point(5,7)
g3 = point(2,2)
g4 = point(8,3)
print(GradienG(g1,g2))
print(is_sejajar(g1,g2,g3,g4))
print(is_tegaklurus(g1,g2,g3,g4))


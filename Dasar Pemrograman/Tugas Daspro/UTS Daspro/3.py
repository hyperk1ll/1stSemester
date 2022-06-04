class point:
    def __init__(self,a,b):
        self.x = a
        self.y = b

# SELEKTOR
def absis(p):
    return p.x

def ordinat(p):
    return p.y

def top(T):
    return 

def bottom(T):
    return 


# KONSTRUKTOR
def makepoint(a,b):
    return (absis(p),ordinat(p))

def makesquare(h,i):
    return 


# OPERATOR

def GetPanjang(S):
    return top(absis(S) - bottom(ordinat(S)))

def GetLebar(S):
    return top(ordinat(S) - bottom(absis(S)))
    
def GetLuas(S):
    return GetPanjang(S) * GetLebar(S)

absis = point(1,2)
ordinat = point(1,2)

print(GetPanjang(absis(S)))
print(GetLebar(S))
print(GetLuas(S))

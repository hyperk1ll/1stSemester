# KONSTRUKTOR
class pecahancampuran:
    def __init__(self,bil,n,d):
        self.bil = bil
        self.n = n
        self.d = d

# SELEKTOR
def Bil(P):
    return P.bil

def PembC(P):
    return P.n

def PenyC(P):
    return P.d

# PREDIKAT
def RealPC(P):
    if Bil(P) >=0:
        return Bil(P) + (PembC(P) / PenyC(P))
    else:
        return Bil(P) - (PembC(P) / PenyC(P))


print(RealPC(pecahancampuran(-2,1,2)))
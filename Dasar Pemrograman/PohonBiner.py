class PohonBiner:
    def __init__(self,A,L,R):
        self.A = A
        self.L = L
        self.R = R
    
    def insert_urut(self,a):
        if(self,A):
            if a < self.A:
                if self.L is None:
                    self.L = PohonBiner(a,None,None)
                else:
                    self.L.insert_urut(a)
            elif a > self.A:
                if self.R is None:
                    self.R


def BSearchX(P,a):
    if(Akar(P) == a):
        return True
    elif(IsTreeEmpty(P)):
        return False
    else:
        if(IsOneElmtPB(P)):
            if(Akar(P) == a):
                return True
            else:
                return False
        else:
            if(Akar(P) < a):
                return BSearchX(Right(P),a)
            else:
                return BSearchX(Left(P),a)


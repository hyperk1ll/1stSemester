def FirstElmt(L):
    return L[0]

def Tail(L):
    if not (IsEmpty(L)):
        return L[1:]

def LastElmt(L):
    return L[-1]

def Head(L):
    if not (IsEmpty(L)):
        return L[:-1]

def IsEmpty(L):
    return L == []

def NbElmt(L):
    if L == []:
        return 0
    else:
        return 1 + NbElmt(Tail(L))

def IsInverse(L1,L2):
    if (NbElmt(L1) == NbElmt(L2)):
        if (IsEmpty(L1) and IsEmpty(L2)):
            return True
        else:
            return FirstElmt(L1) == LastElmt(L2) and IsInverse(Head(L1), Tail(L2))
    else:
        return False

# APLIKASI
L1 = [1,2,3,4,5]
L2 = [5,4,3,2,1]
print(IsInverse(L1,L2))
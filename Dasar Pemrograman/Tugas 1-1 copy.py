
# KONSTRUKTOR
def konso(S,L):
    if L == []:
        return [S]
    else:
        return [S] + L

def konsi(S,L):
    if L == []:
        return [S]
    else:
        return L + [S]

# SELEKTOR
def FirstElmt(L):
    return L[0]

def Tail(L):
    if not (IsEmpty(L)):
        return L[1:]

def LastElmt(L):
    return L[-1]

def prec(n):
    return n - 1

def Head(L):
    if not (IsEmpty(L)):
        return L[0:]

# PREDIKAT
def IsEmpty(L):
    return L == []

def IsMember(X,L):
    if IsEmpty(L):
        return False
    else:
        if LastElmt(L) == X:
            return True
        else:
            return IsMember(Head(L),X)

# FUNGSI LAIN
def NbElmt(L):
    if L == []:
        return 0
    else:
        return 1 + NbElmt(Tail(L))

def ElmtKeN(N,L):
    if N == 1:
        return FirstElmt(L)
    else:
        return ElmtKeN(N-1, Tail(L))

def IsXElmtKeN1(X,N,L):
    if ElmtKeN(N,L) == X:
        return True
    else:
        return False

def IsXElmtKeN2(X,N,L):
    if IsMember(X,L):
        if N == 1 and FirstElmt(L) == X:
            return True
        elif N == 1 and FirstElmt(L) != X:
            return False
        else:
            return IsXElmtKeN2(X,N-1,Tail(L))
    else:
        return False

def IsInverse(L1,L2):
    if (NbElmt(L1) == NbElmt(L2)):
        if (IsEmpty(L2) and IsEmpty(L2)):
            return True
        else:
            return FirstElmt(L1) == LastElmt(L2) and IsInverse(Head(L1),Tail(L2))
    else:
        return False

L1 = ['1','2','3','4','5']
L2 = ['5','4','3','2','1']
X = ['2']
print(ElmtKeN(3,L1))
print(IsXElmtKeN1(X,2,L1))

print(IsInverse(L1,L2))
def prec(n):
    return n - 1

def FirstElmt(L):
    if not(IsEmpty(L)):
        return L[0]

def Tail(L):
    if not (IsEmpty(L)):
        return L[1:]

def IsEmpty(L):
    return L == []

def ElmtKeN(N,L):
    if N == 1:
        return FirstElmt(L)
    else:
        return ElmtKeN(N-1, Tail(L))

def IsXElmtKeN(X,N,L):
    if ElmtKeN(N,L) == X:
        return True
    else:
        return False

L1 = [1,2,3.4,5]

print(IsXElmtKeN(2,2,L1))
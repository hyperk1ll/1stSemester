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

L1 = [2,3,4,5,6]
print(ElmtKeN(3,L1))
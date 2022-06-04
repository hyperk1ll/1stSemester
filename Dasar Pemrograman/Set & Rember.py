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

def IsMember(x,L):
    if IsEmpty(L):
        return False
    else:
        if LastElmt(L) == x:
            return True
        else:
            return IsMember(Head(L),x)

def MakeSet(L):
    if IsEmpty(L):
        return L
    else:
        if IsMember(Tail(L), FirstElmt(L)):
            return MakeSet(Tail(L))
        else:
            return konso(FirstElmt(L), MakeSet(Tail(L)))

def MultiRember(x,L):
    if IsEmpty(L):
        return L
    else:
        if FirstElmt(L) == x:
            return MultiRember(x,Tail(L))
        else:
            return konso(FirstElmt(L), MultiRember(x, Tail(L)))

def IsSet(L):
    if IsEmpty(L):
        return True
    else:
        if IsMember(Tail(L), FirstElmt(L)):
            return False
        else:
            return IsSet(Tail(L))

def IsSubset(H1,H2):
    if IsEmpty(H1):
        return True
    else:
        if not(IsMember(H2, FirstElmt(H1))):
            return False
        else:
            return IsSubset(Tail(H1), H2)

def IsEQSet(H1,H2):
    return IsSubset(H1,H2) and IsSubset(H2,H1)


L1 = ['3','3','a','4']
L3 = ['9','p','9','9','p','a']

H1 = ['2','3']
H2 = ['a','b','3','2','1']

print(MakeSet(L1))
print(MultiRember('3',L1)) 
print(IsSet(L1))
print(IsSubset(H1,H2))
print(IsEQSet(H1,H2))
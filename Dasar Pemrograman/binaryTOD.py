def is_empty(S):
    return S == []

def first(S):
    return S[0]

def tail(S):
    return S[1:]

def nb_element(L):
    if is_empty(L):
        return 0
    else:
        return 1 + nb_element(tail(L))

def isOne(L):
    if L == 0:
        return False
    elif nb_element(L)==1:
        return True
    else:
        False

def is_list(S):
    if type(S) == list:
        return True
    else:
        return False

#====================================================================
def makePB(root, left, right):
    return [root, left, right]

def root(P):
    return P[0]

def left(P):
    return P[1]

def right(P):
    return P[2]

def istreeEmpty(P):
    if P == None:
        return True
    else:
        return False

def isOneElmt(P):
    if not istreeEmpty(P) and istreeEmpty(left(P)) and istreeEmpty(right(P)):
        return True
    else:
        return False
    
def isUnerLeft(P):
    if not istreeEmpty(P) and not istreeEmpty(left(P)) and istreeEmpty(right(P)):
        return True
    else:
        return False

def isUnerRight(P):
    if not istreeEmpty(P) and istreeEmpty(left(P)) and not istreeEmpty(right(P)):
        return True
    else:
        return False

def isbiner(P):
    if not istreeEmpty(P) and not istreeEmpty(left(P)) and not istreeEmpty(right(P)):
        return True
    else: 
        return False

def isExistLeft(P):
    if not istreeEmpty(P) and not istreeEmpty(left(P)):
        return True
    else:
        return False

def isExistRight(P):
    if not istreeEmpty(P) and not istreeEmpty(right(P)):
        return True
    else:
        return False

def NbElmt(P):
    if istreeEmpty(P):
        return 0
    elif isOneElmt(P):
        return 1 
    else:
        if isbiner(P):
            return NbElmt(left(P)) + 1 + NbElmt(right(P))
        elif isUnerLeft(P):
            return NbElmt(left(P)) + 1
        elif isUnerRight(P):
            return NbElmt(right(P)) +1
        else:
            return 0

def repPrefix(P):
    if isOneElmt(P):
        return [root(P)]
    else:
        if isbiner(P):
            return [root(P)] + [repPrefix(left(P))] + [repPrefix(right(P))]
        elif isUnerLeft(P):
            return [root(P)] + [repPrefix(left(P))]
        elif isUnerRight(P):
            return [root(P)] + [repPrefix(right(P))]

def NbDaun(P):
    if istreeEmpty(P):
        return 0
    elif isOneElmt(P):
        return 1
    else:
        if isbiner(P):
            return NbDaun(left(P)) + NbDaun(right(P))
        elif isUnerLeft(P):
            return NbDaun(left(P))
        elif isUnerRight(P):
            return NbDaun(right(P))
        else:
            return 0

# BSearch : binSearchTree, element --> boolean
# {BSearch(P,x) mengirimkan true jika ada node dari pohon binary search tree P yang bernilai X, mengirimkan false jika tidak ada}
def BSearch(P,x):
    if istreeEmpty(P):
        return False 
    else:
        if root(P) == x:
            return True
        elif root(P) > x:
            return BSearch(left(P),x)
        else:
            return BSearch(right(P),x)

# AddX(P,x) : binSearchTree, elemen --> pohonbiner
# {AddX (P,x) menghasilkan sebuah ppohon binary search tree P dengan tambahan simpul X, belum ada simpul P yang bernilai X}    
def AddX(P,x):
    if istreeEmpty(P):
        return makePB(x, None, None)
    elif P == []:
        return makePB(x, None, None)
    elif x == None:
        return P
    elif x > root(P):
        return makePB(root(P), (left(P)), AddX(right(P),x))
    else:
        return makePB(root(P), AddX(left(P),x), (right(P)))


def binSearchtree(L,P):
    if is_empty(L):
        return P
    else:
        return binSearchtree(tail(L), AddX(P, first(L)))

# makebintree : list of element --> pohon biner
# {makebintree(L) menghasilkan sebuah pohon binary search tree P yang elemennya berasal dari elemen list L yang dijamin unik }
def makebintree(L):
    return binSearchtree(L, [])

# delBtree : binsearchtree tidak kosong, elemen --> pohon biner
# {delBtree(P,x) menghasilkan sebuah pohon binary search tree p tanpa node yang bernilai x, x pasti ada sebagai salah satu node, tree menghasilkan tree kosong jika p hanya terdiri dari x}        
def delBtree(P,x):
    if istreeEmpty(P):
        return P
    elif not BSearch(P,x):
        return P
    else:
        if isExistLeft(P) and BSearch(left(P),x):
            return makePB(root(P),delBtree(left(P),x), (right(P)))
        elif isExistRight(P) and BSearch(right(P),x):
            return makePB(root(P), (left(P)), delBtree(right(P),x))

# makeBaltree : list of node, integer --> binBaltree
# {menghasilkan sebuah balace tree dengan n node, nilai setiap node yang berasal dari list}
def BuildBalanceTree(L):
    L =sorted(L)
    if is_empty(L):
        return L
    else:
        mid =(len(L))//2
        root=L[mid]
        left=BuildBalanceTree(L[:mid])
        right=BuildBalanceTree(L[mid+1:])    
        return makePB(root,left,right)

p0 = makePB(
    2,
    None,
    None
)
p1 = makePB(
    5,
    makePB(3, makePB(2,None,None), makePB(4, None, None)),
    makePB(7, makePB(6, None, None), makePB(8,None,None))
)

L1 = [5,3,7,2,6,9]
L2 = [5,3,7,2,6,9,10,54,24,13]


print('\n====isBiner====')
print(isbiner(p1))

print('\n====repPrefix====')
print(repPrefix(p1))

print('\n====BSearch====')
print(BSearch(p1,4))

print('\n====AddX====')
print(AddX(p1,16))

print('\n====makebintree====')
print(makebintree(L1))

print('\n====delBtree====')
print(delBtree(p1,7))

print('\n====BuildBalanceTree====')
print(BuildBalanceTree(L2))
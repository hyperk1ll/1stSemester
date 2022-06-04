L1 = [9, 2, 5, 1, 4, -3, 10, -9, 1]

def FirstElmt(L):
    return L[0]

def IsEmpty(L):
    return L == []

def IsOneElmt(L):
	if((not IsEmpty(L)) and (IsEmpty(Tail(L)))):
		return True
	else:
		return False

def Tail(L):
    if not (IsEmpty(L)):
        return L[1:]

def max2(a,b):
    if (a > b):
        return a
    else:
        return b

def min2(a,b):
    if (a < b):
        return a
    else:
        return b



print(FirstElmt(L1))
print(IsEmpty(L1))
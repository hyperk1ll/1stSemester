# Nama      : Muhammad Hilmy Tsany
# NIM       : 24060120140171
# Tanggal   : 14 Desember 2020
# Deskripsi : Latihan UAS (Coba Soal UAS Tahun 2019/2020)
# Nomor 3

# DefSpek
#

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

def BST(P):
    if IsOneElmt(P) == 7:
        return True
    else:
        return False

tree = [8,3,1,6,4,10,14,13]

print(BST(tree))
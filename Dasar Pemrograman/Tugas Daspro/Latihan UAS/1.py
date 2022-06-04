# Nama      : Muhammad Hilmy Tsany
# NIM       : 24060120140171
# Tanggal   : 14 Desember 2020
# Deskripsi : Latihan UAS (Coba Soal UAS Tahun 2019/2020)
# Nomor 1

#DefSpek
#IsEmpty : list --> boolean
#IsEmpty(L) bernilai benar jika list kosong

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


# DefSpek
# max2 : 2 integer --> integer
# max2(a,b) menentukan bilangan hasil maksimum dari 2 bilangan integer

def max2(a,b):
    if (a > b):
        return a
    else:
        return b

# DefSpek
# min2 : 2 integer --> integer
# min2(a,b) menentukan bilangan hasil minimum dari 2 bilangan integer

def min2(a,b):
    if (a < b):
        return a
    else:
        return b

# DefSpek
# min_list : list --> integer
# min_list menentukan bilangan minimum dari sebuah list

def min_list(L):
    if(IsEmpty(L)):
        return 0
    elif(IsOneElmt(L)):
        return FirstElmt(L)
    else:
        return min2(FirstElmt(L), min_list(Tail(L)))

# DefSpek
# max_list : list --> integer
# max_list(L) menentukan bilangan maksimum dari sebuah list

def max_list(L):
    if(IsEmpty(L)):
        return 0
    elif(IsOneElmt(L)):
        return FirstElmt(L)
    else:
        return max2(FirstElmt(L), max_list(Tail(L))
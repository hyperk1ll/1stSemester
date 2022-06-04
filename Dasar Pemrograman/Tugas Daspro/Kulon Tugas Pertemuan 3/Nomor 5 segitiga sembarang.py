# Segitiga sembarang                  IsSembarang(a,b,c)

# definisi dan spesifikasi
#IsSembarang: integer --> integer
# {IsSembarang(a,b,c) adalah 3 buah nilai panjang sisi segitiga}

# Realisasi
def IsSembarang(a,b,c):
    return(a != b != c != a)

# Aplikasi
print(IsSembarang(4,3,2))

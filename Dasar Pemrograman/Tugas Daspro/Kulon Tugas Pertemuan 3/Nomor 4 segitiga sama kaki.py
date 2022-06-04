# Segitiga sama kaki                  IsSama_kaki(a,b,c)

# definisi dan spesifikasi
#IsSama_kaki: integer --> integer
# {IsSama_kaki(a,b,c) adalah 3 buah nilai panjang sisi segitiga}

# Realisasi
def IsSama_kaki(a,b,c):
    return(a==b and b!=c) or (a==c and c!=b) or (b==c and c!=a)

# Aplikasi
print(IsSama_kaki(4,3,4))

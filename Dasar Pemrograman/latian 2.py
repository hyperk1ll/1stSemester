# Nama file: pangkat2.py
# pembuat: Hilmy Tsany
# tanggal: 21 September 2020
# Deskripsi: Aaaa

# Definisi dan Spesifikasi
# max3 : 3 integer --> integer
#   max3(a,b,c) menentukan nilai maksimum dari 3 bilangan integer

# Realisasi
def max2(a,b):
    return((a,b) + abs(a-b)) // 2

def max3(a,b,c):
    return max2(max2(a,b),c)

# Aplikasi

print(max2(3,9))
print(max3(3,33,333))

# Nama file: pangkat2.py
# pembuat: Hilmy Tsany
# tanggal: 21 September 2020
# Deskripsi: Aaaa

# Definisi dan Spesifikasi
# fx2 : integer --> integer
# ...

# Realisasi
def fx2(x):
    return x*x

def fx3v2(x):
    return x*fx2(x)
          
# Aplikasi
print (fx3v2(2))
print (fx3v2(3))
print (fx3v2(-2))

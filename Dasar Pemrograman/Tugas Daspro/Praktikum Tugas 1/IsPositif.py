# Nama file: IsPositif.py
# pembuat: Muhammad Hilmy Tsany
# tanggal: 21 September 2020
# Deskripsi: membuat definisi, spesifikasi, dan realisasi dari sebuah predikat yang menerima sebuah bilangan buat dan bernilai benar jika bilangan tersebut positif untuk menghasilkan sebuah nilai boolean yang bernilai true jika bilangan tersebut positif, atau false jika bilangan tersebut negatif

# Definisi dan spesifikasi dari fungsi positif bernama IsPositif?(x) adalah:
# IsPositif : integer --> boolean
#   IsPositif(x) benar jika x positif

# Realisasi
def IsPositif (x):
    return x == 0 or x > 0

# Aplikasi

# IsPositif (1)
# IsPositif (0)
# IsPositif (-1)

print (IsPositif (1))
print (IsPositif (0))
print (IsPositif (-1))

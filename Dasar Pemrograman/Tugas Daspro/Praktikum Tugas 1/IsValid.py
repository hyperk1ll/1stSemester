# Nama file: IsValid.py
# pembuat: Muhammad Hilmy Tsany
# tanggal: 21 September 2020
# Deskripsi: membuat definisi, spesifikasi, dan realisasi dari sebuah predikat yang menerima sebuah besaran integer, dan menentukan apakah bilangan tersebut valid. Bilangan disebut valid jika nilainya lebih kecil dari 5 atau lebih besar dari 500. Jadi bilangan diantara 5 dan 500 tidak valid

# Definisi dan spesifikasi dari fungsi Apakah valid bernama IsValid?(x) adalah:
# IsValid : integer --> boolean
#   IsValid(x) benar jika x positif bernilai lebih kecil dari 5 atau lebih besar dari 500 

# Realisasi
def IsValid (x):
    return x < 5 or x > 500

# Aplikasi

# IsValid (8)
# IsValid (0)
# IsValid (501)
# IsValid (6000)

print (IsValid (8))
print (IsValid (0))
print (IsValid (501))
print (IsValid (6000))

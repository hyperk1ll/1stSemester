# Nama file: Least Square (Jarak 2 Titik)
# pembuat: Muhammad Hilmy Tsany
# tanggal: 21 September 2020
# Deskripsi: menghasilkan sebuah bilangan riil yang merupakan jarak dari kedua titik tersebut (atau panjang garis yang dibentuk oleh kedua titik tersebut)

# Definisi dan spesifikasi dari fungsi Least Square bernama LS(x1,x2,y1,y2) adalah:
# LS : 4 real --> real
#   LS(x1,x2,y1,y2) adalah jarak antara dua buah titik x1,x2 dengan y1,y2

# Definisi dan spesifikasi fungsi antara
# dif2 : 2 real --> real
#   dif(x,y) adalah kuadrat dari selisih antara x dan y
# FX2 : real --> real
#   FX2(x) adalah hasil kuadrat dari x

# Realisasi
import math
def FX2(x) :
    return (x*x)
def dif2(x,y):
    return (FX2(x - y))
def LS(x1,x2,y1,y2):
    return (math.sqrt(dif2(y2,y1) + dif2(x2,x1)))

# Aplikasi

print (LS(1,3,5,6))




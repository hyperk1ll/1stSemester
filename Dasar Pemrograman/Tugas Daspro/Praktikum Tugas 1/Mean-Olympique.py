# Nama file: Mean-Olympique.py
# pembuat: Muhammad Hilmy Tsany
# tanggal: 21 September 2020
# Deskripsi: menghitung rata-rata dari dua buah bilangan integer yang bukan maksimum dan bukan minimum dari 4 buah integer: ((u+v+w+x) - min4(u,v,w,x))

# Definisi dan Spesifikasi dari fungsi Mean-Olympique bernama MO(u,v,w,x) adalah:
#max4 : 4 integer>0 --> integer
#  max4(i,j,k,l) menentukan maksimum dari 4 bilangan integer i, j, k, dan l, menggunakan fungsi antara max2(a,b)

#min4 : 4 integer>0 --> integer
#  min4(i,j,k,l) menentukan minimum dari 4 bilangan integer i, j, k, dan l, menggunakan fungsi antara min2(a,b)

#max2 : 2 integer>0 --> integer
#  max2(a,b) menentukan maksimum dari 2 bilangan integer a dan b, hanya dengan ekspresi aritmatika: jumlah kedua bilangan ditambah dengan selisih kedua bilangan, hasilnya dibagi 2

#min2 : 2 integer>0 --> integer
#  min2(a,b) menentukan minimum dari 2 bilangan integer a dan b, hanya dengan ekspresi aritmatika: jumlah dari kedua bilangan dikurangi selisih kedua bilangan, hasilnya dibagi 2

# Realisasi
def max2(a,b):
    return ((a+b) + abs(a-b))/2
def min2(a,b):
    return ((a+b) - abs(a-b))/2
def max4(i,j,k,l):
    return (max2(max2(i,j),max2(k,l)))
def min4(i,j,k,l):
    return (min2(min2(i,j),min2(k,l)))

def MO(u,v,w,x):
    return ((u+v+w+x) - min4(u,v,w,x))/2

# Aplikasi
print (MO(8,12,10,20))

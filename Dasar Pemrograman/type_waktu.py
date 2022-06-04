# Nama file: type_waktu.py
# Pembuat: Muhammad Hilmy Tsany
# Tanggal: 10 Oktober 2020
# Deskripsi: mendefinisikan suatu type bernama waktu, yang terdiri dari <j,m,d> dengan j adalah jam, m adalah menit dan d adalah detik.

# Definisi dan spesifikasi type:
# type_time : <j:integer[0...23], m:integer[0...59], d:integer[0...59]
#   <j,m,d> dimana j = jam, m = menit, d = detik
    
# Definisi dan spesifikasi selektor dengan fungsi
# Hour : time --> integer[0...23]
#   Hour(T) memberikan nilai jam dari suatu time
# Minute : time --> integer[0...59]
#   Minute(T) memberikan nilai menit dari suatu time
# Second : time --> integer[0...59]
#   Second(T) memberikan nilai detik dari suatu time

# Definisi dan spesifikasi konstruktor 
# MakeTime : integer[0...23], integer[0...59], integer[0...59] --> time
#   MakeTime(a,b,c) membentuk tme dengan jam a, menit b, detik c dengan a,b,c integer

# Definisi dan spesifikasi predikat
# IsBefore : 2 time --> boolean
#   IsBefore(T1,T2) benar jika T1 adalah sebelum T2
# IsAfter : 2 time --> boolean
#   IsAfter(T1,T2) benar jika T1 adalah sesudah T2

# Definisi dan spesifikasi operator
# DetikToTime : integer>0 --> time
#   DetikToTime(P) mengkonversi detik(c) menjadi sebuah time
#   Jika hasil konversi lebih dari 24 jam, dikembalikan sisa waktu setelah 24 jam
# JumlahDetik : time --> integer
#   JumlahDetik(T) menghitung jumlah detik dari suatu time
# AddTime : 2 time --> time
#   AddTime(T1,T2) menjumlahkan 2 buah time menghasilkan sebuah time
# AddTimeSecond : time, integer --> time
#   AddTimeSecond(T,N) menambahkan time dengan detik(N) menghasilkan time
#   Jika hasil melebihi 24 jam, dikembalikan sisa waktunya
#   Contoh : AddTimeSecond(<23,0,0>,4000) hasilnya melebihi 24 jam, sehingga dikembaikan sisanya <0,6,40>

class Time:
    def __init__(self,x,y,z):
        self.j = x
        self.m = y
        self.d = z

# SELEKTOR
def Hour(T):
    return T.j

def Minute(T):
    return T.m

def Second(T):
    return T.d

# KONSTRUKTOR
def MakeTime(a,b,c):
    return (a,b,c)

# PREDIKAT
def IsBefore(T1,T2):
    return JumlahDetik(T1) < JumlahDetik(T2)

def IsAfter(T1,T2):
    return JumlahDetik(T1) > JumlahDetik(T2)

# OPERATOR
def DetikToTime(P) :
    if (P > 86400) :
        r = ((P-86400) // 3600)
        s = ((P-86400)-(r*3600)) // 60
        t = (P-86400)-(r*3600) - (s*60)
        return (MakeTime(r,s,t))
                
    else :
        r = P // 3600
        s = (P-(r*3600))//60
        t = (P-(r*3600)-(s*60))
        return (MakeTime(r,s,t))

def JumlahDetik(T):
    return (Hour(T)*3600) + (Minute(T)*60) + (Second(T))

def AddTime(T1,T2):
    return DetikToTime(JumlahDetik(T1) + JumlahDetik(T2))

def AddTimeSecond(T,N):
    return DetikToTime(JumlahDetik(T)+N)



T1=Time(10,30,0)
T2=Time(11,24,1)

print(IsBefore(T1,T2))
print(IsAfter(T1,T2))
print(DetikToTime(86500))
print(JumlahDetik(T1))
print(AddTime(T1,T2))
print(AddTimeSecond(T1,4000))


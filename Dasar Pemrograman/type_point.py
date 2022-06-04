# Nama file: type_point.py
# Pembuat: Muhammad Hilmy Tsany
# Tanggal: 10 Oktober 2020
# Deskripsi: mendefinisikan suatu type bernama point yang terdiri dari absis dan ordinat 

# Definisi dan spesifikasi type:
# type_point : <x : real, y : real>
#   <x,y> adalah sebuah point, dengan x adalah absis, y adalah ordinat
    
# Definisi dan spesifikasi selektor dengan fungsi
# absis : point --> real
#   absis(p) memberikan absis point p
# ordinat : point --> real
#   ordinat(p) memberikan ordinat point p

# Definisi dan spesifikasi konstruktor 
# makepoint : 2 real --> point
#   makepoint(x,y) membentuk sebuah point dari x dan y dengan x sebagai absis dan y sebagai ordinat

# Definisi dan spesifikasi operator
# Gradien : 2 point --> real
#   Gradien(G) mengkonversi detik(c) menjadi sebuah time
# is_sejajar : 4 point --> boolean
#   is_sejajar(G1,G2,G3,G4) benar jika gradien (G1,G2) sejajar dengan gradien (G3,G4)
# is_tegaklurus : 4 point --> boolean
#   is_tegaklurus(G1,G2,G3,G4) benar jika gradien (G1,G2) tegak lurus dengan (G3,G4)

class point:
    def __init__(self,a,b):
        self.x = a
        self.y = b

# SELEKTOR
def absis(p):
    return p.x

def ordinat(p):
    return p.y


# KONSTRUKTOR
def makepoint(x,y):
    return point(x,y)


# OPERATOR
def Gradien(p1,p2):
    return (ordinat(p2)-ordinat(p1) / absis(p2)-absis(p1))


def is_sejajar(G1,G2,G3,G4):
    if Gradien(G1,G2) == Gradien(G3,G4):
        return True
    else :
        return False
    
def is_tegaklurus(G1,G2,G3,G4):
    if Gradien(G1,G2) * Gradien(G3,G4) == -1 :
        return True
    else :
        return False


print(Gradien(makepoint(2,4),makepoint(5,7)))
print(Gradien(makepoint(2,2),makepoint(8,3)))
print(is_sejajar(makepoint(2,4),makepoint(5,7),makepoint(2,2),makepoint(8,3)))
print(is_tegaklurus(makepoint(2,4),makepoint(5,7),makepoint(2,2),makepoint(8,3)))
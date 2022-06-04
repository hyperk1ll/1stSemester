class waktu :
    def __init__(self,j,m,d ) :
        self.x = j
        self.y = m
        self.z = d

def Jam(T) :
    return T.x

def Menit(T) :
    return T.y

def Detik(T) :
    return T.z

def MakeWaktu (a,b,c) :
    return (a,b,c)

def KonversiWaktu(P) :

    if (P > 86400) :
        r = (P-86400) // 3600
        s = ((P-86400)-(r*3600)) // 60
        t = (P-86400)-(r*3600)-(s*60)
        return MakeWaktu(r,s,t)
    
    else :
        r = P // 3600
        s = (P-(r*3600)) // 60
        t = P-(r*3600)-(s*60)
        return MakeWaktu(r,s,t)

def JumlahDetik (T) :
    return (Jam(T)*3600) + (Menit(T)*60) + (Detik(T))

def AddTime(T1,T2) :
    return  KonversiWaktu (JumlahDetik(T1)+ (JumlahDetik(T2)))

def AddTimeDetik(T,N) :
    return KonversiWaktu (JumlahDetik(T)+N)

def IsBefore(T1,T2) :
    return JumlahDetik(T1) < JumlahDetik(T2)

def IsAfter(T1,T2) :
    return JumlahDetik(T1) > JumlahDetik(T2)

T1=waktu(12,30,0)
T2=waktu(13,30,0)

print(JumlahDetik(T1))

print(AddTime(T1,T2))

print(AddTimeDetik(T1,T2))

print(IsBefore(T1,T2))

print(IsAter(T1,T2))
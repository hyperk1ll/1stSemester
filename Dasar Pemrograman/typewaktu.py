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

# PREDIKAT
def JumlahDetik(T):
    return (Hour(T)*3600) + (Minute(T)*60) + (Second(T))

def AddTime(T1,T2):
    return DetikToTime(JumlahDetik(T1) + JumlahDetik(T2))

def AddTimeSecond(T,N):
    return DetikToTime(JumlahDetik(T)+N)

def IsBefore(T1,T2):
    return JumlahDetik(T1) < JumlahDetik(T2)

def IsAfter(T1,T2):
    return JumlahDetik(T1) > JumlahDetik(T2)

T1=Time(10,30,0)
T2=Time(11,24,1)


print(DetikToTime(86500))
print(JumlahDetik(T1))
print(AddTime(T1,T2))
print(AddTimeSecond(T1,4000))
print(IsBefore(T1,T2))
print(IsAfter(T1,T2))

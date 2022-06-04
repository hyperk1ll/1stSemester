def FX2 (x):
    return (x*x)
def dif2 (x,y):
    return (FX2 (x-y))
def LS (x1,y1,x2,y2):
    return (math.sqrt(dif2(y2,x2) + dif2 (y1,x1)))

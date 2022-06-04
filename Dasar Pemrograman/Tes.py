import math as hype

a = hype.sqrt(81)
print(a)


  if(day(D2) > 1) and (month(D2) != 1 or month(D2) != 3):
        return (day(D2)) == (day(D1) + 1)
    elif(day(D2) == 1) and (month(D2) == 1):
        return (D1 == Date(31,12,(year(D2) - 1)))
    elif(day(D2) == 1) and (month(D2) == 3):
        if IsKabisat == True:
            return (Date(day(D1), month(D1), year(D1))) == (Date(29,(month(D2) - (1), year(D))))
        else:
            return (Date(day(D1), month(D1), year(D1))) == (Date(28,(month(D2) - (1), year(D))))

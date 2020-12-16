vikt = float(input("Hur mycket väger paketet?: "))
if vikt <= 2.0 :
    Pris = 30 * vikt
elif vikt <= 6.0 :
    Pris = 28 * vikt

elif vikt <= 12.0 :
    Pris = 25 * vikt

else:
    Pris = 23 * vikt

print ("Det kommer att kosta", Pris, "kr")
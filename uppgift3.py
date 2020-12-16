antal_paket = int(input("Hur många paket vill du skicka?: "))         #Frågar efter hur många paket användaren vill skicka och begär en inmatning
summa = 0                                                             #Summan från start är 03
i = 0                                                 # i är en variabel som får while loopen att gå igenom loopen. Ökas succesivt tills dess att den är lika med antal paket och då tar while loopen slut
while i < antal_paket:                               # Medan i är mindre än antal paket ska while loopen fortsätta
    vikt = float(input("Hur mycket väger paket " + str(i+1) + "?"))   #Frågar efter vikt för varje paket
    if vikt <= 2.0 :                                     
        summa += 30 * vikt                               #Om vikten är mindre eller lika med 2 så ska summan adderas med 30 * vikten
    elif vikt <= 6.0 :                                   #Annars ska om vikten är mindre eller lika med 6 ska summan adderas med 28 * vikten
        summa += 28 * vikt 
    elif vikt <= 12.0 :
        summa += 25 * vikt
    else:
        summa += 23 * vikt
    i+=1                                             #i ska adderas med 1 för varje gång den loopas
print("Det kommer att kosta",summa,"kr.")            #Efter while loopen stannar så ska totala summan skrivas ut

Rader = int(input("Ange antal rader: "))
Kolumner = int(input("Ange antal kolumner: "))
i=1
while i <= Rader:
    j = 1
    while j <= Kolumner:
        print("{:2d}".format(j * i), end=" ")
        j+=1
    i+=1
    print()





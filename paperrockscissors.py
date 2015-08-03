import random


dzialaj = True

while dzialaj:
    wybor = int(raw_input("Wybierz wciskajac przypisana liczbe: \n 1. Kamien \n 2. Nozyce \n 3. Papier\n"))

    if wybor > 3:
        print "Sa tylko trzy opcje Tytanie Intelektu"

    komp = random.randint(1,3)

    if wybor == komp:
        print "Remis!"
        
    if (wybor == 1 and komp == 3 or wybor == 2 and komp == 1 or wybor == 3 and komp == 2):
        print "Przegrales"

    if (wybor == 3 and komp == 1 or wybor == 1 and komp == 2 or wybor == 2 and komp == 3):
        print "Wygrales"

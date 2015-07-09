#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random, time

localtime= time.asctime(time.localtime(time.time()))
print ("Aktualny czas :", localtime)

print("Witaj! Czy chcesz poznac swoje szczesliwe liczby na dzis?\nJesli tak, to wcisnij 1.\nJesli nie, wybierz 2")
answer = int(raw_input())
if answer == 1:
    print ("Oto i one:")
else:
    print ("Milego dnia!")
    exit(0)
    
ileliczb = int(6)    
liczby = []
i = 0
while i < ileliczb:
    liczba = random.randint(1,49)
    if liczby.count(liczba) == 0:
        liczby.append(liczba)
        i = i + 1

print liczby

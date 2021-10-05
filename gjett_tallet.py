from random import randint

hemmeligTall = randint(1, 1000000)
gjett = -1
forsok = 0
grense = 21

print("Velkommen til mattespillet vårt! Wihu!")
print("Jeg tenker på et tall mellom 1-100. Klarer du å gjette det?")

while (forsok < grense):
    gjett = int(input("Gjett et heltall mellom 1-100: "))
    forsok += 1
    if (gjett > hemmeligTall):
        print("Lavere! Du har " + str(grense - forsok) + " forsøk igjen")
    elif (gjett < hemmeligTall):
        print("Høyere! Du har " + str(grense - forsok) + " forsøk igjen")
    else:
        print("Gratulerer du gjettet riktig tall! Det var: " + str(hemmeligTall))
        break

if (hemmeligTall == gjett):
    print("du vant")
else:
    print("Beklager du tapte. Det hemmelige tallet var: " + str(hemmeligTall))

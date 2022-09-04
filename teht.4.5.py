käyttäjä = "python"
salasana = "rules"

k_1 = input("Kirjoita käyttäjätunnus\n")
k_2 = input("Kirjoita salasana\n")
laskuri = 0

while laskuri < 5:
    if käyttäjä != k_1 or salasana != k_2:
        k_1 = input("Kirjoita käyttäjätunnus\n")
        k_2 = input("Kirjoita salasana\n")
        laskuri += 1
    else:
        laskuri += 10

if laskuri > 5:
    print("Tervetuloa")
else:
    print("Pääsy evätty")
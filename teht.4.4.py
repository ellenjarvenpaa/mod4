import random
x = random.randint(1, 10)

arvaus = int(input("Arvaa numero 1 ja 10 välillä.\n"))

while arvaus != x:
    if x > arvaus:
        print("Liian pieni arvaus")
    elif x < arvaus:
        print("Liaan suuri arvaus")
    arvaus = int(input("Arvaa numero 1 ja 10 välillä.\n"))

print("Oikein")


from random import randint

stevilo = randint(0, 30)

for poiskus in range(5):
    cifra = int(input("vnesi stevilo "))

    if(stevilo == cifra):
        print("mater uganu si!")
        break
    elif (stevilo > cifra):
        print("vpisi vecjo cifro")
    else:
        print("vpisi manjso cifro")
print("stevilo je bilo", stevilo)
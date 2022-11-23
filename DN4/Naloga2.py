import math

stevila = [5, 3, 0, 2, 10, 7, 4, 6, 5, 4]


print("Najmanjše število v arrayju je:", min(stevila))

print("\nNajvečje število v arrayju je:", max(stevila))

print("\nPovprečje števil v arrayju je:", math.fsum(stevila)/len(stevila))

for x in stevila:
    if x == round(math.fsum(stevila)/len(stevila)):
        print("\nStevilo najbližje povprečju", x)
        break


#V primeru če bi želeli vedeti ali se število, ki je najbljižje povprečju ponavjla
#ali odstranimo "break" v if stavku ali pa bi kodo spremenili, da bi izpisali katero 
#je najbližje in dodali kolikokrat se ponavlja
data = {"prices": [41970, 40721, 41197, 41137, 43033],
       "volume": [49135346712, 50768369805, 47472016405, 34809039137, 38700661463]}


def najvecja_vrednost(podatki): 
    # dopolnite funkcijo z lastno kodo
    celota = []
    for value in podatki.values():
        maxN = max(value)
        celota.append(maxN)
    return(celota)

# uporaba
vrednosti=najvecja_vrednost(data)
print(vrednosti)
#>>> [43033, 50768369805]


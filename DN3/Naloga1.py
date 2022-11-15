def emso_leta_preracun():

    while True: #preverja da vpišeš točno 14 številk za EMŠO kar je več ali manj ti da možnost ponovnega vpisa
        EMSO = input("Vpisi EMSO stevilko: ")
        if len(EMSO) < 12:
            print("Premalo stevilk ponovno vpisi")
        elif len(EMSO) > 13:
            print("Preveč številk ponovno vpiši")
        else:
            break    

    trenutno_leto = 2022
    starost = 0

    if(int(EMSO[4]) == 9):
        letnica = '1' + EMSO[4] + EMSO[5] + EMSO[6]
        starost = trenutno_leto - int(letnica)
        print("Leto rojstva:", letnica)
    elif(int(EMSO[4]) == 0):
        letnica = '2'+ EMSO[4] + EMSO[5] + EMSO[6]
        starost = trenutno_leto - int(letnica)
        print("Leto rojstva:", letnica)
    else:
        print("You probably died already or don't yet exist")
        starost = "o-o"
    
    

    return(starost)
    


starost = emso_leta_preracun()
print("Glede na letnico si star:", starost)

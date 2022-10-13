st1=int(input("Vpisi prvo stevilo: "))
st2=int(input("Vpisi drugo stevilo: "))
st3=int(input("Vpisi tretje stevilo: "))

print(st1)
print(type(st1))

print(st2)
print(type(st2))

print(st3)
print(type(st3))

# ker piše 3 celoštevilčne sem že v začetu vrednosti nastavil na int in pa tudi če tega nebi storil bi program
# vrnil napako da operatorji < > <= >=... ne delujejo na stringih

if(st1 == st2) or (st3 <= st1):
    print("eden od zgornjih pogojev je pravilen zato sem se izvedel")
else:
    print("hmm zgleda da nobeden od zgornjih dveh pogojev ni pravilen")

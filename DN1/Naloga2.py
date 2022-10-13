st1=int(input("Vpisi prvo stevilo: "))
st2=int(input("Vpisi drugo stevilo: "))

# uporabim int(...) zaradi tega ker python prebrano vrednost ovrednoti kot string in v primeru seštevanja ne sešteje števili ampak
# bi samo skupaj dal 2 stringa npr: st1=5, st2=10 v primeru stringa dobimo 510 namesto 15
# int(...) bi lahko uporabili tudi po že vpisu sampak s tem dodamo 2 nepotrebni vrstici

print("st1 + st2 = ", st1+st2)
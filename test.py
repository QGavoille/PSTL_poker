import projet

test = projet.Game("cards.projet")
x0_matches = projet.getx0(test)
x0_java = input()

for x0 in x0_matches:
    print("x0 = %s, x0_java = %s" % (x0, x0_java))
    if x0 != x0_java:
        print("Différents !")
    else:
        print("Identiques !")
        exit(0)
print("Aucun x0 ne correspond à celui de java !")
exit(1)

import projet

test = projet.Game("cards.projet")
x0x1, deck = projet.getBitCardInfo(test)
print(x0x1)
try:
    X0 = projet.trouveX0(x0x1)
    print("X0 = %s" % X0)
except Exception as e:
    print(e)
    exit(1)

"""x0_matches, deck = projet.getx0(test)
print((x0_matches[0]))
print(projet.cut("01100010111000111101011001111111"), " le vrais")
c = x0_matches[0]
print(projet.cut(c), " le trouvé")
x1_matches = projet.getx1(test, deck)
print(projet.cut(x1_matches[0]), " le x1 trouvé")
print(projet.trouvex0x1fixe(x0_matches[0], "11110110110111111010011100111101"))"""

'''
x0 = x0_matches[0][0]
k = 2
l = 6

print("experiences sur res_______")
res = projet.cut(x0)
print(res)
res.insert(k,projet.complete(projet.int2bin(52 + l)))
print(res)
res = res[:6]
print(res)
res = projet.uncut(res)
projet.cut(res[:32])
#print(projet.trouveX0x1fixe(x0_matches[0][0],"11010111110101111001000001111010"))
'''

import projet

test = projet.Game("cards.projet")
x0_matches = projet.getx0(test)
print((x0_matches[0]))
print(projet.cut("10011110111101101100011101001110"), " le vrais")
c = x0_matches[0][0]
print(projet.cut(c)," le trouvé")
print(projet.trouveX0x1fixe(x0_matches[0][0],"11110001011000101001111000001100"))

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
import projet

test = projet.Game("cards.projet")
x0_matches = projet.getx0(test)
print((x0_matches[0]))
print(projet.cut("11101110000001000110100101111110"), " le vrais")
c = x0_matches[0][0]
print(projet.cut(c)," le trouvé")
#print(projet.trouveX0x1fixe(x0_matches[0][0],"00101000100100001001111001000010"))
d = x0_matches[0][0]
d = projet.cut(d)
k = 0
l = 4
j = 3
n = 10
d.insert(k, projet.complete(projet.int2bin(52+j)))
d.insert(l, projet.complete(projet.int2bin(52 + n)))
d = d[:6]
r = projet.uncut(d)[:32]
print(projet.cut(r))
print(projet.x32bitsTo48bits(projet.b2tob10("11101110000001000110100101111110"),1115228436))
print(projet.trouveX0x1fixe(x0_matches[0][0],"00101000100100001001111001000010"))

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
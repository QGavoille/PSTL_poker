import sys

import projet

sys.path.append('../')

def recup(l,pos):
    toret = []
    for k in l:
        toret += [k[pos:(pos+6)]]
    return toret

print(projet.getMyCards(projet.recupFile(), 0))
print(projet.getNextPlayerCard(projet.recupFile(), 0))
print(projet.getNextNextPlayerCard(projet.recupFile(),0))
print(projet.getTable(projet.recupFile(),0))
print(projet.card2int('10 de PIQUE'))
print(projet.recupX(projet.recupFile()))

print(projet.int2bin(1))
print(projet.int2bin(52))
print(projet.isValid("001011",0))

print(projet.convert("001011",0))
print(projet.newRecupX(projet.recupFile()),12)
print(projet.b2tob10("101100"))
print(projet.int2bin(22))

#10111001100110110001011001010011
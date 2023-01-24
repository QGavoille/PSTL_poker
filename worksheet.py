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
#print(projet.recupX(projet.recupFile()))

print(projet.int2bin(1))
print(projet.int2bin(52))
print(projet.isValid("001011",0))

print(projet.convert("001011",0))
#print(projet.newRecupX(projet.recupFile()),12)
print(projet.b2tob10("101100"))
print(projet.int2bin(22))

#print(projet.unshuffleSbs("3 de PIQUE",0,["3 de PIQUE","1 de PIQUE","2 de PIQUE"]))
#print(51==projet.card2int(projet.int2card(51)))
print(projet.card2int("6 de CARREAU"))


#print(projet.scan(projet.recupFile()))
print(projet.card2int("1 de PIQUE"))
print(projet.card2int(projet.getTable(projet.recupFile(),0)[0]))
print(projet.recupXagain(projet.recupFile()))
print(projet.x32bitsTo48bits(2042017850,-2276942239))

# 10111001100110110001011001010011

'''
def newRecupX(s):
    l = []
    toret = [""]
    for k in range(5):
          l += [getTable(s,0)[k]]
    l += [getMyCards(s,0)[0]]
    l += [getMyCards(s,0)[1]]
    l += [getNextPlayerCard(s, 0)[0]]
    l += [getNextPlayerCard(s, 0)[1]]
    l += [getNextNextPlayerCard(s, 0)[0]]
    l += [getNextNextPlayerCard(s, 0)[1]]

    for k in range(5):
        if isValid(complete(int2bin(card2int(l[k]) - k)), k):
            tmp = []
            for d in toret:
                tmp += [d+complete(int2bin(card2int(l[k])-k))]
            toret = tmp
        else:
            toadd = []
            print("here")
            for d in toret:
                toadd += [d+complete(int2bin(card2int(l[k])-k))]
                toadd+=[d+convert(complete(int2bin(card2int(l[k])-k)),k)]
            toret = toadd
    toadd = []
    if isValid(complete(int2bin(card2int(l[5]) - 5)),5):

        for k in toret:
            toadd += [k+complete(int2bin(card2int(l[5])-5))[0]+complete(int2bin(card2int(l[5])-5))[1]]
    else:
        toadd = []
        for d in toret:
            toadd += [d + complete(int2bin(card2int(l[5]) - 5))[0]+complete(int2bin(card2int(l[5]) - 5))[1]]
            toadd += [d + convert(complete(int2bin(card2int(l[5]) - 5)), 5)[0]+convert(complete(int2bin(card2int(l[5]) - 5)), 5)[1]]

    toret = toadd


    return toret'''

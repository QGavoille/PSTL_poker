

def recupFile():
    file = open("cards.projet")
    s = ""
    for k in file.readlines():
        s+= k
    return s


def getMyCards(s,i):
    '''

    :param s: contenu du fichier
    :param i: manche que l'on souhaite examiner
    :return: couple des cartes possédées par moi même
    '''
    manche = s.split("<>")[i]
    manche = manche.split("\n")[0]
    cards = manche.split(":")[1]
    return cards.split(";")[0],cards.split(";")[1]

def getNextPlayerCard(s,i):
    '''

    :param s: contenu du fichier
    :param i: manche que l'on souhaite examiner
    :return: couple des cartes possédéees par le joueur 1
    '''
    manche = s.split("<>")[i]
    manche = manche.split("\n")[2]
    cards = manche.split(":")[1]
    return cards.split(";")[0], cards.split(";")[1]


def getNextNextPlayerCard(s,i):
    '''

    :param s: contenu du fichier
    :param i: manche que l'on souhaite examiner
    :return: couple des cartes possédées par le joueur 2
    '''
    manche = s.split("<>")[i]
    manche = manche.split("\n")[3]
    cards = manche.split(":")[1]
    return cards.split(";")[0], cards.split(";")[1]

def getTable(s,i):
    manche = s.split("<>")[i]
    manche = manche.split("\n")[1]
    cards = manche.split(":")[1]
    ret = cards.split(";")
    return ret[0],ret[1],ret[2],ret[3],ret[4]



def card2int(s):
    ret = s.replace(" ","")
    ret = ret.split("de")
    if ret[1] == "PIQUE":
        return int(ret[0])-1
    elif ret[1]== "TREFLE":
        return int(ret[0])-1+13
    elif ret[1] == "COEUR":
        return int(ret[0])-1+26
    else :
        return int(ret[0])-1+39


def int2bin(i):
    return "".join(reversed(bin(i).split("0b")[1]))
def complete(i):
    if(len(i)>6):
        print(len(i))
        return "0"
    if len(i)!= 6:
        while len(i)!= 6:
            i = i+"0"

    return i

def b2tob10(i):
    cpt = 0
    for k in range(len(i)):
        cpt+= (2**k)*int(i[k])
    return cpt

def recupX(s):
    l = []

    for k in range(5):
          l += [getTable(s,0)[k]]
    l += [getMyCards(s,0)[0]]
    l += [getMyCards(s,0)[1]]
    l += [getNextPlayerCard(s, 0)[0]]
    l += [getNextPlayerCard(s, 0)[1]]
    l += [getNextNextPlayerCard(s, 0)[0]]
    l += [getNextNextPlayerCard(s, 0)[1]]
    cpt = ""
    for k in range(5):
        cpt = cpt+complete(int2bin(card2int(l[k])-k))#30 bits

    cpt = cpt + complete(int2bin(card2int(l[5])-5))[-2]#31 bits
    cpt = cpt +complete(int2bin(card2int(l[5])-5))[-1]#31 bits
    return cpt

def isValid(bits,decalage):
    if(b2tob10(bits)<12+decalage):
        return False
    return True

def convert(bits,decalage):
    b10 = b2tob10(bits)
    b10 = b10 +(52-decalage)
    return int2bin(b10)

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


    return toret

#TODO regler le problème du melange (permutation 1-3 puis 2-3)
#TODO regler le problème des 2 derniers bits







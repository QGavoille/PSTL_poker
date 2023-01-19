

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
    return bin(i).split("0b")[1]
def complete(i):
    if(len(i)>6):
        print(len(i))
        return "0"
    if len(i)!= 6:
        while len(i)!= 6:
            i = "0"+i

    return i

def b2tob10(i):
    cpt = 0
    for k in range(len(i)):
        cpt+= (2**k)*int(i[len(i)-1-k])
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
    for i in range(5):

        cpt = complete(int2bin(card2int(l[i])))+cpt
    cpt = "".join(reversed(complete(int2bin(card2int(l[6])))[-1]+cpt))


    return b2tob10(cpt) #bit de poids faible a droite




print(getMyCards(recupFile(),0))
print(getNextPlayerCard(recupFile(),0))
print(getNextNextPlayerCard(recupFile(),0))
print(getTable(recupFile(),0))
print(recupX(recupFile()))
print(complete(int2bin(6)))





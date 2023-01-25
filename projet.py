

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
    '''

    :param s: string: contenu du fichier
    :param i: manche que l'on souhaite examiner: pour examiner la premiere i = 0
    :return: liste des cartes de la table par ordre chronologique
    '''
    manche = s.split("<>")[i]
    manche = manche.split("\n")[1]
    cards = manche.split(":")[1]
    ret = cards.split(";")
    return ret[0],ret[1],ret[2],ret[3],ret[4]



def card2int(s):
    '''

    :param s: chaine de caractère représentant la carte de la forme valeur "de" "TYPE" en majuscule
    :return: entier correspondant a la carte
    '''
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
    '''

    :param i: entier base 10
    :return: i en base 2
    '''
    return "".join(reversed(bin(i).split("0b")[1]))
def complete(i):
    '''

    :param i: entiers
    :return:  i completer de 0 a droite
    '''
    if(len(i)>6):
        print(len(i))
        return "0"
    if len(i)!= 6:
        while len(i)!= 6:
            i = i+"0"

    return i

def b2tob10(i):
    '''

    :param i: entiers en base 2
    :return:  entier en base 10
    '''
    cpt = 0
    for k in range(len(i)):
        cpt+= (2**k)*int(i[k])
    return cpt


def isValid(bits,decalage):
    '''

    :param bits: groupe de 6 bits
    :param decalage: manche a laquelle on se trouve
    :return: true si le groupe de 6 bits est ambigu (depasse 52-decalage)
    '''
    if(b2tob10(bits)<12+decalage):
        return False
    return True

def convert(bits,decalage):
    '''

    :param bits: groupe de 6 bits
    :param decalage: décalage
    :return: le groupe de 6 bits auquel on a appliquer le décalage
    '''
    b10 = b2tob10(bits)
    b10 = b10 +(52-decalage)
    return int2bin(b10)



#une permutation pose un problème quand si on l'inverse alors les éléments ne sont pas en ordre


def makePerm(dep,ar,l = [k for k in range(51)]):
    '''
    :param dep: indice de départ
    :param ar: indice d'arrivé
    :param l: liste danslaquelle on doit permuter l[dep] et l[ar]
    :return: l permutée
    '''
    tmp = l[dep]
    l[dep ] = l[ar]
    l[ar] = tmp
    return l



def recupXagain(s):
    '''

    :param s: contenu du fichier
    :return: x0
    '''
    deck = [k for k in range(52)]
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
        if isValid(int2bin(deck.index(card2int(l[k])) - k),k):
            tmp = []
            for qqc in toret:
                tmp += [qqc+complete(int2bin(deck.index(card2int(l[k]))-k))]

            toret = tmp
        else:
            toadd = []
            for qqc in toret:
                toadd+= [qqc+complete(int2bin(deck.index(card2int(l[k]))-k))]
                toadd+= [qqc+convert(int2bin(deck.index(card2int(l[k]))-k),k)]
            toret = toadd
        makePerm(k, deck.index(card2int(l[k])), deck)
    tmp = []
    for k in toret:
        tmp+=[k+int2bin(card2int(l[5])-5)[0]+int2bin(card2int(l[5])-5)[1]]
    toret = tmp

    return toret


def x32bitsTo48bits(x0,x1):
    '''

    :param x0: graine en 32 bits
    :param x1: f(x0) en 32 bits
    :return: x0 sur 48 bits
    '''
    x = int2bin(x0)
    for k in range(2**16):
        f = b2tob10(x+int2bin(k))
        if(25214903917*f+11)%(2**48) == x1:
            return f
    return f

#TODO regler le problème des 2 derniers bits







import json
from typing import Tuple, List, Any


class Game:

    def __init__(self, filePath: str):
        with open(filePath, 'r') as file:
            self.__content = json.load(file)

    def getPlayerData(self, playerId: int) -> dict:
        return self.__content['playerCards'][playerId]

    def getTableData(self) -> list:
        return self.__content['tableCards']

    def __str__(self):
        ret = ""
        ret += "Joueur 1 (moi): " + str(self.getPlayerData(0)) + "\n"
        ret += "Joueur 2: " + str(self.getPlayerData(1)) + "\n"
        ret += "Joueur 3: " + str(self.getPlayerData(2)) + "\n"
        ret += "Joueur 4: " + str(self.getPlayerData(3)) + "\n"
        ret += "Table: " + str(self.getTableData()) + "\n"
        return ret


def card2int(card: dict):
    '''

    :param s: Dictionnaire représentant la carte
    :return: entier correspondant a la carte
    '''
    if card["couleur"] == "PIQUE":
        return int(card["valeur"]) - 1
    elif card["couleur"] == "TREFLE":
        return int(card["valeur"]) - 1 + 13
    elif card["couleur"] == "COEUR":
        return int(card["valeur"]) - 1 + 26
    else:
        return int(card["valeur"]) - 1 + 39


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
    while len(i) != 6:
        i = i + "0"
    return i


def b2tob10(i):
    '''

    :param i: entiers en base 2
    :return:  entier en base 10
    '''
    cpt = 0
    for k in range(len(i)):
        cpt += (2 ** k) * int(i[k])
    return cpt

def isAmbiguous(bits, decalage):
    '''

    :param bits: groupe de 6 bits
    :param decalage: manche a laquelle on se trouve
    :return: true si le groupe de 6 bits est ambigu (depasse 52-decalage)
    '''
    if b2tob10(bits) < 12 + decalage:
        return True
    return False


def convert(bits, decalage):
    '''

    :param bits: groupe de 6 bits
    :param decalage: décalage
    :return: le groupe de 6 bits auquel on a appliquer le décalage
    '''
    b10 = b2tob10(bits)
    b10 = b10 + (52 - decalage)
    return int2bin(b10)


# une permutation pose un problème quand si on l'inverse alors les éléments ne sont pas en ordre


def makePerm(dep, ar, l=[k for k in range(51)]):
    '''
    :param dep: indice de départ
    :param ar: indice d'arrivée
    :param l: liste dans laquelle on doit permuter l[dep] et l[ar]
    :return: l permutée
    '''
    tmp = l[dep]
    l[dep] = l[ar]
    l[ar] = tmp
    return l



def getx0(game: Game) -> list:
    '''

    :param game: objet Game représentant la partie
    :return: tous les x0 possibles en représentation binaire avec les bits de poids fort à droite
    '''
    deck = [k for k in range(52)]
    x0 = [""]
    l = [game.getTableData()[i] for i in range(5)]#recupt
    for k in range(4): #recup les autes
        l += game.getPlayerData(k)["cards"][:2]
    for k in range(5):  # lecture des cartes de la table
        if not isAmbiguous(int2bin(deck.index(card2int(l[k]))-k),k):
            tmp = []
            for qqc in x0:
                tmp+= [qqc + complete(int2bin(deck.index(card2int(l[k])) - k))]
            x0 = tmp
        else:
            toadd = []
            for qqc in x0:
                toadd += [qqc + complete(int2bin(deck.index(card2int(l[k])) - k))]
                toadd += [qqc + convert(int2bin(deck.index(card2int(l[k])) - k), k)]
            x0 = toadd
        makePerm(k,deck.index(card2int(l[k])),deck)

    if not isAmbiguous(int2bin(deck.index(card2int(l[5])) - 5), 5):
        toadd = []
        for qqc in x0:
            toadd += [qqc + complete(int2bin(deck.index(card2int(l[5])) - 5))[0]+complete(int2bin(deck.index(card2int(l[5])) - 5))[1]]
    else:
        toadd = []
        for qqc in x0:
            toadd += [qqc + complete(int2bin(deck.index(card2int(l[5])) - 5))[0]+ complete(int2bin(deck.index(card2int(l[5])) - 5))[1]]
            toadd += [qqc + convert(int2bin(deck.index(card2int(l[5])) - 5), 5)[0]+convert(int2bin(deck.index(card2int(l[5])) - 5), 5)[1]]
    x0 = toadd



    return x0,deck



def getx1(game: Game, deck) -> list:
    x1 = []
    deck = deck
    l = [game.getTableData()[i] for i in range(5)]
    for k in range(4):  # lecture des 4 premiers bits
        l += game.getPlayerData(k)["cards"][:2]

    if not isAmbiguous(int2bin(deck.index(card2int(l[5]))-5),5):
        x1 += [complete(int2bin(deck.index(card2int(l[5]))-5))[2:]]
    else:
        x1+= [complete(int2bin(deck.index(card2int(l[5]))-5))[2:]]
        x1+= [convert(int2bin(deck.index(card2int(l[5]))-5),5)[2:]]


    makePerm(5, deck.index(card2int(l[5])), deck)
    for k in range(4):#Lecture de 24bits
        if not isAmbiguous(int2bin(deck.index(card2int(l[6+k]))-(6+k)), 6+k):
            tmp = []
            for qqc in x1:
                tmp+= [qqc +complete(int2bin(deck.index(card2int(l[6+k]))-(6+k)))]
            x1 = tmp
        else:
            tmp = []
            for qqc in x1:
                tmp += [qqc + complete(int2bin(deck.index(card2int(l[6+k])) - (6+k)))]
                tmp += [qqc + convert(int2bin(deck.index(card2int(l[6+k])) - (6+k)), 6+k)]
            x1 = tmp
        makePerm(5+k,deck.index(card2int(l[5+k])),deck)
    if not isAmbiguous(int2bin(deck.index(deck.index(card2int(l[10]))-10)),10):
        tmp = []
        for qqc in x1:
           tmp += [qqc + complete(int2bin(deck.index(card2int(l[10]))-10))[0:5]]
    else:
        tmp = []
        for qqc in x1:
            tmp += [qqc + complete(int2bin(deck.index(card2int(l[10]))-10))[0:4]]
            tmp += [qqc + convert(int2bin(deck.index(card2int(l[10]))-10),10)[0:4]]
        x1 = tmp
    return x1










#TODO regler le problème des 2 derniers bits


def suivant(x):
    a = 25214903917
    c = 11
    m = 2 ** 48

    return (a * x + c) % m



def javaBitsToHumanInteger(x02):
    cpt = b2tob10(x02)
    if x02[-1] == "1":
        cpt = cpt - 2 ** 32

    return cpt


def x32bitsTo48bits(x0, x1):
    '''
    :param x0: graine en 32 bits(int)
    :param x1: f(x0) en 32 bits(int)
    :return: x0 sur 48 bits
    '''

    x = x0
    x *= 2 ** 16

    for k in range(2 ** 16):
        d = (suivant(x) // 2 ** 16)
        nx1 = x1
        if x1 <0 :
            nx1 = x1+(2**32)
        if d == nx1:
            print("hey")
            if x<0:
                return x+2**48
            else:
                return x
        x += 1

    return None

def listto48bits(l,x1):
    ret = []
    for k in l:
        if x32bitsTo48bits(javaBitsToHumanInteger(k), x1) is not None:
            ret += [x32bitsTo48bits(javaBitsToHumanInteger(k), x1)]
    return ret

def cut (x0):
    '''
    coupe x0 en 5 paquets de 5 bits plus 1 packet de 2 bits
    :param x0:
    :return:
    '''
    l = []
    for k in range(5):
        l+= [x0[k*6:6*k+6]]
    return l+[x0[-2:]]

def uncut(l):
    '''
    inverse de cut
    :param l:
    :return:
    '''
    x0 = ""
    for k in l:
        x0 += k
    return x0

def trouveX0x1fixe(x0,x1):
    '''
    On donne le x0 lu dans les cartes et un x1 fixé.
    L'algorithme vas alors tester si le x0 lu corresponds bien au x1 donné par l'utilisateur
    Si ce n'est pas le cas il vas alors supposer qu'il y'a eu 1 rejet ie que 6 bits sont faux.
    alors il vas tester si le rejet a eu lieu au 1er groupe de 6 bits ( 12 possibilitées), puis au 2eme,...
    Si on echoue avec 1 rejet on passe a 2 etc.
    :param x0: string
    :param x1:string
    :return:
    '''

    if not x32bitsTo48bits(b2tob10(x0),b2tob10(x1)) is None: #cas ou 0 rejet
        return x0

    else:
        for k in range(5):#cas ou il y'a un rejet

            for l in range(12):

                res = cut(x0)
                res.insert(k,complete(int2bin(52+l)))
                res = res[:6]
                res = uncut(res)[:32]


                if not x32bitsTo48bits(b2tob10(res),b2tob10(x1)) is None:
                    return res
        for k in range(5): #cas ou 2 rejets

            d = cut(x0)
            for l in [x for x in range(5) if x>=k]:

                for j in range(12):
                    d = cut(x0)
                    d.insert(k, complete(int2bin(52+j-k)))
                    d = d[:6]
                    save = d.copy()
                    for n in range(12):
                        d = save.copy()
                        d.insert(l+k, complete(int2bin(52+n-l)))
                        d = d[:6]


                        r = uncut(d)[:32]
                        if(k==0 and l == 2 and j == 6 and n ==1):
                            print("passé")
                            print(d)
                            print(r)
                        if not x32bitsTo48bits(b2tob10(r),b2tob10(x1)) is None:
                            return r
                        d = save.copy()

                    d = cut(x0).copy()
    return None











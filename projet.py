import json


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
    l = [game.getTableData()[i] for i in range(5)]
    for k in range(4):
        l += game.getPlayerData(k)["cards"][:2]
    print(l)
    for k in range(5):  # lecture des cartes de la table
        possible_values = []
        possible_values += [complete(int2bin(deck.index(card2int(l[k])) - k))]
        if isAmbiguous(int2bin(deck.index(card2int(l[k])) - k), k):
            possible_values += [convert(complete(int2bin(deck.index(card2int(l[k])) - k)), k)]

        new_x0 = []
        for i in x0:
            for j in possible_values:
                new_x0.append(i + j)
        x0 = new_x0
        makePerm(k, deck.index(card2int(l[k])), deck)
    # il faut récupérer 2 bits supplémentaires sur les cartes suivantes
    carte_suivante = l[5]
    print(carte_suivante)
    possible_values = []
    possible_values += [complete(int2bin(deck.index(card2int(carte_suivante)) - 5))]
    if isAmbiguous(int2bin(deck.index(card2int(carte_suivante)) - 5), 5):
        possible_values += [convert(complete(int2bin(deck.index(card2int(carte_suivante)) - 5)), 5)]

    new_x0 = []
    for i in x0:
        for j in possible_values:
            new_x0.append(i + j)
    x0 = new_x0
    makePerm(5, deck.index(card2int(carte_suivante)), deck)

    # On récupère les 32 bits de poids faible
    for i in range(len(x0)):
        x0[i] = x0[i][-32:]
    return x0


def getx1(game: Game) -> list:
    '''

    :param game: objet Game représentant la partie
    :return: tous les x1 possibles en représentation binaire avec les bits de poids fort à droite
    '''
    deck = [k for k in range(52)]
    toret = [""]
    l = [game.getTableData()[i] for i in range(5)] + [game.getPlayerData(k) for k in range(4)]
    for k in range(5):  # lecture des cartes de la table
        if isAmbiguous(int2bin(deck.index(card2int(l[k])) - k), k):
            tmp = []
            for qqc in toret:
                tmp += [qqc + complete(int2bin(deck.index(card2int(l[k])) - k))]

            toret = tmp
        else:
            toadd = []
            for qqc in toret:
                toadd += [qqc + complete(int2bin(deck.index(card2int(l[k])) - k))]
                toadd += [qqc + convert(int2bin(deck.index(card2int(l[k])) - k), k)]
            toret = toadd
        makePerm(k, deck.index(card2int(l[k])), deck)
    toadd = []
    for k in toret:
        toadd += [k + complete(int2bin(card2int(l[5]) - 5))[0] + complete(int2bin(card2int(l[5]) - 5))[1]]
    else:
        toadd = []
        for d in toret:
            toadd += [d + complete(int2bin(card2int(l[5]) - 5))[0] + complete(int2bin(card2int(l[5]) - 5))[1]]
            toadd += [d + convert(complete(int2bin(card2int(l[5]) - 5)), 5)[0] +
                      convert(complete(int2bin(card2int(l[5]) - 5)), 5)[1]]
    toret = toadd

    return toret


def recupXagain(s):
    '''

    :param s: contenu du fichier
    :return: x0
    '''
    deck = [k for k in range(52)]
    l = []
    toret = [""]
    for k in range(5):
        l += [getTable(s, 0)[k]]
    l += [getMyCards(s, 0)[0]]
    l += [getMyCards(s, 0)[1]]
    l += [getNextPlayerCard(s, 0)[0]]
    l += [getNextPlayerCard(s, 0)[1]]
    l += [getNextNextPlayerCard(s, 0)[0]]
    l += [getNextNextPlayerCard(s, 0)[1]]
    for k in range(5):  # lecture des cartes de la table
        if isAmbiguous(int2bin(deck.index(card2int(l[k])) - k), k):
            tmp = []
            for qqc in toret:
                tmp += [qqc + complete(int2bin(deck.index(card2int(l[k])) - k))]

            toret = tmp
        else:
            toadd = []
            for qqc in toret:
                toadd += [qqc + complete(int2bin(deck.index(card2int(l[k])) - k))]
                toadd += [qqc + convert(int2bin(deck.index(card2int(l[k])) - k), k)]
            toret = toadd
        makePerm(k, deck.index(card2int(l[k])), deck)
    toadd = []
    for k in toret:
        toadd += [k + complete(int2bin(card2int(l[5]) - 5))[0] + complete(int2bin(card2int(l[5]) - 5))[1]]
    else:
        toadd = []
        for d in toret:
            toadd += [d + complete(int2bin(card2int(l[5]) - 5))[0] + complete(int2bin(card2int(l[5]) - 5))[1]]
            toadd += [d + convert(complete(int2bin(card2int(l[5]) - 5)), 5)[0] +
                      convert(complete(int2bin(card2int(l[5]) - 5)), 5)[1]]
    toret = toadd

    return toret




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
    :param x0: graine en 32 bits
    :param x1: f(x0) en 32 bits
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
            return x
        x += 1

    return None

def listto48bits(l,x1):
    ret = []
    for k in l:
        if x32bitsTo48bits(javaBitsToHumanInteger(k), x1) is not None:
            ret += [x32bitsTo48bits(javaBitsToHumanInteger(k), x1)]
    return ret

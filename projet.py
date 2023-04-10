import json
import time
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
    while len(i) < 6:
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


def getx0(game: Game) -> tuple[list[Any], list[int]]:
    '''

    :param game: objet Game représentant la partie
    :return: tous les x0 possibles en représentation binaire avec les bits de poids fort à droite
    '''
    deck = [k for k in range(52)]
    x0 = [""]
    l = [game.getTableData()[i] for i in range(5)]  # recupt
    for k in range(4):  # recup les autes
        l += game.getPlayerData(k)["cards"][:2]
    for k in range(5):  # lecture des cartes de la table
        if not isAmbiguous(int2bin(deck.index(card2int(l[k])) - k), k):
            tmp = []
            for qqc in x0:
                tmp += [qqc + complete(int2bin(deck.index(card2int(l[k])) - k))]
            x0 = tmp
        else:
            toadd = []
            for qqc in x0:
                toadd += [qqc + complete(int2bin(deck.index(card2int(l[k])) - k))]
                toadd += [qqc + convert(int2bin(deck.index(card2int(l[k])) - k), k)]
            x0 = toadd
        makePerm(k, deck.index(card2int(l[k])), deck)

    if not isAmbiguous(int2bin(deck.index(card2int(l[5])) - 5), 5):
        toadd = []
        for qqc in x0:
            toadd += [qqc + complete(int2bin(deck.index(card2int(l[5])) - 5))[0] +
                      complete(int2bin(deck.index(card2int(l[5])) - 5))[1]]
    else:
        toadd = []
        for qqc in x0:
            toadd += [qqc + complete(int2bin(deck.index(card2int(l[5])) - 5))[0] +
                      complete(int2bin(deck.index(card2int(l[5])) - 5))[1]]
            toadd += [qqc + convert(int2bin(deck.index(card2int(l[5])) - 5), 5)[0] +
                      convert(int2bin(deck.index(card2int(l[5])) - 5), 5)[1]]
    x0 = toadd

    return x0, deck


def getx1(game: Game, deck) -> list:
    x1 = []
    deck = deck
    l = [game.getTableData()[i] for i in range(5)]
    for k in range(4):  # lecture des 4 premiers bits
        l += game.getPlayerData(k)["cards"][:2]

    if not isAmbiguous(int2bin(deck.index(card2int(l[5])) - 5), 5):
        x1 += [complete(int2bin(deck.index(card2int(l[5])) - 5))[2:]]
    else:
        x1 += [complete(int2bin(deck.index(card2int(l[5])) - 5))[2:]]
        x1 += [convert(int2bin(deck.index(card2int(l[5])) - 5), 5)[2:]]

    makePerm(5, deck.index(card2int(l[5])), deck)
    for k in range(4):  # Lecture de 24bits
        if not isAmbiguous(int2bin(deck.index(card2int(l[6 + k])) - (6 + k)), 6 + k):
            tmp = []
            for qqc in x1:
                tmp += [qqc + complete(int2bin(deck.index(card2int(l[6 + k])) - (6 + k)))]
            x1 = tmp
        else:
            tmp = []
            for qqc in x1:
                tmp += [qqc + complete(int2bin(deck.index(card2int(l[6 + k])) - (6 + k)))]
                tmp += [qqc + convert(int2bin(deck.index(card2int(l[6 + k])) - (6 + k)), 6 + k)]
            x1 = tmp
        makePerm(5 + k, deck.index(card2int(l[5 + k])), deck)
    if not isAmbiguous(int2bin(deck.index(deck.index(card2int(l[10])) - 10)), 10):
        tmp = []
        for qqc in x1:
            tmp += [qqc + complete(int2bin(deck.index(card2int(l[10])) - 10))[0:5]]
    else:
        tmp = []
        for qqc in x1:
            tmp += [qqc + complete(int2bin(deck.index(card2int(l[10])) - 10))[0:4]]
            tmp += [qqc + convert(int2bin(deck.index(card2int(l[10])) - 10), 10)[0:4]]
        x1 = tmp
    return x1


def getBitCardInfo(game: Game) -> tuple[str, list[int]]:
    data = [game.getTableData()[i] for i in range(5)]
    deck = [k for k in range(52)]
    data_ret = ""
    for k in range(4):
        data += game.getPlayerData(k)["cards"][:2]
    for k in range(5 + 6):
        data_ret += complete(int2bin(deck.index(card2int(data[k])) - k))
        makePerm(k, deck.index(card2int(data[k])), deck)
    return data_ret[:64], deck


# TODO regler le problème des 2 derniers bits


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
        if x1 < 0:
            nx1 = x1 + (2 ** 32)
        if d == nx1:
            print("hey")
            if x < 0:
                return x + 2 ** 48
            else:
                return x
        x += 1

    return None


def listto48bits(l, x1):
    ret = []
    for k in l:
        if x32bitsTo48bits(javaBitsToHumanInteger(k), x1) is not None:
            ret += [x32bitsTo48bits(javaBitsToHumanInteger(k), x1)]
    return ret


def cut(x0):
    '''
    coupe x0 en 5 paquets de 5 bits plus 1 packet de 2 bits
    :param x0:
    :return:
    '''
    l = []
    for k in range(5):
        l += [x0[k * 6:6 * k + 6]]
    return l + [x0[-2:]]


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


def trouvex0x1fixe1r(x0, x1):
    for i in range(6):
        for i2 in range(12):
            d = cut(x0)
            d.insert(i, complete(int2bin(52 + i2)))
            d = d[:6]
            r = uncut(d)[:32]
            if not x32bitsTo48bits(b2tob10(r), b2tob10(x1)) is None:
                return r


def trouvex0x1fixe2r(x0, x1):
    for i in range(6):
        for j in range(i + 1, 6):
            for i2 in range(12):
                d = cut(x0)
                d.insert(i, complete(int2bin(52 + i2)))
                d = d[:6]
                r = uncut(d)[:32]
                for j2 in range(12):
                    d2 = cut(r)
                    d2.insert(j, complete(int2bin(52 + j2)))
                    d2 = d2[:6]
                    r2 = uncut(d2)[:32]
                    if not x32bitsTo48bits(b2tob10(r2), b2tob10(x1)) is None:
                        return r2


def trouvex0x1fixe3r(x0, x1):
    for i in range(6):
        print("i change", i)
        for j in range(i + 1, 6):

            for k in range(j + 1, 6):
                print("k change: ", k)
                for i2 in range(12):
                    print("i2 change", i2)
                    d = cut(x0)
                    d.insert(i, complete(int2bin(52 + i2)))
                    d = d[:6]
                    r = uncut(d)[:32]

                    for j2 in range(12):
                        d2 = cut(r)
                        d2.insert(j, complete(int2bin(52 + j2)))
                        d2 = d2[:6]
                        r2 = uncut(d2)[:32]

                        for k2 in range(12):
                            d3 = cut(r2)
                            d3.insert(k, complete(int2bin(52 + k2)))
                            d3 = d3[:6]
                            r3 = uncut(d3)[:32]
                            if not x32bitsTo48bits(b2tob10(r3), b2tob10(x1)) is None:
                                return r3


def trouvex0x1fixe4r(x0, x1):
    for i in range(6):
        print("i change", i)
        for j in range(i + 1, 6):
            for k in range(j + 1, 6):
                for l in range(k + 1, 6):

                    print("k change: ", k)
                    for i2 in range(12):
                        print("i2 change", i2)
                        d = cut(x0)
                        d.insert(i, complete(int2bin(52 + i2)))
                        d = d[:6]
                        r = uncut(d)[:32]

                        for j2 in range(12):
                            d2 = cut(r)
                            d2.insert(j, complete(int2bin(52 + j2)))
                            d2 = d2[:6]
                            r2 = uncut(d2)[:32]

                            for k2 in range(12):
                                d3 = cut(r2)
                                d3.insert(k, complete(int2bin(52 + k2)))
                                d3 = d3[:6]
                                r3 = uncut(d3)[:32]

                                for l2 in range(12):
                                    d4 = cut(r3)
                                    d4.insert(k, complete(int2bin(52 + l2)))
                                    d4 = d4[:6]
                                    r4 = uncut(d4)[:32]
                                    if not x32bitsTo48bits(b2tob10(r4), b2tob10(x1)) is None:
                                        return r4


def trouvex0x1fixe(x0, x1):
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

    if not x32bitsTo48bits(b2tob10(x0), b2tob10(x1)) is None:  # cas ou 0 rejet
        return x0
    d = trouvex0x1fixe1r(x0, x1)
    if d is not None:
        return d
    d = trouvex0x1fixe2r(x0, x1)
    if d is not None:
        return d
    d = trouvex0x1fixe3r(x0, x1)
    if d is not None:
        return d
    d = trouvex0x1fixe4r(x0, x1)  # TODO s'arreter
    if d is not None:
        return d

    return None
# TODO faire les calculs théoriques sur le nombre de moyen de rejets
# TODO integrer les distributions statistiques
# TODO ranger le git
# TODO Traiter x0 et x1 commme un gros paquet de 64 bits
# TODO installer pypy


def cut64bits(x0x1):
    """Cut a 64 bits string into 10 groups of 6 bits and a 4 bits group"""
    d = []
    for i in range(10):
        d.append(x0x1[i * 6:(i + 1) * 6])
    d.append(x0x1[60:])
    return d


def uncut64bits(d):
    """Concatenate a list of 10 groups of 6 bits and a 4 bits group into a 64 bits string"""
    x0x1 = ""
    for i in range(10):
        x0x1 += d[i]
    x0x1 += d[10]
    return x0x1


def insert1rejet(x0x1):
    print(cut64bits(x0x1))
    for i in range(11):
        for i2 in range(12):
            d = cut64bits(x0x1)
            d.insert(i, complete(int2bin(52 + i2)))
            d = d[:11]
            res = uncut64bits(d)[:64]
            ret = x32bitsTo48bits(b2tob10(res[:32]), b2tob10(res[32:]))
            if not (ret is None):
                return ret

    return None


def insert2rejets(x0x1):
    for i in range(10):
        for j in range(i + 1, 11):
            for i2 in range(12):
                d = cut64bits(x0x1)
                d.insert(i, complete(int2bin(52 + i2)))
                d = d[:11]
                x0x1 = uncut64bits(d)

                for j2 in range(12):
                    d2 = cut64bits(x0x1)
                    d2.insert(j, complete(int2bin(52 + j2)))
                    d2 = d2[:11]
                    x0x1 = uncut64bits(d2)
                    if not x32bitsTo48bits(b2tob10(x0x1[:32]), b2tob10(x0x1[32:])) is None:
                        return x0x1

    return None


def insert3rejets(x0x1):
    for i in range(9):
        for j in range(i + 1, 10):
            for k in range(j + 1, 11):
                for i2 in range(12):
                    d = cut64bits(x0x1)
                    d.insert(i, complete(int2bin(52 + i2)))
                    d = d[:11]
                    x0x1 = uncut64bits(d)

                    for j2 in range(12):
                        d2 = cut64bits(x0x1)
                        d2.insert(j, complete(int2bin(52 + j2)))
                        d2 = d2[:11]
                        x0x1 = uncut64bits(d2)

                        for k2 in range(12):
                            d3 = cut64bits(x0x1)
                            d3.insert(k, complete(int2bin(52 + k2)))
                            d3 = d3[:11]
                            x0x1 = uncut64bits(d3)
                            if not x32bitsTo48bits(b2tob10(x0x1[:32]), b2tob10(x0x1[32:])) is None:
                                return x0x1

    return None


def insert4rejets(x0x1):
    for i in range(8):
        for j in range(i + 1, 9):
            for k in range(j + 1, 10):
                for l in range(k + 1, 11):
                    for i2 in range(12):
                        d = cut64bits(x0x1)
                        d.insert(i, complete(int2bin(52 + i2)))
                        d = d[:11]
                        x0x1 = uncut64bits(d)

                        for j2 in range(12):
                            d2 = cut64bits(x0x1)
                            d2.insert(j, complete(int2bin(52 + j2)))
                            d2 = d2[:11]
                            x0x1 = uncut64bits(d2)

                            for k2 in range(12):
                                d3 = cut64bits(x0x1)
                                d3.insert(k, complete(int2bin(52 + k2)))
                                d3 = d3[:11]
                                x0x1 = uncut64bits(d3)

                                for l2 in range(12):
                                    d4 = cut64bits(x0x1)
                                    d4.insert(l, complete(int2bin(52 + l2)))
                                    d4 = d4[:11]
                                    x0x1 = uncut64bits(d4)
                                    if not x32bitsTo48bits(b2tob10(x0x1[:32]), b2tob10(x0x1[32:])) is None:
                                        return x0x1

    return None


def insert5rejets(x0x1):
    for i in range(7):
        for j in range(i + 1, 8):
            for k in range(j + 1, 9):
                for l in range(k + 1, 10):
                    for m in range(l + 1, 11):
                        for i2 in range(12):
                            d = cut64bits(x0x1)
                            d.insert(i, complete(int2bin(52 + i2)))
                            d = d[:11]
                            x0x1 = uncut64bits(d)

                            for j2 in range(12):
                                d2 = cut64bits(x0x1)
                                d2.insert(j, complete(int2bin(52 + j2)))
                                d2 = d2[:11]
                                x0x1 = uncut64bits(d2)

                                for k2 in range(12):
                                    d3 = cut64bits(x0x1)
                                    d3.insert(k, complete(int2bin(52 + k2)))
                                    d3 = d3[:11]
                                    x0x1 = uncut64bits(d3)

                                    for l2 in range(12):
                                        d4 = cut64bits(x0x1)
                                        d4.insert(l, complete(int2bin(52 + l2)))
                                        d4 = d4[:11]
                                        x0x1 = uncut64bits(d4)

                                        for m2 in range(12):
                                            d5 = cut64bits(x0x1)
                                            d5.insert(m, complete(int2bin(52 + m2)))
                                            d5 = d5[:11]
                                            x0x1 = uncut64bits(d5)
                                            if not x32bitsTo48bits(b2tob10(x0x1[:32]), b2tob10(x0x1[32:])) is None:
                                                return x0x1

    return None


def insert6rejets(x0x1):
    for i in range(6):
        for j in range(i + 1, 7):
            for k in range(j + 1, 8):
                for l in range(k + 1, 9):
                    for m in range(l + 1, 10):
                        for n in range(m + 1, 11):
                            for i2 in range(12):
                                d = cut64bits(x0x1)
                                d.insert(i, complete(int2bin(52 + i2)))
                                d = d[:11]
                                x0x1 = uncut64bits(d)

                                for j2 in range(12):
                                    d2 = cut64bits(x0x1)
                                    d2.insert(j, complete(int2bin(52 + j2)))
                                    d2 = d2[:11]
                                    x0x1 = uncut64bits(d2)

                                    for k2 in range(12):
                                        d3 = cut64bits(x0x1)
                                        d3.insert(k, complete(int2bin(52 + k2)))
                                        d3 = d3[:11]
                                        x0x1 = uncut64bits(d3)

                                        for l2 in range(12):
                                            d4 = cut64bits(x0x1)
                                            d4.insert(l, complete(int2bin(52 + l2)))
                                            d4 = d4[:11]
                                            x0x1 = uncut64bits(d4)

                                            for m2 in range(12):
                                                d5 = cut64bits(x0x1)
                                                d5.insert(m, complete(int2bin(52 + m2)))
                                                d5 = d5[:11]
                                                x0x1 = uncut64bits(d5)

                                                for n2 in range(12):
                                                    d6 = cut64bits(x0x1)
                                                    d6.insert(n, complete(int2bin(52 + n2)))
                                                    d6 = d6[:11]
                                                    x0x1 = uncut64bits(d6)
                                                    if not x32bitsTo48bits(b2tob10(x0x1[:32]), b2tob10(x0x1[32:])) is None:
                                                        return x0x1

    return None


def trouveX0(x0x1 : str) -> int:
    x0 = x0x1[:32]
    x1 = x0x1[32:]
    start = time.time()
    X0 = x32bitsTo48bits(b2tob10(x0), b2tob10(x1))
    end = time.time()
    print("0 rejet : " + str(end - start))
    if not (X0 is None):
        return X0
    start = time.time()
    X0 = insert1rejet(x0x1)
    end = time.time()
    print("1 rejet : " + str(end - start))
    if not (X0 is None):
        return X0
    start = time.time()
    X0 = insert2rejets(x0x1)
    end = time.time()
    print("2 rejets : " + str(end - start))
    if not (X0 is None):
        return X0
    start = time.time()
    X0 = insert3rejets(x0x1)
    end = time.time()
    print("3 rejets : " + str(end - start))
    if not (X0 is None):
        return X0
    start = time.time()
    X0 = insert4rejets(x0x1)
    end = time.time()
    print("4 rejets : " + str(end - start))
    if not (X0 is None):
        return X0
    start = time.time()
    X0 = insert5rejets(x0x1)
    end = time.time()
    print("5 rejets : " + str(end - start))
    if not (X0 is None):
        return X0
    start = time.time()
    X0 = insert6rejets(x0x1)
    end = time.time()
    print("6 rejets : " + str(end - start))
    if not (X0 is None):
        return X0
    raise Exception("Pas de X0 trouvé")


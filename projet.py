

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
    manche = manche.split("\n")[3]
    cards = manche.split(":")[1]
    return cards.split(";")[0], cards.split(";")[1]


def getNextNextPlayerCard(s,i):
    '''

    :param s: contenu du fichier
    :param i: manche que l'on souhaite examiner
    :return: couple des cartes possédées par le joueur 2
    '''
    manche = s.split("<>")[i]
    manche = manche.split("\n")[2]
    cards = manche.split(":")[1]
    return cards.split(";")[0], cards.split(";")[1]

def getTable(s,i):
    manche = s.split("<>")[i]
    manche = manche.split("\n")[1]
    cards = manche.split(":")[1]
    ret = cards.split(";")
    return ret[0],ret[1],ret[2],ret[3],ret[4]



print(getMyCards(recupFile(),0))
print(getNextPlayerCard(recupFile(),0))
print(getNextNextPlayerCard(recupFile(),0))
print(getTable(recupFile(),0))
import matplotlib.pyplot as plt
def parse(filename):
    file = open(filename)
    lines = file.readlines()
    result =[]
    for line in lines:
        result+= [line.strip()]
    abs = []
    ord = []
    for line in result[1:]:
        tmp = line.split("//")
        abs += [int(tmp[0])]
        ord += [int(tmp[1])]
    return abs,ord


def nomCarte(i):
    if i<14:
        return str(i)+" de pique "
    elif i<27:
        return str(i-13)+" de trefle "
    elif i<40:
        return str(i-26)+ " de coeur "
    else:
        return str(i-39)+ " de carreau "


def affiche(x,y,i):
    fig = plt.figure(figsize=(12,6))
    ax = fig.add_subplot(1,1,1)
    ax.bar(x,y)
    ax.set_xlabel("Position de la carte")
    ax.set_ylabel("Nombre de fois ou la carte considérée se trouve a la position x")
    ax.set_title("Fréquences des positions pour "+nomCarte(i)+"après mélange")

    plt.savefig("viz/graph"+str(i)+"bad.png")

def genereGraph():
    for k in range(1,52):
        x,y = parse("eta"+str(k)+".test")
        affiche(x,y,k)
    return 0

genereGraph()
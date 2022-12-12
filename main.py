import sys


def __main__():
    #   Symbole, Nom, numéro At, Masse At, Famille, Période
    H = ["H", "Hydrogène", "1", "1,01", "Alcalins", "1"]
    He = ["He", "Helium", "2", "4,00", "Gaz rares", "1"]
    Li = ["Li", "Lithium", "3", "6,94", "Alcalins", "2"]
    Be = ["Be", "Bérylium", "4", "9,01", "Alcalino-terreux", "2"]

    atome = str(input("Atome : "))

    if atome in H:
        print("Symbole chimique :", H[0])
        print("Nom de l'élément :", H[1])
        print("Numéro atomique :", H[2])
        print("Masse Atomique :", H[3])
        print("Famille :", H[4])
        print("Période :", H[5])
    elif atome in He:
        print("Symbole chimique :", He[0])
        print("Nom de l'élément :", He[1])
        print("Numéro atomique :", He[2])
        print("Masse Atomique :", He[3])
        print("Famille :", He[4])
        print("Période :", He[5])
    elif atome in Li:
        print("Symbole chimique :", Li[0])
        print("Nom de l'élément :", Li[1])
        print("Numéro atomique :", Li[2])
        print("Masse Atomique :", Li[3])
        print("Famille :", Li[4])
        print("Période :", Li[5])
    elif atome in Be:
        print("Symbole chimique :", Be[0])
        print("Nom de l'élément :", Be[1])
        print("Numéro atomique :", Be[2])
        print("Masse Atomique :", Be[3])
        print("Famille :", Be[4])
        print("Période :", Be[5])
    else:
        print("Wrong Input")
        sys.exit()


while True:
    __main__()

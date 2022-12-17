import sys  # import module sys


class atom:  # create the class atom
    def __init__(self,symbol,name,atomic_n,atomic_m,family,period,neutron,proton,electron, year,):
        self.symbol = symbol
        self.name = name
        self.atomic_n = atomic_n
        self.atomic_m = atomic_m
        self.family = family
        self.period = period
        self.neutron = neutron
        self.proton = proton
        self.electron = electron
        self.year = year

    def __init__(self, splittedLine):
        self.symbol = splittedLine[0]
        self.name = splittedLine[1]
        self.atomic_n = splittedLine[2]
        self.atomic_m = splittedLine[3]
        self.family = splittedLine[4]
        self.period = splittedLine[5]
        self.neutron = splittedLine[6]
        self.proton = splittedLine[7]
        self.electron = splittedLine[8]
        self.year = splittedLine[9]

    def PrintMe(self):  # def PrintMe function
        print("")
        print(f"| Symbole chimique : {self.symbol}")
        print(f"| Nom : {self.name}")
        print(f"| Numéro atomique : {self.atomic_n}")
        print(f"| Masse atomique : {self.atomic_m}")
        print(f"| Famille : {self.family}")
        print(f"| Période : {self.period}")
        print(f"| Nombre de neutrons : {self.neutron}")
        print(f"| Nombre de protons : {self.proton}")
        print(f"| Nombre d'électrons : {self.electron}")
        print(f"| Année de découverte : {self.year}")
        print("")

def __main__():  # def __main__ fonction
    # Declare some atoms and put them in a array
    AtomsList  = []
    CSVfile = open("AtomsDB.csv", "r")
    Lines = CSVfile.readlines()
    for line in Lines:
        ValuesSplitted = line.rstrip(";\n").split(";")
        if len(ValuesSplitted) == 10:
            AtomsList.append(atom(ValuesSplitted))
            # for value in ValuesSplitted:
            #         print(value)
        else: 
            print("Incorrect line")
            print(line)
    WrongInputMessage = "Not found in database - try again"
    while True: 

        InputString = str(input("Nom de l'atome / Numéro atomique / Symbol: ")).upper()
        
        if InputString == "QUIT":
            sys.exit()

        found = False
        for currentAtom in AtomsList:
            if (
                currentAtom.symbol.upper() == InputString 
                or currentAtom.name.upper() == InputString
                or currentAtom.atomic_n.upper() == InputString
            ):
                currentAtom.PrintMe()
                found = True
                break
        if not found:
            print(WrongInputMessage)
        
        


__main__()

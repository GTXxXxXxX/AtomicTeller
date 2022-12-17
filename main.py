import sys  # import module sys
class atom:  # create the class atom
    def __init__(self, splittedLine):   #def the constructor of the class
        self.atom_n = splittedLine[0]
        self.name = splittedLine[1]
        self.symbol = splittedLine[2]
        self.atom_m = splittedLine[3]
        self.neutron = splittedLine[4]
        self.proton = splittedLine[5]
        self.electron = splittedLine[6]
        self.period = splittedLine[7]
        self.group = splittedLine[8]
        self.phase = splittedLine[9]
        self.radioactive = splittedLine[10]
        self.natural = splittedLine[11]
        self.type = splittedLine[12]
        self.elecnegativity = splittedLine[13]
        self.density = splittedLine[14]
        self.discoverer = splittedLine[15]
        self.year = splittedLine[16]
        self.shells = splittedLine[17]

    def PrintMe(self):  # def PrintMe function
        print("")
        print(f"| Symbole chimique : {self.symbol}")
        print(f"| Nom : {self.name}")
        print(f"| Numéro atomique : {self.atom_n}")
        print(f"| Masse atomique : {self.atom_m}")
        print(f"| Famille : {self.type}")
        print(f"| Groupe : {self.group}")
        print(f"| Période : {self.period}")
        print(f"| Nombre de couches électroniques : {self.shells}")
        print(f"| Nombre de neutrons : {self.neutron}")
        print(f"| Nombre de protons : {self.proton}")
        print(f"| Nombre d'électrons : {self.electron}")
        print(f"| Masse volumique (g/cm3) : {self.density}")
        print(f"| Électronégativité : {self.elecnegativity}")
        print(f"| Naturel ? : {self.natural}")
        print(f"| Radioactif ? : {self.radioactive}")
        print(f"| État : {self.phase}")
        print(f"| Découvreur(s) : {self.discoverer}")
        print(f"| Année de découverte : {self.year}")
        print("")

def __main__():  # def __main__ fonction

    AtomsList  = []
    CSVfile = open("PTOFE.csv", "r")
    CSVLines = CSVfile.readlines()
    for line in CSVLines:
        CSVLineSplitted = line.rstrip(";\n").split(";")
        if len(CSVLineSplitted) == 18:
            AtomsList.append(atom(CSVLineSplitted))
        else: 
            print("Incorrect line")
            print(line)
    WrongInputMessage = "Not found in database - try again"
    while True: 

        InputString = str(input("Nom de l'atome / Numéro atomique / Symbole : ")).upper()
        
        if InputString == "QUIT":
            sys.exit()

        found = False
        for currentAtom in AtomsList:
            if (
                currentAtom.symbol.upper() == InputString 
                or currentAtom.name.upper() == InputString
                or currentAtom.atom_n.upper() == InputString
            ):
                currentAtom.PrintMe()
                found = True
                break
        if not found:
            print(WrongInputMessage)
__main__()

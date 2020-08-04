from copy import deepcopy

class Set:
    def __init__(self, data = {}):                         #skup ce da ima samo jedno polje koje je tipa dictionary
        if data is None:                                   #kljuc je link, a vrednost je broj pronadjenih reci
            self.data = {}
        else:
            self.data = deepcopy(data)

    def getData(self):
        return self.data

    def union(self, set2):   #OR operator
        if set2.data is not None:
            for key in set2.data.keys():                   #ukoliko se neki link pojavljuje u oba seta, broj reci se sabira
                if key in self.data.keys():
                    self.data[key] += set2.data[key]
                else:
                    self.data[key] = set2.data[key]

    def section(self, set2): #AND operator
        new_data = {}
        for key in self.data.keys():                       #link mora da bude sadrzan u oba seta, i tada se broj
            if key in set2.data.keys():                    #pronadjenih reci iz oba seta sabiraju
                 new_data[key] = self.data[key] + set2.data[key]
        self.data = new_data

    def complement(self,set2): #NOT operator
        new_data = {}
        for key in self.data.keys():                       #link koji postoji u setu broj 1 ne sme da se nalazi u setu broj 2
            if key not in set2.data.keys():
                new_data[key] = self.data[key]
        self.data = new_data

    def __str__(self):                                     #metoda za prikaz podataka u setu
        string = ""
        for item in self.data.items():
            string += str(item) + '\n'
        return string

    def isEmpty(self):
        if len(self.data) == 0:
            return True
        else:
            return False
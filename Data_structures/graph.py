class cvor():
    def __init__(self,naziv,linkovi):
        self.naziv = naziv                      #Naziv cvora
        self.dolazni = []                       #lista cvorova koji pokazuju na ovaj (odnosno veza(grana) u kojima ovaj cvor predstavlja odrediste)
        self.polazni = linkovi                  #lista cvorova na koje pokazuje ovaj (odnosno veza(grana) u kojima ovaj cvor predstavlja polazni)
                                                #veza je modelirana pomocu ove 2 liste

    def getDolazni(self):
        return self.dolazni

    def getPolazni(self):
        return  self.polazni



class Graf():
    def __init__(self):
        self.cvorovi = {}

    def getCvorovi(self):
        return self.cvorovi

    def dodajCvor(self,naziv,linkovi):
        if naziv not in self.cvorovi.keys():            #ukoliko se cvor vec ne nalazi u grafu dodajemo ga
            self.cvorovi[naziv] = cvor(naziv,linkovi)


    def ispisiGraf(self):
        for cvor in self.cvorovi.keys():
            self.cvorovi[cvor].ispisiCvor()

    def srediLinkove(self):                                         #ova netoda sredjuje veze medju cvorovima grafa
        for pocetni in self.cvorovi.keys():                         #uzimamo cvor iz baze cvorova (pocetni cvor grane)
            for krajni in self.cvorovi[pocetni].polazni:            #prolazimo kroz sve cvorove na koje pokazuje selektvani (otuda krajnji jer se grna zavrsava u njemu)
                if krajni in self.cvorovi.keys():                   #ukoliko se krajni nalazi u bazi cvorova u njegove dolazne dodajemo cvor koji pokazuje na njega (if provera je tu da ne bi doslo do pucanja programa ukoliko ne postoji cvor sa kljucem krajnji u recniku)
                    self.cvorovi[krajni].dolazni.append(pocetni)




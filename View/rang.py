from Data_structures.graph import *
from Data_structures.set import *
from Data_structures.trie import *
from View.sort import *
import traceback



class sortInfo():
    def __init__(self,naziv,vrednost,broj_linkova,pronadjeno_reci,koeficijent_rangiranja = 0):
        self.naziv = naziv                                               #naziv cvora(stranice)
        self.koeficijent = vrednost                                      #koeficijent stranice izracunat rang algoritmmom
        self.broj_ponavljanja = pronadjeno_reci                          #broj ponavljanja trazene reci
        self.broj_linkova = broj_linkova                                 #broj linkova na stranicu
        self.koeficijent_rangiranja = koeficijent_rangiranja             #koeficijent po kome se sortira izracunat kao rang*broj_ponavljanja

#GET i SET metodoe

    def getBrojLinkova(self):
        return self.broj_linkova

    def getNaziv(self):
        return  self.naziv

    def getBrojPonavljanja(self):
        return self.broj_ponavljanja

    def getBroj_ponavljanja(self):
        return self.broj_ponavljanja

    def getKoeficijent(self):
        return self.koeficijent

    def getKoeficijent_rangiranja(self):
        return self.koeficijent_rangiranja

    def setKoeficijent(self,vrednost):
        self.koeficijent = vrednost

    def setBrojPonavljanja(self,vrednost):
        self.broj_ponavljanja = vrednost

    def setKoeficijent_rangiranja(self,vrednost):
        self.koeficijent_rangiranja = vrednost

#----------------------------------------------

def rang(graf,docs):


    trenutna = {}           #trenutna iteracija
    prethodna = {}          #prethodna iteracija tj ona cije vrednosti koristimo za racunanje trenutne

    for kljuc in graf.cvorovi.keys():       #prethodnu iteraciju inicajiluzujemo na 1/broj cvorova kao sto se vidi u prilozenom materijalu
        prethodna[kljuc] = 1/len(graf.cvorovi)  #kljuc je ime cvora kako bi sto lakse pristupili izracunatim vrednostima

    for kljuc in graf.cvorovi.keys():       #trenutnu inicijalizujemo na 0 jer tek treba da dobije vrednost
        trenutna[kljuc] = 0




    for posmatrani in trenutna.keys():      #posmatrani cvor je onaj za koji racunamo rang u datom trenutku
        for posmatrac in trenutna.keys():   #posmatrac predstavlja cvor koji pokazuje na posmatrani odnosno na onaj ciji rang racunamo
            if posmatrani in graf.cvorovi[posmatrac].getPolazni():  #provera da li cvor stvarno pokazuje na posmatrani ukoliko se nalazi u listi dolazni znaci da je posmatrani kraj grane koja ide od posmatraca ka posmatranom
                trenutna[posmatrani] = trenutna[posmatrani] + prethodna[posmatrac]/len(graf.cvorovi[posmatrac].getPolazni())    #trenutna vrednost jednaka je sumi prethodnih vrednosti posmatraca podeljenom sa brojem odlaznih veza iz posmatraca

    #vise o rangu u prilozenom materijalu



    povratnaVrednost = []   #lista koja predstavlja povratnu vrednost funkcije



    for kljuc in graf.cvorovi.keys():   #popunjavamo listu povratnih vrednosti objektima tipa sortInfo koji sadrze potrebne informacije o stranici
        try:
            povratnaVrednost.append(
                sortInfo(kljuc,trenutna[kljuc],len((graf.getCvorovi())[kljuc].getDolazni()),docs.getData()[kljuc],docs.getData()[kljuc]*trenutna[kljuc]))

        except:
                continue




    quick_sort(povratnaVrednost) #pozivamo kvik sort algoritam nad listom povratnih vrednosti koju cemo vratiti koa povratnu vrednost funkcije



    return  povratnaVrednost
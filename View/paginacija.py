from View.rang import *


def paginacija(infoLista):
    poziciija = 0    #pozicija u listi koja se stampa
    ispisano = 0     #broj ispisanih stavki
    print( "==========================================================================================================================================================================================")
    print("Unesite koliko stavki zelite po ispisu:")
    za_ispis = "string"
    while isinstance(za_ispis, str):
        try:
            za_ispis = int(input())         #sa tastature unosimo broj stavki po strani koje zelimo da ispisemo
        except:
            print("Doslo je do greske unesite ponovo:") #zastita ukoliko se unese ne broj vrednost
    print("Vrednost uspešno uneta!")

    izbor = "Nista"

    while izbor != 'X':             #za vrednost X prekidamo ispis

        if izbor == 'N':            #Ponavljace se sve dok ne unesemo validan broj
            za_ispis = "string"
            while isinstance(za_ispis,str): #dok unosimo string kao vrednost while petlja ce se ponavljati
                 try:
                    print("Unesite validnu(brojnu) vrednost:")
                    za_ispis = int(input())
                 except:
                    continue
            print("Vrednost uspešno promenjena!")

        elif izbor == 'W':          #u ovom slucaju ispisujemo n sledecih stavki
            print('{:>4} {:>60} {:>70}  {:>20}  {:>10} {:>40}'.format("REDNI BROJ","ADRESA","KOEFICIJENT","PRONAĐENIH REČI","LINKOVA","KOEFICIJENT RANGIRANJA"))
            if poziciija >= len(infoLista): #ako pozicija  prevazilazi indekse liste ispis je gotov
                print("Kraj ispisa !")
            for ispisano in range (0,za_ispis): #izvrsava se onoliko iteracija koliko zelimo elemenata po strani
                try:    # try catch blok sluzi kao zastita od prevelikog indeksa cim indeks prevazidje broj elemenata ispis se zavrsava
                    print('{:<4} {:<120} {:<30}  {:<10}  {:<30} {:<10}'.format(str(poziciija+1),infoLista[poziciija].getNaziv(),str(infoLista[poziciija].getKoeficijent()),str(infoLista[poziciija].getBrojPonavljanja()),str(infoLista[poziciija].getBrojLinkova()),str(infoLista[poziciija].getKoeficijent_rangiranja()))) #pomnoziti koef sa brojem ponavljanja
                    poziciija = poziciija + 1   #ispisom svakog elementa pomeramo se za jedno mesto u napred
                except:
                    break

        elif izbor == 'S':  #ispis u nazad funkcionise slicno kao i ispis u napred
            print('{:>4} {:>60} {:>70}  {:>20}  {:>10} {:>40}'.format("REDNI BROJ", "ADRESA", "KOEFICIJENT", "PRONAĐENIH REČI","LINKOVA","KOEFICIJENT RANGIRANJA"))
            poziciija = poziciija - 2*za_ispis  #pocetna pozicija ispisa
            if poziciija < 0:
                poziciija = 0
            for ispisano in range(0, za_ispis):
                try:
                    print('{:<4} {:<120} {:<30}  {:<10}  {:<10}'.format(str(poziciija+1),infoLista[poziciija].getNaziv(),str(infoLista[poziciija].getKoeficijent()),str(infoLista[poziciija].getBrojPonavljanja()),str(infoLista[poziciija].getBrojLinkova()),str(infoLista[poziciija].getKoeficijent_rangiranja()))) #pomnoziti koef sa brojem ponavljanja
                    poziciija = poziciija + 1
                except:
                    break

        elif izbor != 'S' and izbor != 'W' and izbor != 'N' and izbor != "Nista":
            print("Uneti izbor je nepostojeći unesite ponovo (velikim slovom)!")

        print("=========================================================================================================================================================================================")
        print("||:...:::...:::...:::...:::...:::...:::...:::...:::...:::....:::...:::...:::IZABERITE OPCIJU:::...:::...:::...:::...:::...:::...:::...:::...:::...:::...:::...:::...:::...:::...:::...:||")
        print("||                                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^                                                    ||")
        print("||                                        Listaj napred...........................................................................W                                                    ||")
        print("||                                        Listaj nazad............................................................................S                                                    ||")
        print("||                                        Za promenu broja stavki po ispisu.......................................................N                                                    ||")
        print("||                                        Za izlaz................................................................................X                                                    ||")
        print("||                                        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^                                                    ||")
        print("||###################################################################### Koristite velika slova! ######################################################################################||")
        print("=========================================================================================================================================================================================")
        izbor = input()
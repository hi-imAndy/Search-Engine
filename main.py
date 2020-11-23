from Parse.parse import *
from Parse.parse_query import *
from View.rang import *
from View.paginacija import *
from Parse.parse import *
from Parse.parse_query import *

if __name__ == "__main__":
    while True:
        try:
            file_path = input("Unesite punu putanju(full path) do direktorijuma za pretragu:")
            parse_docs(file_path)
            break
        except:
	    traceback.print_exc();
            print("Putanju koju ste uneli nije validna!")
    query = input("Unesite upit(Opcione kljucne reci: AND, OR, NOT; Izlaz: x):")
    while query != "x":
        try:
            docs = parse_query(query)
            if docs is None or docs.isEmpty():
                print("Nisu pronadjene reci sa datim upitom!")
            else:
                paginacija(rang(graf,docs))
        except:
            traceback.print_exc();
            print("Greska! Nisu pronadjene reci sa datim upitom!")
        query = input("Unesite upit(Opcione kljucne reci: AND, OR, NOT; Izlaz: x):")







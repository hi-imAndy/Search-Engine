from Data_structures.set import *
from Parse.parse import *

def parse_query(query):                 #metoda koja parsira korisnikov upit
    words = query.split()
    for i in range(len(words)):         #da bismo obezbedili da upit bude key insensitive, pretvaramo sva slova u mala
        words[i] = words[i].lower()
    set1 = Set(trie.find_word(words[0]))        #pravimo skup koji sadrzi prvu rec
    if words.__len__() == 1:
        return set1
    elif words[1] == "or":                      #u slucajevima kada su ispravno koristeni neki od logickih operatora,
        if words.__len__() != 3:                #pravimo skup od 3. reci upita
            print("GRESKA! Greska pri upotrebi logickog operatora!")
            return None
        set2 = Set(trie.find_word(words[2]))                #na osnovu logickog operatora koristimo metode seta:
        set1.union(set2)                                    #union, section, complement
    elif words[1] == "and":
        if words.__len__() != 3:
            print("GRESKA! Greska pri upotrebi logickog operatora!")
            return None
        set2 = Set(trie.find_word(words[2]))
        set1.section(set2)
    elif words[1] == "not":
        if words.__len__() != 3:
            print("GRESKA! Greska pri upotrebi logickog operatora!")
            return None
        set2 = Set(trie.find_word(words[2]))
        set1.complement(set2)
    else:                                       #slucaj kada je uneseno vise od 1 reci, a nije koristen logicki operator
        for word in words[1:]:
            set2 = Set(trie.find_word(word))
            set1.union(set2)
    return set1


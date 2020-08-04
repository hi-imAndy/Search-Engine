class TrieNode:                                           #cvor Trie stabla
    def __init__(self, letter):
        self.letter = letter                              #polje koje predstavlja jedno slovo
        self.children = {}                                #svaki cvor moze da ima decu(dictionary), a pri inicijalizaciji ih nema
        self.docs = {}                                    #dictionary kod koga je key dokument koji sadrzi neku rec, a value je broj
                                                          # tih reci u tom dokumentu

class Trie:                                               #Trie stablo
    def __init__(self):                                   #u konstruktoru kreiramo samo koren koji nece sadrzati slova vec samo decu
        self.root = TrieNode("*")

    def add_word(self, word, doc):                        #metoda kojom dodajemo rec u stablo
        node = self.root                                  #krecemo od korena stabla i obilazimo ga preko njegove dece
        for letter in word:                               #ako ne postoji slovo u potomcima, kreiramo novi cvor sa tim slovom
            if letter not in node.children:
                node.children[letter] = TrieNode(letter)
            node = node.children[letter]
        if doc not in node.docs.keys():                   #na kraju reci dodajemo dokument koji je sadrzi u dictionary docs
            node.docs[doc] = 1                            #ako se red dodaje prvi put postavlja se value na 1, inace dodajemo +1 za taj dokument
        else:
            node.docs[doc] += 1

    def find_word(self, word):                            #metoda koja pretrazuje zadatu rec u stablu, ako postoji, vraca dokumente koji je sadrze
        node = self.root                                  #slicno kao kod dodavanja, krecemo od korena i obilazimo decu
        for letter in word:
            if letter not in node.children:
                return None
            node = node.children[letter]
        return node.docs                                  #ako smo uspesno stigli do kraja reci, vracamo njegove dokumente
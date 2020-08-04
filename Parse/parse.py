from Data_structures.trie import *
from Parse.parser import *
from Data_structures.graph import *

graf = Graf()
trie = Trie()

def parse_docs(path):                               #rekurzivna funkcija koja poziva sebe ako je dati fajl direktorijum,a parsira ga ako je to HTML dokument
    file_names = os.listdir(path)                   #metodom os.listdir(path) dobijamo listu naziva fajlova koji se nalaze na zadatoj putanji
    for fileName in file_names:                     #prolazimo kroz sve fajlove u trenutnom direktorijumu
        full_path = os.path.join(path, fileName)    #konkatencija pune putanje i naziva fajla
        if os.path.isdir(full_path):                #ako je fajl direktorijum, parsiramo njegove poddirektorijume i podfajlove
            parse_docs(full_path)
        if full_path.endswith('.html'):
            parser = Parser()
            links, words = parser.parse(full_path)  #parser vraca sve linkove i reci zadatog dokumenta
            lower_words = []
            for word in words:
                lower_words.append(word.lower())    #pretvaramo sve reci da budu malim slovima i tako ih smestamo u stablo
                graf.dodajCvor(full_path, links)    #dodajemo cvorove u graf
            for word in lower_words:
                trie.add_word(word, full_path)
    graf.srediLinkove()

import nltk

def Rec_Des_Parser(grammar, sentence):
    parser = nltk.parse.RecursiveDescentParser(grammar)
    for word in sentence:
        temp = nltk.word_tokenize(word)
        for tree in parser.parse(temp):
            print(tree)
            tree.draw()


grammar=nltk.CFG.fromstring("""
 S  -> NP VP
  NP -> Det N |Det Nom | Det N PP
  Nom ->  Adj N | Adj Nom
  VP -> V | V NP | V NP PP
  PP -> P NP|P Nom
  Det -> 'the' | 'a'
  N -> 'dog' |'cat' | 'girl' |'hair'|'dogs'   
  Adj  -> 'fierce' | 'long' |  'little' | 'tall' |'black' |'three'
  V ->  'saw' |'chased'  |  'slept' | 'barked' 
  P -> 'with'|'on'
""")

sentence = ["the fierce dog saw a cat","the girl with long hair slept","the three tall black dogs barked"]
Rec_Des_Parser(grammar, sentence)

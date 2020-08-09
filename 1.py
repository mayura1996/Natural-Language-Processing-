import nltk

def Rec_Des_Parser(grammar, sentence):
    parser = nltk.parse.RecursiveDescentParser(grammar)
    for word in sentence:
        temp = nltk.word_tokenize(word)
        for tree in parser.parse(temp):
            print(tree)
            tree.draw()


grammar = nltk.CFG.fromstring("""
 S -> NP VP
 PP -> P NP
 NP -> D N
 VP -> V| V NP |V NP PP
 D -> 'a' | 'the'
 N -> 'boy' | 'dog'
 V -> 'chased'
 P -> 

""")

sentence = ["the boy chased a dog"]
Rec_Des_Parser(grammar, sentence)

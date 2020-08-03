class PorterStemmer:
    def __init__(self):
        self.vowels= ('a', 'e', 'i', 'o', 'u') #defining the vowel letters

    def consonantCheck(self, word: str, i: int):
        return not self.vowelCheck(word, i)

    def vowelCheck(self, word: str, i: int):
        if word[i].lower() in self.vowels:
            return True
        elif word[i].lower() == 'y': #"y" preceded by a consonant
            if self.consonantCheck(word, i-1):
                return True
            else:
                return False

    def m_value(self, word):  #determing the count of VC combinations
        i = 0
        m = 0
        while i < len(word)-1:
            if self.vowelCheck(word, i) and self.consonantCheck(word, i+1):
                m += 1
                i += 2
            else:
                i += 1
        return m

    def checking_for_vowel(self, word): #checking whether there is a vowel available
        for v in self.vowels:
            if v in word:
                return True

        for i in range(len(word)):
            if word[i] == 'y':
                if self.vowelCheck(word, i):
                    return True

        return False

    def double_consonent_ending(self, word):  #checking whether the word is ending with double consonents
        if word[-2].lower() == word[-1].lower():
            if self.consonantCheck(word, -1):
                return True

        return False

    def CVC_ending(self, word):  #checking whether the word is ending with CVC
        if self.consonantCheck(word, -1):
            if self.vowelCheck(word, -2):
                if self.consonantCheck(word, -3):
                    if word[-1] not in ('w', 'x', 'y'):
                        return True

        return False

    #algorithm for the checking of the suffixes
    
    def step1a(self, word):  
        if word[-4:].lower() == 'sses':
            word= word[:-4] + 'ss'
        elif word[-3:].lower() == "ies":
            word= word[:-3] + "i"
        elif word[-2:].lower() == "ss":
            pass
        elif word[-1].lower() == "s":
            word= word[:-1]
        return word

    def step1b(self, word):
        if word[-3:].lower() == 'eed':
            m = self.m_value(word[:-3])
            if m > 0:
                word= word[:-1]
        elif word[-2:].lower() == 'ed':
            if self.checking_for_vowel(word[:-2]):
                word= word[:-2]
                word= self.step1ba(word)
        elif word[-3:].lower() == 'ing':
            if self.checking_for_vowel(word[:-3]):
                word= word[:-3]
                word= self.step1ba(word)

        return word

    def step1ba(self, word):
        if word[-2:].lower() == 'at':
            word= s + 'e'
        elif word[-2:].lower() == 'bl':
            word= s + 'e'
        elif word[-2:].lower() == 'iz':
            word= s + 'e'
        elif self.double_consonent_ending(word) and word[-1].lower() not in ('l', 's', 'z'):
            word= word[:-1]
        elif self.m_value(word) == 1 and self.CVC_ending(word):
            word += 'e'

        return word

    def step1c(self, word):
        if word[-1].lower() == 'y':
            if self.checking_for_vowel(word[:-1]):
                word= word[:-1] + 'i'

        return word

    def step5a(self, word):
        if word[-1].lower() == 'e':
            m = self.m_value(word[:-1])
            if m > 1:
                word= word[:-1]
            elif m == 1 and not self.CVC_ending(word[:-1]):
                word= word[:-1]

        return word

    def step5b(self, word):
        m = self.m_value(word)
        if m > 1 and self.double_consonent_ending(word) and word[-1].lower() == 'l':
            word= word[:-1]

        return word

    def step2(self, word):
        if word[-7:] == 'ational':
            m = self.m_value(word[:-7])
            if m > 0:
                word= word[:-5]+"e"
        elif word[-6:] == 'tional':
            m = self.m_value(word[:-6])
            if m > 0:
                word= word[:-2]
        elif word[-4:] == 'enci':
            m = self.m_value(word[:-4])
            if m > 0:
                word= word[:-1]+"e"
        elif word[-4:] == 'anci':
            m = self.m_value(word[:-4])
            if m > 0:
                word= word[:-1]+"e"
        elif word[-4:] == 'izer':
            m = self.m_value(word[:-4])
            if m > 0:
                word= word[:-1]
        elif word[-4:] == 'abli':
            m = self.m_value(word[:-4])
            if m > 0:
                word= word[:-1]+"e"
        elif word[-4:] == 'alli':
            m = self.m_value(word[:-1])
            if m > 0:
                word= word[:-2]
        elif word[-5:] == 'entli':
            m = self.m_value(word[:-5])
            if m > 0:
                word= word[:-2]
        elif word[-3:] == 'eli':
            m = self.m_value(word[:-3])
            if m > 0:
                word= word[:-2]
        elif word[-5:] == 'ousli':
            m = self.m_value(word[:-5])
            if m > 0:
                word= word[:-2]
        elif word[-7:] == 'ization':
            m = self.m_value(word[:-7])
            if m > 0:
                word= word[:-5]+"e"
        elif word[-5:] == 'ation':
            m = self.m_value(word[:-5])
            if m > 0:
                word= word[:-3]+"e"
        elif word[-4:] == 'ator':
            m = self.m_value(word[:-4])
            if m > 0:
                word= word[:-2]+"e"
        elif word[-5:] == 'alism':
            m = self.m_value(word[:-5])
            if m > 0:
                word= word[:-3]
        elif word[-7:] == 'iveness':
            m = self.m_value(word[:-7])
            if m > 0:
                word= word[:-4]
        elif word[-7:] == 'fulness':
            m = self.m_value(word[:-7])
            if m > 0:
                word= word[:-4]
        elif word[-7:] == 'ousness':
            m = self.m_value(word[:-7])
            if m > 0:
                word= word[:-4]
        elif word[-5:] == 'aliti':
            m = self.m_value(word[:-5])
            if m > 0:
                word= word[:-3]
        elif word[-5:] == 'iviti':
            m = self.m_value(word[:-5])
            if m > 0:
                word= word[:-3]+"e"
        elif word[-6:] == 'bliti':
            m = self.m_value(word[:-6])
            if m > 0:
                word= word[:-3]+"e"

        return word


    def step3(self, word):
        if word[-5:] == 'icate':
            m = self.m_value(word[:-5])
            if m > 0:
                word= word[:-3]
        elif word[-5:] == 'ative':
            m = self.m_value(word[:-5])
            if m > 0:
                word= word[:-5]
        elif word[-5:] == 'alize':
            m = self.m_value(word[:-5])
            if m > 0:
                word= word[:-3]
        elif word[-5:] == 'iciti':
            m = self.m_value(word[:-5])
            if m > 0:
                word= word[:-3]
        elif word[-4:] == 'ical':
            m = self.m_value(word[:-4])
            if m > 0:
                word= word[:-2]
        elif word[-3:] == 'ful':
            m = self.m_value(word[:-3])
            if m > 0:
                word= word[:-3]
        elif word[-4:] == 'ness':
            m = self.m_value(word[:-4])
            if m > 0:
                word= word[:-4]

        return word


    def step4(self, word):
        if word[-2:] == 'al':
            m = self.m_value(word[:-2])
            if m > 1:
                word= word[:-2]
        elif word[-4:] == 'ance':
            m = self.m_value(word[:-4])
            if m > 1:
                word= word[:-4]
        elif word[-4:] == 'ence':
            m = self.m_value(word[:-4])
            if m > 1:
                word= word[:-4]
        elif word[-2:] == 'er':
            m = self.m_value(word[:-2])
            if m > 1:
                word= word[:-2]
        elif word[-2:] == 'ic':
            m = self.m_value(word[:-2])
            if m > 1:
                word= word[:-2]
        elif word[-4:] == 'able':
            m = self.m_value(word[:-4])
            if m > 1:
                word= word[:-4]
        elif word[-4:] == 'ible':
            m = self.m_value(word[:-4])
            if m > 1:
                word= word[:-4]
        elif word[-3:] == 'ant':
            m = self.m_value(word[:-3])
            if m > 1:
                word= word[:-3]
        elif word[-5:] == 'ement':
            m = self.m_value(word[:-5])
            if m > 1:
                word= word[:-5]
        elif word[-4:] == 'ment':
            m = self.m_value(word[:-4])
            if m > 1:
                word= word[:-4]
        elif word[-3:] == 'ent':
            m = self.m_value(word[:-3])
            if m > 1:
                word= word[:-3]
        elif word[-3:] == 'ion':
            m = self.m_value(word[:-3])
            if m > 1 and (word[-4]== "s" or word[-4]=="t"):
                word= word[:-3]
        elif word[-2:] == 'ou':
            m = self.m_value(word[:-2])
            if m > 1:
                word= word[:-2]
        elif word[-3:] == 'ism':
            m = self.m_value(word[:-3])
            if m > 1:
                word= word[:-3]
        elif word[-3:] == 'ate':
            m = self.m_value(word[:-3])
            if m > 1:
                word= word[:-3]
        elif word[-3:] == 'iti':
            m = self.m_value(word[:-3])
            if m > 1:
                word= word[:-3]
        elif word[-3:] == 'ous':
            m = self.m_value(word[:-3])
            if m > 1:
                word= word[:-3]
        elif word[-3:] == 'ive':
            m = self.m_value(word[:-3])
            if m > 1:
                word= word[:-3]
        elif word[-3:] == 'ize':
            m = self.m_value(word[:-3])
            if m > 1:
                word= word[:-3]

        return word

    def __call__(self, s: str):
        word= s.strip()
        word=s.lower()
        word= self.step1a(word)
        word= self.step1b(word)
        word= self.step1c(word)
        word= self.step2(word)
        word= self.step3(word)
        word= self.step4(word)
        word= self.step5a(word)
        word= self.step5b(word)
        return word
    
if __name__ == '__main__':
    stemmer = PorterStemmer()
    words = ["connect", "connecting", "connection","connects","connected"]
    for i in words:
        print(i,"=>",stemmer(i),sep="\t")


    print("\nPRESS ENTER TO EXIT")
    while True:
        inputWord = (input("\n\nInput another word to find the stem : "))
        if not inputWord:
            break
        print("The stem of the "+inputWord+" is => " + stemmer(inputWord))
    
    
 

        
   
   

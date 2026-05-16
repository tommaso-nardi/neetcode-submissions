class WordDictionary:

    def __init__(self):
        self.dizionario=[]

    def addWord(self, word: str) -> None:
        self.dizionario.append(word)

    def search(self, word: str) -> bool:
        i=0
        for parola in self.dizionario:
            if len(parola) != len(word):
                continue
            
            check = True

            for i in range(len(word)):
                if word[i] != '.' and word[i] != parola[i]:
                    check=False
                    break
            if check == True:
                return True
        return False

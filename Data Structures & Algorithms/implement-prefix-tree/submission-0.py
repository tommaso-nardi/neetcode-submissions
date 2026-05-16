class PrefixTree:

    def __init__(self):
        self.albero=[]

    def insert(self, word: str) -> None:
        self.albero.append(word)

    def search(self, word: str) -> bool:
        return (word in self.albero)

    def startsWith(self, prefix: str) -> bool:
        lun = len(prefix)
        for word in self.albero:
            if word[:lun] == prefix:
                return True
        return False
        
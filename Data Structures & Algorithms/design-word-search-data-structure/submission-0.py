class TrieNode:
    def __init__(self):
        self.children={}
        self.word=False

class WordDictionary:

    def __init__(self):
        self.albero=TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.albero
        for c in word:
            if c not in cur.children:
                cur.children[c]=TrieNode()
            cur = cur.children[c]
        cur.word=True

    def search(self, word: str) -> bool:
        def ricorsione(j, root):
            cur=root
            for i in range(j,len(word)):
                c=word[i]

                if c == '.':
                    for lettera in cur.children.values():
                        if ricorsione(i+1,lettera):
                            return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur=cur.children[c]
            return cur.word
        return ricorsione(0,self.albero)


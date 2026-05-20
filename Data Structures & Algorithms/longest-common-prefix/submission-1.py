class TrieNode:
    def __init__(self):
        self.children={}
        self.word=None

class Solution:
    #personalmente mi piace perchè usa i trie. Per ogni parola creaci l'albero...
    def longestCommonPrefix(self, strs: List[str]) -> str:
        root=TrieNode()
        parola=""
        for w in strs:
            cur = root
            for c in w:
                if c not in cur.children:
                    cur.children[c] = TrieNode()
                cur = cur.children[c]
            cur.word = w
        
        cur=root
        #Poi finchè abbiamo un solo children e non abbiamo finito una qualunque parola tra quelle
        #in input allora scendiamo. Perchè se abbiamo 2+ figli allora significa che non è più
        #prefisso comune
        while len(cur.children)==1 and cur.word==None:
            lettera = list(cur.children.keys())[0]
            parola += lettera
            cur = cur.children[lettera]
        return parola
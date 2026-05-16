class TrieNode:
    def __init__(self):
        self.children={}
        self.word=False

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        visti={}
        root=TrieNode()
        for w in wordDict:
            cur = root
            for c in w:
                if c not in cur.children:
                    cur.children[c] = TrieNode()
                cur = cur.children[c]
            cur.word = True

        def ricorsione(i):
            if i==len(s):
                return True
            if i in visti:
                return visti[i]
            #Salva la lettera attuale individuata e settala come nodo da esaminare
            cur=root
            for j in range(i, len(s)):
                char = s[j]
                if char not in cur.children:
                    break # Non ci sono più parole nel Trie con questo prefisso
                
                cur = cur.children[char]
                if cur.word:
                    # Se abbiamo trovato una parola, proviamo a risolvere il RESTO della stringa
                    if ricorsione(j + 1):
                        visti[i] = True
                        return True
            
            visti[i] = False
            return False
        
        return ricorsione(0)
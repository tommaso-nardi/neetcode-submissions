class TrieNode:
    def __init__(self):
        self.children={}
        self.word=False

class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        root=TrieNode()
        visti={}
        for w in dictionary:
            cur = root
            for c in w:
                if c not in cur.children:
                    cur.children[c] = TrieNode()
                cur = cur.children[c]
            cur.word = w
        

        def ricorsione(i):
            if i in visti:
                return visti[i]
            if i == len(s):
                return 0
            
            cur=root

            
            


            r1=1+ricorsione(i+1)
            r2=float("inf")
            for j in range(i,len(s)):
                if s[j] not in cur.children:
                    break
                else:
                    cur = cur.children[s[j]]
                if cur.word:
                    temp=ricorsione(j+1)
                    r2=min(r2,temp)
            
            ris = min(r1,r2)
            visti[i] = ris
            return ris

        return ricorsione(0)
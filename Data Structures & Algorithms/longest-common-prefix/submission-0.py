class TrieNode:
    def __init__(self):
        self.children={}
        self.word=None

class Solution:
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
        while len(cur.children)==1 and cur.word==None:
            lettera = list(cur.children.keys())[0]
            parola += lettera
            cur = cur.children[lettera]
        return parola
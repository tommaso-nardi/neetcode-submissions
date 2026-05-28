class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        tabella={}
        for w in words:
            for i in w:
                if i not in tabella:
                    tabella[i]=1
                else:
                    tabella[i]+=1
        
        for lettera in tabella.keys():
            if tabella[lettera]%len(words) != 0:
                return False
        return True
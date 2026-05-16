class Solution:
    def ispali(self,stringa,i,j):
        while i<j:
            if stringa[i]!=stringa[j]:
                return False
            i+=1
            j-=1
        return True

    def partition(self, s: str) -> List[List[str]]:
        ris=[]
        attuale=[]

        def ricorsione(i):
            if i >= len(s):
                ris.append(attuale.copy())
                return
            for j in range(i,len(s)):
                if self.ispali(s,i,j):
                    attuale.append(s[i:j+1])
                    ricorsione(j+1)
                    attuale.pop()

        ricorsione(0)
        return ris
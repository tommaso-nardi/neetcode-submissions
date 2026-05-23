class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        #Soluzione che scorre 's' senza splittare, O(1) in memoria perchè non chiedo nuove cose
        attuale=[]
        mappaturapattern={}
        mappaturas={}
        contparole=0
        i=0

        for j in range(len(s)):
            if i >= len(pattern):
                return False
            if s[j]!=" " or j == len(s)-1:
                attuale.append(s[j])
            if s[j]==" " or j==len(s)-1:
                if not attuale:
                    continue
                
                parola=" ".join(attuale)
                lettera=pattern[i]

                if lettera not in mappaturapattern:
                    if parola in mappaturas:
                        return False
                    mappaturapattern[lettera] = parola
                    mappaturas[parola] = lettera

                if mappaturapattern[lettera] != parola:
                    return False

                attuale=[]
                i=i+1
        
        return i==len(pattern)
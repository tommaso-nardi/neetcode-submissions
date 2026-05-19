class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n==1:
            return 1
        
        sifida={}
        contfida=[0] * (n+1)
        
        for i in range(len(trust)):
            #Se qualcuno (0) si fida di qualcun altro (1), allora marcalo (0) in sifida
            if trust[i][0] not in sifida:
                sifida[trust[i][0]] = 1
            #E aggiungi 1 al contatore di quante persone si fidano di quella persona (1)
            contfida[trust[i][1]] += 1
        #Se qualcuno non si fida di nessuno e tutti si fidano di lui (grazie al cont)
        #allora quel qualcuno è il giudice
        for i in range(1,n+1):
            if i not in sifida:
                if contfida[i] == n-1:
                    return i
        else: return -1
        
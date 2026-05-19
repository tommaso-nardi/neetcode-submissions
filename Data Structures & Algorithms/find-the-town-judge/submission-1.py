class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        if n==1:
            return 1
        
        sifida={}
        contfida=[0] * (n+1)
        for i in range(len(trust)):
            if trust[i][0] not in sifida:
                sifida[trust[i][0]] = 1
            contfida[trust[i][1]] += 1
        for i in range(1,n+1):
            if i not in sifida:
                if contfida[i] == n-1:
                    return i
        else: return -1
        
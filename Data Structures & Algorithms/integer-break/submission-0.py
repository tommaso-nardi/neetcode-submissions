class Solution:
    def integerBreak(self, n: int) -> int:
        visti = {}

        def ricorsione(a):
            if a==1:
                return 1
            if a in visti:
                return visti[a]
            
            massimo=0
            for i in range(1,a):
                attuale=i*max((a-i),ricorsione(a-i))
                massimo=max(massimo,attuale)
            
            visti[a]=massimo
            return massimo
        
        return ricorsione(n)
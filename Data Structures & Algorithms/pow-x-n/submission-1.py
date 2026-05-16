class Solution:
    def myPow(self, x: float, n: int) -> float:
        ris=x
        if n==0:
            return 1
        
        for i in range(1,abs(n)):
            ris=ris*x




        if n<0:
            ris=1/ris
        return ris
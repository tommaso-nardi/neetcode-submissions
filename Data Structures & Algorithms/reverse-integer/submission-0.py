class Solution:
    def reverse(self, x: int) -> int:
        i = 10
        ris=0
        isNeg=False
        if x<0:
            isNeg=True
        x=abs(x)
        while x!=0:
            numero=x%i
            ris=ris*10+(x%i)
            x=x//10
        if not (-2**31) < ris < (2**31-1):
            return 0
        if not isNeg:
            return ris
        else:
            return -ris
        
class Solution:
    def hammingWeight(self, n: int) -> int:
        ris = 0
        while n > 0:
            if (1 & n)  == 1:
                ris=ris+1
            n= n >> 1
        return ris
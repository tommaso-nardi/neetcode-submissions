class Solution:
    def isHappy(self, n: int) -> bool:
        dictt = {}

        while True:
            totale=0
            i=0
            while n!=0:
                cifra = n%10
                totale = totale + (cifra*cifra)
                n = n//10
            if totale in dictt:
                return False
            if totale == 1:
                return True
            dictt[totale] = totale
            n=totale
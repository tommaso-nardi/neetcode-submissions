#Soluzione troppo profonda

class Solution:
    def numSquares(self, n: int) -> int:
        visti={}
        sys.setrecursionlimit(100000)
        
        def ricorsione(num):
            if num == 0:
                return 0
            if num in visti:
                return visti[num]

            minimo = float("inf")
            i=1
            #Per ogni possibile qudrato vedi il minimo necessario se scendi
            while i*i <= num:
                minimo=min(minimo,(1+ricorsione(num-(i*i))))
                i=i+1
            visti[num] = minimo
            return minimo
        
        return ricorsione(n)

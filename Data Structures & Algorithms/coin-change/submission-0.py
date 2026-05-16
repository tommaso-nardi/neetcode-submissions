class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        visti={}

        def ricorsione(x):
            if x==0:
                return 0
            if x<0:
                return -1
            if x in visti:
                return visti[x]
            numero=float("inf")
            for moneta in coins:
                risultato=ricorsione(x-moneta)
                if risultato!=-1:
                    numero = min(numero,risultato+1)
            if numero==float("inf"):
                visti[x]=-1
            else:
                visti[x]=numero
            return visti[x]
        
        return ricorsione(amount)

            
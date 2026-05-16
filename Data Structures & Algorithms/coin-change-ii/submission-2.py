class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        visti={}

        def ricorsione(x,moneta):
            totale=0
            if x==0:
                return 1
            if x<0:
                return 0
            if (x,moneta) in visti:
                return visti[(x,moneta)]
            
            totale=totale+ricorsione(x-coins[moneta],moneta)
            if moneta!=len(coins)-1:
                totale=totale+ricorsione(x,moneta+1)

            visti[(x,moneta)]=totale
            return visti[(x,moneta)]
        
        return ricorsione(amount,0)
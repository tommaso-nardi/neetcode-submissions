class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        visti={}


        def ricorsione(x,moneta):
            totale=0
            #Se manca niente allora 1
            if x==0:
                return 1
            #Se sforiamo allora 0
            if x<0:
                return 0
            #Se è un resto che già abbiamo esplorato allora returna quanto già calcolato
            if (x,moneta) in visti:
                return visti[(x,moneta)]
            numero=float("inf")
            #Per ogni moneta possibile, vedi il minimo di monete per cambiare il resto restante se togliamo
            #il valore di quella esatta moneta
            totale=totale+ricorsione(x-coins[moneta],moneta)
            if moneta!=len(coins)-1:
                totale=totale+ricorsione(x,moneta+1)


            visti[(x,moneta)]=totale
            return visti[(x,moneta)]
        


        return ricorsione(amount,0)
class Solution:
    def integerBreak(self, n: int) -> int:
        visti = {}

        def ricorsione(a):
            #Se siamo ad 1, allora ritorna 1
            if a==1:
                return 1
            #Se già sappiamo il massimo che si ottiene da a, ritorna quanto salvato
            if a in visti:
                return visti[a]
            
            massimo=0
            #Per ogni valore fino ad a (cioè il pezzo che stiamo vedendo ora)
            for i in range(1,a):
                #Vedi se conviene di più considerare questo a-i o il massimo ricorrendo a ritroso a-i
                attuale=i*max((a-i),ricorsione(a-i))
                #Vedi se conviene di più questo a-i o quello massimo già salvato
                massimo=max(massimo,attuale)
            
            visti[a]=massimo
            return massimo
        
        return ricorsione(n)
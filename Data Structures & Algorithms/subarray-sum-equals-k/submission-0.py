class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        visti={0: 1}
        sommaattuale=0
        totale=0

        # Per ogni valore
        for val in nums:
            #Aggiungi alla somma attuale totale
            sommaattuale = sommaattuale+val
            #Salva la somma da cercare a ritroso
            cerca=sommaattuale-k

            #Se c'è allora vuol dire che c'è un valore complessivo attuale in visti, aggiungilo a totale
            if cerca in visti:
                totale=totale+visti[cerca]

            #Se la somma attuale è già stata vista allora aggiungi +1, significa che c'è
            #un altra istanza di subarray che da questo valore, quindi sono +2 in una botta, per esempio
            if sommaattuale in visti:
                visti[sommaattuale] = visti[sommaattuale]+1
            else:
                visti[sommaattuale] = 1
        return totale

            
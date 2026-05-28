class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k==0 or n>=k+maxPts:
            return 1.0
        #Un pò difficile, inizializziamo l'inizializzabile
        somma_finestra=1.0
        prob=[0.0]*(n+1)
        prob[0]=1.0
        #Poi per ogni numero che possiamo prendere calcoliamo la probabilità
        #a ritroso basandoci su tutte le precedenti valide con la nostra window "immaginaria"
        for i in range(1,n+1):
            prob[i] = somma_finestra / maxPts

            #Se il punteggio ci permette ancora di pescare (punteggio minore del massimo giocabile)
            if i<k:
                somma_finestra+=prob[i]
            
            #Sfrattiamo il punteggio che è appena diventato troppo lontano (scaduto oltre maxPts, ai fini della window).
            #Lo sottraiamo SOLO se a suo tempo era minore di k, cioè se era davvero entrato nella finestra.
            if i-maxPts>= 0 and (i-maxPts)<k:
                somma_finestra-=prob[i-maxPts]

        return sum(prob[k:n+1])
class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        
        visti={}

        def ricorsione(i,m):
            #Se già sappiamo il massimo che si prende da qui, prendilo
            if (i,m) in visti:
                return visti[(i,m)]
            #Se abbiamo sforato lascia stare
            if i>=len(piles):
                return 0

            #Inizializzazioni variabili per i calcoli
            totale_rimasto=0
            punteggio=float("-inf")
            massimo=float("-inf")

            #Vedi il massimo che manca
            for j in range(i,len(piles)):
                totale_rimasto = totale_rimasto+piles[j]
            
            #Vedi per tutto quello che puoi ancora fare...
            for x in range (1,min(2*m,len(piles)-i)+1):
                #Quanto guadagni se fai prendere a Bob partendo da i+(un certo indice x)
                #Praticamente facciamo partire Bob da i+x con range M aggiornato
                punteggio=totale_rimasto-ricorsione(i+x,max(m,x))
                #Trova la combinazione ottimale giocando sempre al meglio
                massimo = max(massimo, punteggio)

            visti[(i,m)] = massimo
            return massimo

        return ricorsione(0,1)
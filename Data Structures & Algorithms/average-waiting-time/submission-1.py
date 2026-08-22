class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        tempoatt=0
        attesetot=0

        #Semplice problema di attesa
        for arrivo,tempo in customers:
            #Se non c'è nessuno allora il tempo di fine sarà arrivo+tempoproduzione
            #altrimenti si aspetta che lo chef si libera e allora sarà tempoatt+tempoproduzione
            fine=max(tempoatt,arrivo)+tempo
            attesetot+=fine-arrivo
            tempoatt=fine
        
        return attesetot/len(customers)
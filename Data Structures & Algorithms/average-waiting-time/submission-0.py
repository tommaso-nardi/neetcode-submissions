class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        tempoatt=0
        attesetot=0

        for arrivo,tempo in customers:
            fine=max(tempoatt,arrivo)+tempo
            attesetot+=fine-arrivo
            tempoatt=fine
        
        return attesetot/len(customers)
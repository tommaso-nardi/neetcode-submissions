class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        #L'idea è che se salviamo in una coda semplicemente le posizioni...
        radiant=collections.deque()
        dire=collections.deque()
        for i in range(len(senate)):
            if senate[i] == "R":
                radiant.append(i)
            else:
                dire.append(i)
        
        #Poi qui vediamo chi viene prima di Radiant e Dire secondo gli id, quello che vince
        #si salva in posizione originale + len(senate) per indicare il prossimo giro
        while radiant and dire:
            senrad = radiant.popleft()
            sendir = dire.popleft()
            if senrad < sendir:
                radiant.append(senrad+len(senate))
            else:
                dire.append(sendir+len(senate))
        
        if radiant:
            return "Radiant"
        return "Dire"
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        frequenze={}
        mosse=0

        for x in nums:
            if x not in frequenze:
                frequenze[x] = 0
            frequenze[x] += 1

        #Problema matematico
        for numero, frequenza in frequenze.items():
            #Se la frequenza è già divisibile per 3 allora abbiamo già il numero di sue mosse
            #cioè frequenza/3
            if frequenza%3==0:
                mosse+=frequenza//3
                continue
            
            #Se la frequenza è divisible per 2 invece vuol dire che facciamo tutte le possibili
            #mosse /3 e poi aggiungiamo il +2 finale
            if frequenza%3==2:
                mosse+=frequenza//3+1
                continue
            
            #Se la frequenza è 1...
            if frequenza%3==1:
                #e non sono almeno 4, quindi è 1 e basta, è impossibile
                if frequenza<4:
                    return -1
                #Altrimenti matematicamente il numero di mosse è il numero massimo di mosse
                #fattibili con 3 (che non ci portino ad 1, per questo frequenza-3) e poi si aggiungono le
                #due mosse da 2 finali (quindi 4 è 2+2)
                mosse+=(frequenza-3)//3+2

        return mosse
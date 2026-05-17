class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        #Se le grandezze non vanno bene falso a prescindere
        if len(s1)+len(s2) != len(s3):
            return False
        
        visti = {}

        def ricorsione(i,j):
            #Se siamo alla fine di entrambi vuol dire che ce l'abbiamo fatta
            #perchè abbiamo preso uno ad uno tutti i caratteri da tutti e due
            if i == len(s1) and j == len(s2):
                return True
            if (i,j) in visti:
                return visti[(i,j)]
            
            strada1=False
            strada2=False
            #Se s1 ha ancora lettere e la lettera che vediamo ora combacia con quella di s3 che stiamo
            #vedendo allora apri un ramo dove prendi questa lettera di i
            #Funziona perchè diciamo "Ok, vediamo che succede se considero questo s1[i] per s3[i+j]"
            #riesco a completare? Se si allora eventualmente returno True
            #s3[i+j] è giusto perchè la sua posizione attuale sarà sempre la somma di quella di queste due
            if i<len(s1) and s1[i] == s3[i+j]:
                strada1=ricorsione(i+1,j)
            #Analogo ma per s2 e non s1
            if j<len(s2) and s2[j] == s3[i+j]:
                strada2=ricorsione(i,j+1)

            
            visti[(i,j)] = strada1 or strada2
            return strada1 or strada2
        
        return ricorsione(0,0)

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        finale=[]
        inizio=[]

        def ricorsione(listaatt,natt):
            if len(listaatt)==k:
                print(listaatt)
                finale.append(listaatt.copy())
                return
            punt=natt
            while punt<n:
                punt+=1
                #percorso dove si aggiunge questo numero
                listaatt.append(punt)
                ricorsione(listaatt,punt)
                #percorso dove non si fa
                listaatt.pop()
        
        ricorsione(inizio,0)
        return finale
                
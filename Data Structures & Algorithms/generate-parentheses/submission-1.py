class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ris = []

        def ricorsione(aperte,chiuse,totale,attuale):
            #Se siamo all'ultimo step, ritorna quanto hai e fermati
            if totale==(n*2):
                ris.append(attuale)
                return

            #Lato dove aggiungiamo l'aperta se è ancora possibile
            if aperte<n:
                ricorsione(aperte+1,chiuse,totale+1,attuale+"(")

            #Lato dove aggiungiamo la parentesi chiusa se possibile
            if chiuse<aperte:
                ricorsione(aperte,chiuse+1,totale+1,attuale+")")
        
        #Fai partire
        ricorsione(1,0,1,"(")
        return ris
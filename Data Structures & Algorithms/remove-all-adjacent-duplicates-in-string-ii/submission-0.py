class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        if len(s)<k:
            return s
        i=0
        car=""
        cont=0
        
        while i < len(s):
            if s[i]==car:
                cont+=1
            else:
                car=s[i]
                cont=1
            if cont == k:
                #Abbiamo trovato k duplicati stesi tra (i - k + 1) e i
                inizio_taglio=i - k + 1
                fine_taglio=i + 1

                #Tagliamo la stringa al volo
                s=s[:inizio_taglio] + s[fine_taglio:]

                #Ora riportiamo i al giusto valore post taglio, o torniamo a 0 o indietro di k
                i=max(0,inizio_taglio-k)
                car=""
                cont=0
            else:
                i+=1
            
        return s
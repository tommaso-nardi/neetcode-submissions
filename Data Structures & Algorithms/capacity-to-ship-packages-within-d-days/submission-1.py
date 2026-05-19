class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        if days==1:
            return sum(weights)

        #Dato una dimensione della nave "peso"...
        def viaggio(peso):
            tot=0
            giorni=1
            #Per ogni pacco, calcola il peso totale finora del carico
            for pacco in weights:
                tot=tot+pacco
                #Se raggiungiamo il massimo di peso, allora aumenta i giorni e setta il peso totale
                #al peso del pacco che non abbiamo potuto caricare e se abbiamo sforato il limite, returna
                #il nostro False (Float Infinito). Altrimenti se ce la facciamo returna True
                if tot>peso:
                    giorni=giorni+1
                    tot=pacco
                    if giorni>days:
                        return False
            return True
        
        #I pesi iniziali vanno dal più grande pacco che abbiamo alla somma dei pacchi
        sx=max(weights)
        dx=sum(weights)
        minimo=dx

        #Con la ricerca binaria trova il minimo peso. Funziona che se sforiamo, aumenta il minimo
        #altrimenti salva il valore attuale che funziona e diminuisci il massimo
        while dx>=sx:
            mid=(sx+dx)//2
            ris=viaggio(mid)
            if ris==False:
                sx=mid+1
            else:
                dx=mid-1
                minimo=mid
        return minimo

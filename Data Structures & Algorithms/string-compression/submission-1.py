class Solution:
    def compress(self, chars: List[str]) -> int:
        #Bel problema, la difficoltà sta nello scrivere il count correttamente
        puntwrite=0
        puntread=0

        while puntread in range(len(chars)):
            car=chars[puntread]
            count=0
            while puntread in range(len(chars)) and car==chars[puntread]:
                puntread+=1
                count+=1
            chars[puntwrite]=car
            puntwrite+=1
            moltatt=1
            #Se c'è una sola istanza del carattere allora ok, abbiamo già fatto
            if count==1:
                continue
            #Altrimenti vediamo l'ordine corretto...
            while count//moltatt>=10:
                moltatt*=10
            #E usiamo questa formula per ogni sottoordine del numero
            #count//moltatt%10 restituirà sempre la cifra più a destra della divisione
            #facendolo cosi quindi, con il moltatt//=10, prendiamo per esempio:
            #1234/1000%10 = 1%10 = 1
            #1234/100%10 = 12%10 = 2
            #1234/10%10 = 123%10 = 3
            while moltatt!=1:
                chars[puntwrite]=str(count//moltatt%10)
                moltatt//=10
                puntwrite+=1
            #1234/1%10 = 1234%1 = 4
            #ordine corretto!
            chars[puntwrite]=str(count//moltatt%10)
            puntwrite+=1
        
        return puntwrite

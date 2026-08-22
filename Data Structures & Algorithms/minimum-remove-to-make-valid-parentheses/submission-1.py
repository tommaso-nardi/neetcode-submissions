class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        if not s:
            return s
        i=0
        posizioniaperte=[]
        stringa=[]

        #Stessa logica del dire se una stringa è valida con parentesi o meno
        #ci salviamo le aperte in uno stack insieme alla posizione
        #quando abbiamo finito facciamo i pop per dire quali parentesi in quale posizione
        #devono essere rimosse semplicemente con stringa.pop(indiceestratto)
        while i<len(s):
            if s[i]!='(' and s[i]!=')':
                stringa.append(s[i])
            elif s[i]==')':
                if posizioniaperte:
                    posizioniaperte.pop()
                    stringa.append(s[i])
            else:
                stringa.append(s[i])
                posizioniaperte.append(len(stringa)-1)
            i+=1

        while posizioniaperte:
            indice=posizioniaperte.pop()
            stringa.pop(indice)
        return("".join(stringa))
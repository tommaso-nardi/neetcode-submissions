class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        #Soluzione che divide le parole in una lista
        parole=s.split()
        if len(pattern) != len(parole):
            return False
        #Serve tener conto bidirezionalmente delle associazioni
        mappaturapattern={}
        mappaturas={}
        i=0
        for c in pattern:
            #Se la lettera è nuova ma la parola è assegnata ad un altra lettera, allora False
            if c not in mappaturapattern:
                if parole[i] in mappaturas:
                    return False
                mappaturapattern[c] = parole[i]
                mappaturas[parole[i]] = c
            #Altrimenti se la lettera è associata ad un altra parola interamente, sempre False
            if mappaturapattern[c] != parole[i]:
                return False
            i+=1
        return True
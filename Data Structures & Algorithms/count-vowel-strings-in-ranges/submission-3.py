class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        visti=[0]*len(words)
        risultato=[]
        conta=0
        i=0
        
        #Niente memoization, serve prefix sum
        #Qui facciamo la somma cumulativa per parola che abbiamo
        for parola in words:
            if parola[0] in 'aeiouAEIOU':
                if parola[len(parola)-1] in 'aeiouAEIOU':
                    conta+=1
            visti[i]=conta
            i+=1

        #E poi, semplicemente, vedendo la somma cumulativa nel range ritorniamo il numero di
        #parole valide che sono presenti con visti[query[1]]-visti[query[0]-1] (inclusivi)
        for query in queries:
            if query[0]==0:
                risultato.append(visti[query[1]])
                continue
            risultato.append(visti[query[1]]-visti[query[0]-1])
        return risultato

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        #Per ogni nodo i, all'inizio sarà radice di se stesso
        radice = list(range(n + 1))
        #Quanto profondo va l'albero?
        grado = [1] * (n+1)

        #Per trovare la radice di un nodo n, se la radice è uguale a se stesso ritorna se stesso, altrimenti itera
        #finchè non si arriva alla radice "vera" e restituiscila
        def parent(n):
            if n != radice[n]:
                radice[n] = parent(radice[n])
            return radice[n]

        #Si ritorna falso se i due nodi che stiamo vedendo ora sono già connessi (prima [1,3][4,3] e poi [3,1])
        def unione(p1,p2):
            p1,p2 = parent(p1),parent(p2)
            if p1 == p2:
                return False
            #Se p1 ha più figli di p2, vogliamo che p1 diventi radice di p2, altrimenti il contrario
            if grado[p1] > grado[p2]:
                radice[p2] = p1
                grado[p1] = grado[p1] + grado[p2]
            else:
                radice[p1] = p2
                grado[p2] = grado[p2] + grado[p1]
            return True

        for n1,n2 in edges:
            if not unione(n1,n2):
                return [n1,n2]
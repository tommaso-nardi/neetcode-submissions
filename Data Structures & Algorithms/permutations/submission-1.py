class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # 1. Caso Base: Se la lista è vuota, restituisce una lista che contiene una lista vuota.
        # Questo serve a far partire il ciclo for successivo.
        if len(nums) == 0:
            return [[]]

        # 2. Scomposizione: Chiamiamo la funzione su tutto tranne il primo numero.
        # 'perm' conterrà tutte le permutazioni della lista "ridotta".
        # Esempio: se nums è [1,2,3], perm riceverà [[2,3], [3,2]]
        perm= self.permute(nums[1:])
        ris = []

        # 3. Ricostruzione: Prendiamo ogni permutazione 'p' che ci è tornata dalla ricorsione
        for p in perm:
            # 4. Infiltrazione: 'i' rappresenta la posizione dove infilare nums[0]
            # Se p è lungo 2, ci sono 3 posizioni (0, 1, 2)
            for i in range (len(p)+1):
                attuale = p.copy()             # Creiamo una copia per non rovinare 'p'
                attuale.insert(i, nums[0])     # Infiliamo il numero '1' nella posizione i
                ris.append(attuale)            # Salviamo questa nuova variante
        return ris
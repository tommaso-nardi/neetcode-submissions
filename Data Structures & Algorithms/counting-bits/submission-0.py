class Solution:
    def countBits(self, n: int) -> List[int]:
        # Inizializziamo la lista dei risultati. Lo spazio è O(n).
        # ris[i] conterrà il numero di bit a 1 per il numero i.
        ris = [0] * (n + 1)
        
        # Partiamo da 1 perché ris[0] è già 0 (corretto, 0 non ha bit a 1).
        for i in range(1, n + 1):
            # LA LOGICA DI OTTIMIZZAZIONE:
            # 1. (i >> 1) : Prendi il numero 'i' e spostalo a destra di 1 bit.
            #               Questo è un numero più piccolo che abbiamo GIÀ calcolato!
            # 2. (i & 1)  : Controlla se l'ultimo bit che abbiamo tolto era un 1 (se i è dispari).
            
            # Esempio: i = 5 (101 in binario)
            # i >> 1 è 2 (10 in binario). ris[2] sappiamo già che è 1.
            # i & 1  è 1 (perché 5 è dispari).
            # ris[5] = ris[2] + 1 = 2. Corretto!
            
            ris[i] = ris[i >> 1] + (i & 1)
            
        return ris
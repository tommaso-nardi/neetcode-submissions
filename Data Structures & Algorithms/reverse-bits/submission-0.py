class Solution:
    def reverseBits(self, n: int) -> int:
        ris = 0

        for i in range(32):
            # 1. FACCIAMO SPAZIO: Spostiamo i bit già salvati in 'ris' a sinistra.
            # Immagina di creare un posto vuoto all'estremità destra.
            ris = ris << 1
            
            # 2. ESTRAIAMO E AGGIUNGIAMO: 
            # Prendiamo l'ultimo bit di n (n & 1) e lo mettiamo nel posto vuoto di ris.
            ris = ris | (n & 1)
            
            # 3. SCORRIAMO: Spostiamo n a destra di uno.
            # Il bit che abbiamo appena letto viene "buttato fuori".
            n = n >> 1
        
        return ris
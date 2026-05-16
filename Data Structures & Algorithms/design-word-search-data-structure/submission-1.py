class WordDictionary:
    def __init__(self):
        self.dizionario = []

    def addWord(self, word: str) -> None:
        self.dizionario.append(word)

    def search(self, word: str) -> bool:
        # 1. Prendiamo ogni parola salvata
        for parola_nel_diz in self.dizionario:
            
            # 2. Controllo rapido sulla lunghezza
            if len(parola_nel_diz) != len(word):
                continue
            
            # 3. Supponiamo che la parola sia corretta finché non troviamo prove contrarie
            match_possibile = True
            
            for i in range(len(word)):
                # Se il carattere non è un punto E le lettere sono diverse...
                if word[i] != "." and word[i] != parola_nel_diz[i]:
                    match_possibile = False
                    break # Inutile controllare le altre lettere di questa parola
            
            # 4. Se dopo il ciclo delle lettere match_possibile è ancora True, abbiamo vinto!
            if match_possibile:
                return True
        
        # 5. Se arriviamo qui, abbiamo controllato TUTTO il dizionario senza successo
        return False
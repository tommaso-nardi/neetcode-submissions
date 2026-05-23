class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        #Forzatura della memoria con i puntatori invece che salvataggio di caratteri
        mappaturapattern = {}
        mappaturas = {}

        sx = 0
        dx = 0
        i = 0

        while dx <= len(s):
            if i >= len(pattern):
                return False
            #Muoviamo dx in avanti finché non finisce la stringa o incontriamo uno spazio
            if dx < len(s) and s[dx] != " ":
                dx += 1
                continue

            #Quando dx si ferma (perchè non si è fatto continue) allora vediamo cosa abbiamo
            #sx<dx evita anche di salvare spazi vuoti, in quel caso non succede niente e si va avanti di nuovo
            #grazie al dx+=1 alla fine. Un controllo in meno
            if sx < dx:
                #Stessi controlli di prima
                #s[sx:dx] è la parola attuale individuata, sx:dx è il suo range
                #Pattern[i] è la lettera attuale, associata quindi alla parola appena trovata
                if pattern[i] not in mappaturapattern:
                    if s[sx:dx] in mappaturas:
                        return False
                    mappaturapattern[pattern[i]] = s[sx:dx]
                    mappaturas[s[sx:dx]] = pattern[i]

                if mappaturapattern[pattern[i]] != s[sx:dx]:
                    return False

                i += 1

            dx += 1
            sx = dx

        return i == len(pattern)
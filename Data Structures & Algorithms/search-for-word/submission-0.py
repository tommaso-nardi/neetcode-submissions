class TrieNode:
    def __init__(self):
        self.children={}
        self.word=False

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #Salviamo nel Trie tutte le parole che dobbiamo cercare, cur.word è la parola completa che rappresentano
        root=TrieNode()
        cur = root
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.word = word
        #Prepariamoci a salvare i risultati e salviamo la matrice
        ris = set()
        rows = len(board)
        cols = len(board[0])
        ris=False


        def ricorsione(x,y,nodo):
            nonlocal ris
            #Salva la lettera attuale individuata e settala come nodo da esaminare
            lettera=board[x][y]
            cur=nodo.children[lettera]
            #Se è una parola completa effettiva salvala e marchia che non ci serve più
            if cur.word:
               ris=True
            #Nascondi la posizione per evitare ripetizioni
            board[x][y]='#'
            #Controlla tutte le direzioni
            direzioni=[(x+1,y),(x,y+1),(x-1,y),(x,y-1)]
            for dx,dy in direzioni:
                # Se la prossima lettera è nel Trie, allora continuiamo a scendere, visto che non rompe gli if
                if 0 <= dx < rows and 0 <= dy < cols:
                    #Salva le 4 lettere attorno, se per caso sono children validi allora continua la ricorsione
                    #perchè se sono nel Trie vuol dire che si va da qualche parte di noto
                    prossima_lettera = board[dx][dy]
                    if prossima_lettera in cur.children:
                        ricorsione(dx, dy, cur)
            #Alla fine recupera le posizioni nascoste per evitare problemi
            board[x][y]=lettera
            
        #Vediamo se le lettere nella matrice sono o meno iniziali di parole, se si parte la ricorsione
        for x in range(rows):
            for y in range(cols):
                if board[x][y] in root.children:
                    ricorsione(x,y,root)
        return ris
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        wordlen=len(word)
        ris=False

        def ricorsione(x,y,i):
            nonlocal ris
            if i == wordlen:
                ris=True
                return
            lettera=board[x][y]
            board[x][y]='#'
            direzioni=[(x+1,y),(x,y+1),(x-1,y),(x,y-1)]
            for dx,dy in direzioni:
                if 0 <= dx < rows and 0 <= dy < cols:
                    if board[dx][dy] == word[i]:
                        ricorsione(dx,dy,i+1)
            #Alla fine recupera le posizioni nascoste per evitare problemi
            board[x][y]=lettera


        for x in range(rows):
            for y in range(cols):
                if board[x][y] == word[0]:
                    ricorsione(x,y,1)
        return ris
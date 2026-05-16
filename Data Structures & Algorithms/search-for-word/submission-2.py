class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])
        wordlen=len(word)

        def ricorsione(x,y,i):
            if i == wordlen:
                return True
            lettera=board[x][y]
            board[x][y]='#'
            direzioni=[(x+1,y),(x,y+1),(x-1,y),(x,y-1)]
            for dx,dy in direzioni:
                if 0 <= dx < rows and 0 <= dy < cols:
                    if board[dx][dy] == word[i]:
                        if ricorsione(dx,dy,i+1):
                            return True
            #Alla fine recupera le posizioni nascoste per evitare problemi
            board[x][y]=lettera
            return False


        for x in range(rows):
            for y in range(cols):
                if board[x][y] == word[0]:
                    if ricorsione(x,y,1):
                        return True
        return False
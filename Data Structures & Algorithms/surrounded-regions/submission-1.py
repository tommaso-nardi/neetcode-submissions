class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])


        def ricorsione(x,y):
            direzioni=[(x+1,y),(x,y+1),(x-1,y),(x,y-1)]
            for dx,dy in direzioni:
                if 0 <= dx < rows and 0 <= dy < cols and dx!=0 and dx!=rows-1 and dy!=0 and dy!=cols-1 and board[dx][dy] == "O":
                    board[dx][dy] = "T"
                    ricorsione(dx,dy)

        for i in range(rows):
            if board[i][0] == "O":
                board[i][0] = "T"
                ricorsione(i,0)
            if board[i][cols-1] == "O":
                board[i][cols-1] = "T"
                ricorsione(i,cols-1)
        for i in range(cols):
            if board[0][i] == "O":
                board[0][i] = "T"
                ricorsione(0,i)
            if board[rows-1][i] == "O":
                board[rows-1][i] = "T"
                ricorsione(rows-1,i)

        for x in range(rows):
            for y in range(cols):
                if board[x][y] == "T":
                    board[x][y] = "O"
                elif board[x][y] == "O":
                    if x!=0 and x!=rows-1 and y!=0 and y!=cols-1:
                        board[x][y] = "X"
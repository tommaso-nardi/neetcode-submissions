class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])

        def ricorsione(x,y):
            grid[x][y]=0
            direzioni=[(x+1,y),(x,y+1),(x-1,y),(x,y-1)]
            for dx,dy in direzioni:
                if 0 <= dx < rows and 0 <= dy < cols and grid[dx][dy]==1:
                    ricorsione(dx,dy)
        
        for i in range(cols):
            if grid[0][i] == 1:
                ricorsione(0,i)
            if grid[rows-1][i]==1:
                ricorsione(rows-1,i)
        for j in range(rows):
            if grid[j][0] == 1:
                ricorsione(j,0)
            if grid[j][cols-1] == 1:
                ricorsione(j,cols-1)

        cont=0
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    cont+=1
        return cont
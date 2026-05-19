class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])

        def ricorsione(x,y):
            lati1=0
            lati2=0
            totale=0
            grid[x][y] = 2
            direzioni=[(x+1,y),(x,y+1),(x-1,y),(x,y-1)]
            for dx,dy in direzioni:
                if 0 <= dx < rows and 0 <= dy < cols and grid[dx][dy] == 1:
                    lati1+=1
                    totale = totale+ricorsione(dx,dy)
                elif 0 <= dx < rows and 0 <= dy < cols and grid[dx][dy] == 2:
                    lati2+=1
            return totale+(4-lati1-lati2)
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    return ricorsione(i,j)
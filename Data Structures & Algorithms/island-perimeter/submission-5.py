class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0
        rows=len(grid)
        cols=len(grid[0])

        #Per ogni isola vediamo con la ricorsione quanti vicini ha (e gli chiamiamo la ricorsione sopra)
        #Per poi ritornare il totale dei perimetri trovati ricorsivamente
        def ricorsione(x,y):
            laticoperti=0
            totale=0
            grid[x][y] = 2
            direzioni=[(x+1,y),(x,y+1),(x-1,y),(x,y-1)]
            for dx,dy in direzioni:
                if 0 <= dx < rows and 0 <= dy < cols and grid[dx][dy] == 1:
                    laticoperti+=1
                    totale = totale+ricorsione(dx,dy)
                elif 0 <= dx < rows and 0 <= dy < cols and grid[dx][dy] == 2:
                    laticoperti+=1
            return totale+(4-laticoperti)
        
        for i in range(rows):
            for j in range(cols):
                if grid[i][j]==1:
                    return ricorsione(i,j)
        return 0
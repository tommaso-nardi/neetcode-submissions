class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        rows = len(grid)
        cols = len(grid[0])

        def ricorsione(x,y,dist):
            if grid[x][y] == -1:
                return
            direzioni=[(x+1,y),(x,y+1),(x-1,y),(x,y-1)]
            figlio = grid[x][y]+1
            for dx,dy in direzioni:
                if 0 <= dx < rows and 0 <= dy < cols and grid[dx][dy] != -1:
                    if figlio < grid[dx][dy]:
                        grid[dx][dy] = figlio
                        ricorsione(dx,dy,figlio)

            

        for x in range(rows):
            for y in range(cols):
                if grid[x][y]==0:
                    ricorsione(x,y,0)
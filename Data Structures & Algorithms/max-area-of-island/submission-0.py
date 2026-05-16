class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ris = 0
        rows=len(grid)
        cols=len(grid[0])
        
        def ricorsione(x,y) -> int:
            if grid[x][y] != 1:
                return 0
            grid[x][y]=2
            attuale=1
            direzioni=[(x+1,y),(x,y+1),(x-1,y),(x,y-1)]
            for dx,dy in direzioni:
                if 0 <= dx < rows and 0 <= dy < cols:
                    attuale = attuale+ricorsione(dx,dy)
            return attuale

        for x in range(rows):
            for y in range(cols):
                if grid[x][y]==1:
                    ris=max(ris,ricorsione(x,y))
        return ris
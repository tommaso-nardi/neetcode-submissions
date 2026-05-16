class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ris = 0
        rows=len(grid)
        cols=len(grid[0])
        
        def ricorsione(x,y):
            if grid[x][y] != "1":
                return
            grid[x][y]="#"
            direzioni=[(x+1,y),(x,y+1),(x-1,y),(x,y-1)]
            for dx,dy in direzioni:
                if 0 <= dx < rows and 0 <= dy < cols:
                    ricorsione(dx,dy)

        for x in range(rows):
            for y in range(cols):
                if grid[x][y]=="1":
                    ricorsione(x,y)
                    ris=ris+1
        return ris
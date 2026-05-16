class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        
        visti={}
        rows=len(grid)
        cols=len(grid[0]) 

        def ricorsione(x,y):
            if (x,y) in visti:
                return visti[(x,y)]
            if x==rows or y==cols:
                return float("inf")
            if x==rows-1 and y==cols-1:
                return grid[x][y]

            att=min(grid[x][y]+ricorsione(x+1,y),grid[x][y]+ricorsione(x,y+1))

            visti[x,y] = att
            return visti[x,y]

        return int(ricorsione(0,0))
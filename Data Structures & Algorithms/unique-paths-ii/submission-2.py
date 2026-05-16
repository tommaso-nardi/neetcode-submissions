class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        visti = {}
        rows=len(obstacleGrid)
        cols=len(obstacleGrid[0])

        def ricorsione(x,y):
            if (x,y) in visti:
                return visti[(x,y)]
            if x==rows or y==cols or obstacleGrid[x][y]==1:
                return 0
            if x==rows-1 and y==cols-1:
                return 1

            att=ricorsione(x+1,y)
            att=att+ricorsione(x,y+1)
            
            visti[x,y] = att
            return visti[x,y]

        return ricorsione(0,0)
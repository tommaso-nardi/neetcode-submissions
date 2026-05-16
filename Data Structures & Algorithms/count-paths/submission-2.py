class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        visti={}

        def ricorsione(x,y):
            if x == m-1 and y == n-1:
                return 1
            if x==m or y==n:
                return 0
            if (x,y) in visti:
                return visti[(x,y)]
            
            att=ricorsione(x+1,y)
            att=att+ricorsione(x,y+1)
            
            visti[x,y] = att
            return visti[x,y]

        return ricorsione(0,0)

        
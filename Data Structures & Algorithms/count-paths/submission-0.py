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
            
            att=0
            direzioni=[(x+1,y),(x,y+1)]
            for dx,dy in direzioni:
                if 0 <= dx < m and 0 <= dy < n:
                    att=att+ricorsione(dx,dy)
            visti[x,y] = att
            return visti[x,y]

        return ricorsione(0,0)

        
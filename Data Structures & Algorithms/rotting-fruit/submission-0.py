class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        turni = 0
        totali = 0
        totalimarci = 0
        queue = collections.deque()
        rows = len(grid)
        cols = len(grid[0])

        for x in range(rows):
            for y in range(cols):
                if grid[x][y] != 0:
                    totali = totali+1
                    if grid[x][y] == 2:
                        totalimarci = totalimarci+1
                        queue.append((x,y))
        
        def ricorsione(queue):
            nonlocal totalimarci
            nonlocal turni
            check=False
            counter = len(queue)
            for i in range(counter):
                attx, atty = queue.popleft()
                direzioni=[(attx+1,atty),(attx,atty+1),(attx-1,atty),(attx,atty-1)]
                for dx,dy in direzioni:
                    if 0 <= dx < rows and 0 <= dy < cols and grid[dx][dy] == 1:
                        check=True
                        totalimarci = totalimarci+1
                        grid[dx][dy] = 2
                        queue.append((dx,dy))
            if check:
                turni = turni+1
                ricorsione(queue)

        ricorsione(queue)
        if totalimarci==totali:
            return turni
        return -1




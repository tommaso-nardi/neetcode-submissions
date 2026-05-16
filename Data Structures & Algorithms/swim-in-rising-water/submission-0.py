class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        
        minHeapDij=[[grid[0][0],(0,0)]]
        shortest={}
        rows=len(grid)
        cols=len(grid[0])

        while minHeapDij:
            w1,(x,y) = heapq.heappop(minHeapDij)
            if x == rows-1 and y == cols-1:
                return w1
            
            if (x,y) in shortest:
                continue
            
            shortest[(x,y)] = w1

            direzioni=[(x+1,y),(x,y+1),(x-1,y),(x,y-1)]
            for dx,dy in direzioni:
                if 0 <= dx < rows and 0 <= dy < cols:
                    if (dx,dy) not in shortest:
                        tempo = max(w1,grid[dx][dy])
                        heapq.heappush(minHeapDij, [tempo,(dx,dy)])

        return 0
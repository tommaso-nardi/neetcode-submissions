class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        #Visto che ci muoviamo in 8 direzioni serve per forza una queue per evitare di tornare indietro
        #anche perchè vuole sapere quanti passi ci vogliono, quindi poi si rischia di andare troppo avanti
        #quando non serve
        if grid[0][0]!=0:
            return -1
        grid[0][0]=1
        coda=deque([(0, 0)])
        passi=1

        #Logica analoga alle ricorsioni che faccio sui grafi con le direzioni, solo che qui si applica sulla
        #coda bfs
        while coda:
            iterazioni=len(coda)
            for i in range(iterazioni):
                x,y=coda.popleft()
                if x==len(grid)-1 and y==len(grid[0])-1:
                    return passi
                direzioni=[(x+1,y),(x,y+1),(x-1,y),(x,y-1),(x+1,y+1),(x-1,y+1),(x-1,y+1),(x+1,y-1)]
                for dx,dy in direzioni:
                    if 0 <= dx < len(grid) and 0 <= dy < len(grid[0]) and grid[dx][dy]==0:
                        grid[dx][dy]=1
                        coda.append((dx,dy))
            passi+=1
        
        return -1
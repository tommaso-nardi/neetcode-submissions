class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows=len(image)
        cols=len(image[0])

        def ricorsione(x,y,og):
            image[x][y]=color
            direzioni=[(x+1,y),(x,y+1),(x-1,y),(x,y-1)]
            for dx,dy in direzioni:
                if 0 <= dx < rows and 0 <= dy < cols and image[dx][dy]==og:
                    ricorsione(dx,dy,og)
        
        if image[sr][sc]==color:
            return image
        ricorsione(sr,sc,image[sr][sc])
        return image
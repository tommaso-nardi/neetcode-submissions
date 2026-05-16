class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        dictpacific=set()
        dictatlantic=set()
        rows=len(heights)
        cols=len(heights[0])
        ris=[]

        def ricorsionepacific(x,y):
            valore=heights[x][y]
            direzioni=[(x+1,y),(x,y+1),(x-1,y),(x,y-1)]
            for dx,dy in direzioni:
                if 0 <= dx < rows and 0 <= dy < cols and heights[dx][dy] >= valore and (dx,dy) not in dictpacific:
                    dictpacific.add((dx,dy))
                    ricorsionepacific(dx,dy)

        def ricorsioneatlantic(x,y):
            valore=heights[x][y]
            direzioni=[(x+1,y),(x,y+1),(x-1,y),(x,y-1)]
            for dx,dy in direzioni:
                if 0 <= dx < rows and 0 <= dy < cols and heights[dx][dy] >= valore and (dx,dy) not in dictatlantic:
                    dictatlantic.add((dx,dy))
                    ricorsioneatlantic(dx,dy)

        for i in range(rows):
            dictpacific.add((i,0))
            dictatlantic.add((i,cols-1))
            ricorsionepacific(i, 0)
            ricorsioneatlantic(i,cols-1)
        for i in range(cols):
            dictpacific.add((0,i))
            dictatlantic.add((rows-1,i))
            ricorsionepacific(0,i)
            ricorsioneatlantic(rows-1,i)
        
        for x in range(rows):
            for y in range(cols):
                if (x,y) in dictatlantic and (x,y) in dictpacific:
                    ris.append([x,y])
        return ris
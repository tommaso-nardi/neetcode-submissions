class Solution:
    def maxArea(self, heights: List[int]) -> int:
        sx=0
        dx=len(heights)-1
        sol=0
        while sx<dx:
            capienza=(dx-sx) * min(heights[sx],heights[dx])
            if capienza>sol:
                sol=capienza
            if heights[sx]>heights[dx]:
                dx=dx-1
            else:
                sx=sx+1
        return sol
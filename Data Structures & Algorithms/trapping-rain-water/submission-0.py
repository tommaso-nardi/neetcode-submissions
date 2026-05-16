class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) == 0 or len(height) == 1:
            return 0
        maxsx=[0] * len(height)
        maxdx=[0] * len(height)
        sol=0
        for i in range(1, len(height)-1):
            maxsx[i] = max(maxsx[i-1],height[i-1])

        heights=height[::-1]
        i=len(height)-2

        while i in range(len(height)):
            maxdx[i] = max(height[i+1],maxdx[i+1])
            i=i-1
        
        for i in range(len(height)):
            if min(maxsx[i],maxdx[i])-height[i] > 0:
                sol = sol+(min(maxsx[i],maxdx[i]))-height[i]
        return sol
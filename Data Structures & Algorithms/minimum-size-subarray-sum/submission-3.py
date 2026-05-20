class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        window_sx=0
        tot=0
        minimo=float("inf")
        for window_dx in range(0,len(nums)):
            tot=tot+nums[window_dx]
            #La logica è che quando ci arriviamo vediamo se la roba di destra basta
            #togliendo man mano le robe di sinistra, se si allora minimo scende sempre più
            while tot>=target:
                minimo=min(minimo,(window_dx-window_sx+1))
                tot=tot-nums[window_sx]
                window_sx=window_sx+1
        if minimo==float("inf"):
            return 0
        return minimo
class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        visti = {}

        def ricorsione(sommaatt):
            if sommaatt in visti:
                return visti[sommaatt]
            if sommaatt == target:
                return 1
            if sommaatt > target:
                visti[sommaatt] = 0
                return 0

            tot=0
            for i in range(len(nums)):
                tot = tot+ricorsione(sommaatt+nums[i])

            visti[sommaatt]=tot
            return tot

        return ricorsione(0)
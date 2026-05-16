class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        differenze = {}
        ris = []
        for x in range(len(nums)):
            diff = target-nums[x]
            if diff in differenze:
                ris.append(differenze[diff])
                ris.append(x)
                return ris
            else:
                differenze[target-diff] = x
        
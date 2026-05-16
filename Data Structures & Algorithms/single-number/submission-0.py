class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nonbit=set()
        for n in nums:
            if n in nonbit:
                nonbit.remove(n)
            else:
                nonbit.add(n)
        return list(nonbit)[0]
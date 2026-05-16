class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]

        perm= self.permute(nums[1:])
        ris = []
        for p in perm:
            for i in range (len(p)+1):
                attuale=p.copy()
                attuale.insert(i,nums[0])
                ris.append(attuale)
        return ris
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        sx=0
        dx=len(numbers)-1
        sol=[]
        while sx<dx:
            if numbers[sx]+numbers[dx]>target:
                dx=dx-1
            elif numbers[sx]+numbers[dx]<target:
                sx=sx+1
            elif numbers[sx]+numbers[dx]==target:
                sol.append(sx+1)
                sol.append(dx+1)
                return sol
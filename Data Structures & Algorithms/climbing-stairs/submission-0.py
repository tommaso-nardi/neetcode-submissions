class Solution:
    def climbStairs(self, n: int) -> int:
        stepuno,stepdue = 1,1

        for i in range (n-1):
            temp=stepuno
            stepuno=stepuno+stepdue
            stepdue=temp
        return stepuno
            
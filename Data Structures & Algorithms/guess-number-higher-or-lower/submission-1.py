# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        sx=1
        dx=n
        while dx>sx:
            mid=(dx+sx)//2
            ris=guess(mid)
            if ris==0:
                return mid
            elif ris==-1:
                dx=mid-1
            else:
                sx=mid+1
        return dx
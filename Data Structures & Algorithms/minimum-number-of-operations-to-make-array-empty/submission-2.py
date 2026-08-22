class Solution:
    def minOperations(self, nums: List[int]) -> int:
        frequenze={}
        mosse=0

        for x in nums:
            if x not in frequenze:
                frequenze[x] = 0
            frequenze[x] += 1

        for numero, frequenza in frequenze.items():
            if frequenza%3==0:
                mosse+=frequenza//3
                continue
            if frequenza%3==2:
                mosse+=frequenza//3+1
                continue
            if frequenza%3==1:
                if frequenza<4:
                    return -1
                if frequenza==4:
                    mosse+=2
                    continue
                mosse+=(frequenza-3)//3+2

        return mosse
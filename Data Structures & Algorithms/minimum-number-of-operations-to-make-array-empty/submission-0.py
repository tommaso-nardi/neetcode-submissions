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
                while frequenza!=0:
                    frequenza-=3
                    mosse+=1
                continue
            if frequenza%3==2:
                while frequenza!=2:
                    frequenza-=3
                    mosse+=1
                mosse+=1
                continue
            if frequenza%3==1:
                if frequenza<4:
                    return -1
                while frequenza!=4:
                    frequenza-=3
                    mosse+=1
                mosse+=2
        return mosse
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ris=[]
        dictt={}
        for n in nums:
            if n not in dictt:
                dictt[n]=1
            else:
                dictt[n]=dictt[n]+1
        frequenze=[[] for i in range(len(nums)+1)]
        for n, freq in dictt.items():
            frequenze[freq].append(n)
        i=0
        for i in range(len(frequenze) - 1, 0, -1):
            for n in frequenze[i]:
                ris.append(n)
                if len(ris) == k:
                    return ris

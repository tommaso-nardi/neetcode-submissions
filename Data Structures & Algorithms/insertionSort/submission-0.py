# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        ris=[]
        for i in range(len(pairs)):
            temp = pairs[i]
            j=i-1
            while j>=0 and pairs[j].key > temp.key:
                pairs[j+1] = pairs[j]
                j=j-1
                pairs[j+1] = temp
            ris.append(list(pairs))
        return ris

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        maxi=-1
        frequenze = Counter(arr)
        for chiave,valore in frequenze.items():
            if chiave==valore:
                maxi=max(maxi,chiave)
        return maxi
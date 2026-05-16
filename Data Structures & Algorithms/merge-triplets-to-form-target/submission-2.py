class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        if len(triplets)==0:
            return False
        if len(triplets)==1 and triplets[0] == target:
            return True
        ris = [0,0,0]
        check = 0
        for tripla in triplets:
            if tripla[0] > target[0] or tripla[1] > target[1] or tripla[2] > target[2]:
                check=1
            if check==0:
                ris[0] = max(ris[0],tripla[0])
                ris[1] = max(ris[1],tripla[1])
                ris[2] = max(ris[2],tripla[2])
            check=0
            if ris == target:
                return True
        return False
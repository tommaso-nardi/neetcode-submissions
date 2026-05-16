class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        vet=sorted(nums1+nums2)
        if len(vet)%2==1:
            return vet[len(vet)//2]
        return (vet[len(vet)//2]+vet[(len(vet)//2)-1])/2
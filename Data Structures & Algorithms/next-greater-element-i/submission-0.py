class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ris=[]
        j=0
        for numero in nums1:
            for j in range(len(nums2)):
                if numero==nums2[j]:
                    break
            
            j+=1
            while j<len(nums2):
                if nums2[j]>numero:
                    ris.append(nums2[j])
                    break
                j+=1
            
            if j==len(nums2):
                ris.append(-1)
        
        return ris

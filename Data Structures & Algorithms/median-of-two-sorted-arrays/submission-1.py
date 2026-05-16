class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        mid = (len(nums1)+len(nums2))//2
        uno = nums1
        due = nums2
        if len(uno)>len(due):
            due,uno=uno,due
        sx=0
        dx=len(uno)-1
        while True:
            metauno=(sx+dx)//2
            metadue=mid-metauno-2

            # Estraiamo i valori a sinistra e destra della partizione per 'uno'
            unoSinistra = uno[metauno] if metauno >= 0 else float("-inf")
            unoDestra = uno[metauno + 1] if (metauno + 1) < len(uno) else float("inf")
            
            # Estraiamo i valori a sinistra e destra della partizione per 'due'
            dueSinistra = due[metadue] if metadue >= 0 else float("-inf")
            dueDestra = due[metadue + 1] if (metadue + 1) < len(due) else float("inf")

            if unoSinistra <= dueDestra and dueSinistra <= unoDestra:
                if (len(nums1) + len(nums2)) % 2 == 1:
                    return min(unoDestra,dueDestra)
                else:
                    return (max(unoSinistra, dueSinistra) + min(unoDestra, dueDestra)) / 2

            elif unoSinistra > dueDestra:
                dx = metauno-1
            else:
                sx = metauno+1
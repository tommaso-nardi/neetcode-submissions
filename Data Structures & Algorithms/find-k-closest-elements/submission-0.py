class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        #Approccio sliding window
        sx=0
        dx=len(arr)-1
        while dx-sx>=k:
            if abs(arr[sx]-x) <= abs(arr[dx]-x):
                dx-=1
            else:
                sx+=1
        
        return arr[sx:dx+1]
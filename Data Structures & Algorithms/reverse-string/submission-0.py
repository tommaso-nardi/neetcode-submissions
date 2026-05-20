class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        punt1=0
        punt2=len(s)-1
        
        while punt1<punt2:
            s[punt1],s[punt2]=s[punt2],s[punt1]
            punt1+=1
            punt2-=1
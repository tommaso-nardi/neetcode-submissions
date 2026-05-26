class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        visti={}

        def ricorsione(i,j):
            if (i,j) in visti:
                return visti[(i,j)]
            if i==len(text1) or j==len(text2):
                return 0
            if text1[i]==text2[j]:
                ris=1+ricorsione(i+1,j+1)
                visti[(i,j)] = ris
                return ris
            
            ris = max(ricorsione(i,j+1),ricorsione(i+1,j))
            visti[(i,j)] = ris
            return ris
        
        return ricorsione(0,0)
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        punt1=0
        punt2=0
        ris=""

        while punt1 < len(word1) and punt2 < len(word2):
            ris+=word1[punt1]
            ris+=word2[punt2]
            punt1+=1
            punt2+=1
        
        for i in range(punt1,len(word1)):
            ris+=word1[i]
        
        for i in range(punt2,len(word2)):
            ris+=word2[i]
        return ris
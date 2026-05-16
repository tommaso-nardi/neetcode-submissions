class Solution:
    def longestPalindrome(self, s: str) -> str:
        ris = ""
        rislen = 0

        for i in range(len(s)):
            sx,dx=i,i
            while sx>=0 and dx < len(s) and s[sx] == s[dx]:
                if (dx-sx+1) > rislen:
                    ris = s[sx:dx+1]
                    rislen=dx-sx+1
                sx=sx-1
                dx=dx+1

            sx,dx=i,i+1
            while sx>=0 and dx < len(s) and s[sx] == s[dx]:
                if (dx-sx+1) > rislen:
                    ris = s[sx:dx+1]
                    rislen=dx-sx+1
                sx=sx-1
                dx=dx+1
        return ris
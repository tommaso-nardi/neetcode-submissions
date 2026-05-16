class Solution:
    def countSubstrings(self, s: str) -> int:
        ris = 0
        for i in range(len(s)):
            sx,dx=i,i
            while sx>=0 and dx < len(s) and s[sx] == s[dx]:
                ris=ris+1
                sx=sx-1
                dx=dx+1

            sx,dx=i,i+1
            while sx>=0 and dx < len(s) and s[sx] == s[dx]:
                ris=ris+1
                sx=sx-1
                dx=dx+1

        return ris        
class Solution:
    def numDecodings(self, s: str) -> int:
        visti={}

        def ricorsione(x):
            if x in visti:
                return visti[x]
            if x == len(s):
                return 1
            if s[x] == "0":
                return 0
            ris = ricorsione(x+1)
            if x+1<len(s):
                if s[x] == "1" or (s[x] == "2" and s[x+1] in "0123456"):
                    ris = ris + ricorsione(x+2)
            visti[x] = ris
            return ris

        return ricorsione(0)
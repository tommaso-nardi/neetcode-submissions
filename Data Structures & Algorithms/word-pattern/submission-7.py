class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        parole=s.split()
        if len(pattern) != len(parole):
            return False
        mappaturapattern={}
        mappaturas={}
        i=0
        for c in pattern:
            if c not in mappaturapattern:
                if parole[i] in mappaturas:
                    return False
                mappaturapattern[c] = parole[i]
                mappaturas[parole[i]] = c
            if mappaturapattern[c] != parole[i]:
                return False
            i+=1
        return True
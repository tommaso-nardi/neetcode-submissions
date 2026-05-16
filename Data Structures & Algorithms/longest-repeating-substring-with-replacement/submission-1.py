class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == k:
            return k
        if len(s) < k:
            return len(s)
        dictt={}
        inizio=0
        lunattuale=0
        maxfreq=0
        ris=0
        for lunattuale in range(len(s)):
            lett = s[lunattuale]
            dictt[lett] = dictt.get(lett,0)+1

            maxfreq = max(maxfreq,dictt[lett])


            if (lunattuale-inizio+1)-maxfreq > k:
                dictt[s[inizio]] -=1
                inizio=inizio+1
                
            ris= max(ris, lunattuale - inizio + 1)
        return ris

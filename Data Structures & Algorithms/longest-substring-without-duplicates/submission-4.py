class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        attuali = []
        dictt = {}
        inizio=0
        mas=0

        for i in range(len(s)):
            while s[i] in attuali:
                attuali.remove(s[inizio])
                inizio=inizio+1
            attuali.append(s[i])
            dictt[s[i]] = i
            mas=max(mas, i-inizio+1)
        return mas
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dicts = {}
        dictt = {}
        for x in range(len(s)):
            if (s[x] not in dicts):
                dicts[s[x]] = 1
            else:
                dicts[s[x]] = dicts[s[x]]+1
        for x in range(len(t)):
            if (t[x] not in dictt):
                dictt[t[x]] = 1
            else:
                dictt[t[x]] = dictt[t[x]]+1
        return (dicts == dictt)
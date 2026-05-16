class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        dictsol={}
        dictatt={}
        for i in s1:
            if i not in dictsol:
                dictsol[i] = 1
            else:
                dictsol[i] +=1
        inizio=0
        lunattuale=0
        for i in range(len(s2)):
            if s2[i] not in dictsol:
                inizio=i+1
                dictatt={}
                continue
            if s2[i] not in dictatt:
                dictatt[s2[i]] = 1
            else:
                dictatt[s2[i]] += 1
            if sum(dictatt.values()) == sum(dictsol.values()):
                if dictatt == dictsol:
                    return True
                dictatt[s2[inizio]] = dictatt[s2[inizio]]-1
                if dictatt[s2[inizio]] == 0:
                    dictatt.pop(s2[inizio])
                inizio=inizio+1
        
        return False

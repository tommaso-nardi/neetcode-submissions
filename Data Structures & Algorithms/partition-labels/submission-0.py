class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        ris=[]
        if len(s)==1:
            ris.append(1)
            return ris
        dictt = {}
        i=0
        for c in s:
            dictt[c]=i
            i=i+1
        curmaxlet=s[0]
        curlen=0
        fine=0
        inizio=0
        for i in range(len(s)):
            fine = max(fine,dictt[s[i]])
            if (i==fine):
                ris.append(i-inizio+1)
                inizio=i+1
        return ris

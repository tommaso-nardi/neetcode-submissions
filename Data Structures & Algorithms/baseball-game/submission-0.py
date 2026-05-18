class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record=[0] * len(operations)
        i=0
        for o in operations:
            if (o != '+') and (o != 'D') and (o != 'C'):
                record[i]=int(o)
                i=i+1
            elif o == '+':
                record[i]=record[i-1]+record[i-2]
                i=i+1
            elif o == 'D':
                record[i]=record[i-1]*2
                i=i+1
            else:
                i=i-1
        
        tot=0
        for j in range(i):
            tot=tot+record[j]
        return tot
class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record=[0] * len(operations)
        i=0
        for o in operations:
            if o == '+':
                record[i]=record[i-1]+record[i-2]
                i=i+1
            elif o == 'D':
                record[i]=record[i-1]*2
                i=i+1
            elif o == 'C':
                record[i-1]=0
                i=i-1
            else:
                record[i]=int(o)
                i=i+1
        
        return sum(record)
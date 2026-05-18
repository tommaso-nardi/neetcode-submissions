class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record=[]

        for o in operations:
            if (o != '+') and (o != 'D') and (o != 'C'):
                record.append(int(o))
            elif o == '+':
                record.append(record[-1] + record[-2])
            elif o == 'D':
                record.append(record[-1]*2)
            else:
                record.pop()
        
        return sum(record)
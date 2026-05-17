class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        ris = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                rimuovi=stack.pop()
                ris[rimuovi] = i-rimuovi

            stack.append(i)
        return ris
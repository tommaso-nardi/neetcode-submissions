class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        radiant=collections.deque()
        dire=collections.deque()
        for i in range(len(senate)):
            if senate[i] == "R":
                radiant.append(i)
            else:
                dire.append(i)
        
        while radiant and dire:
            senrad = radiant.popleft()
            sendir = dire.popleft()
            if senrad < sendir:
                radiant.append(senrad+len(senate))
            else:
                dire.append(sendir+len(senate))
        
        if radiant:
            return "Radiant"
        return "Dire"
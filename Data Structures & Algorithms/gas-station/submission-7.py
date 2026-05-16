class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        benza=0
        spesa=0
        inizio=0
        iterazione=0
        x=0
        while inizio in range(len(gas)):
            benza = benza+gas[x]
            spesa = benza-cost[x]
            benza = spesa
            iterazione = iterazione+1
            x=x+1
            if iterazione == len(gas):
                return inizio
            if x>len(gas)-1:
                x=0
            if spesa<0:
                spesa=0
                iterazione=0
                benza=0
                inizio=x
        return -1
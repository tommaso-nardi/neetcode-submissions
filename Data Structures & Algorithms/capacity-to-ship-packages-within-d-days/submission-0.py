class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        if days==1:
            return sum(weights)

        def viaggio(peso):
            tot=0
            giorni=1
            for pacco in weights:
                tot=tot+pacco
                if tot>peso:
                    giorni=giorni+1
                    tot=pacco
                    if giorni>days:
                        return float("inf")
            return giorni
        
        sx=max(weights)
        dx=sum(weights)
        minimo=dx

        while dx>=sx:
            mid=(sx+dx)//2
            ris=viaggio(mid)
            if ris==float("inf"):
                sx=mid+1
            else:
                dx=mid-1
                minimo=mid
        return minimo

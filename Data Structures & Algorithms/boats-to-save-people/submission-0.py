class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        ordine=sorted(people)
        
        sx=0
        dx=len(people)-1
        tot=0
        while sx<=dx:
            attuale=ordine[dx]
            if attuale+ordine[sx]<=limit:
                sx=sx+1
                dx=dx-1
                tot=tot+1
            else:
                dx=dx-1
                tot=tot+1
        return tot
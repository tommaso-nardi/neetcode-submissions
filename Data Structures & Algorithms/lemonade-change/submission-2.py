class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        if bills[0] != 5:
            return False
        soldi={5: 0, 10: 0, 20:0}

        for cliente in bills:
            if cliente==5:
                soldi[cliente] = soldi[cliente]+1
            elif cliente==20:
                if soldi[10] !=0 and soldi[5] !=0:
                    soldi[10]-=1
                    soldi[5]-=1
                    soldi[20]+=1
                elif soldi[5] >= 3:
                    soldi[5]-=3
                    soldi[20]+=1
                else:
                    return False
            elif soldi[5] != 0:
                soldi[5] = soldi[5] -1
                soldi[10] = soldi[10]+1
            else: return False
        return True 

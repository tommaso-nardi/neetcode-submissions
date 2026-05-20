class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums) % 2 == 1:
            return False
        meta=sum(nums)//2
        visti={}

        def ricorsione(tot,indice):
            if (tot,indice) in visti:
                return visti[(tot,indice)]
            if indice == len(nums) or tot>meta:
                return False
            if tot==meta:
                visti[(tot,indice)] = True
                return True

            strada1=ricorsione(tot+nums[indice],indice+1)
            strada2=ricorsione(tot,indice+1)

            ris = (strada1 or strada2)
            visti[(tot,indice)] = ris
            return ris
        
        return ricorsione(0,0)
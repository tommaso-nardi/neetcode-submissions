class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        if len(fruits)==1:
            return 1
        tipo1=None
        tipo2=None

        indicesx=0
        indicedx=0

        ultimovisto=0
        inizioultimoblocco=0
        sommamax=0

        while indicedx<len(fruits):
            if tipo1==None:
                tipo1=fruits[indicedx]
                indicedx+=1
                continue
            elif tipo2==None:
                tipo2=fruits[indicedx]
                inizioultimoblocco=indicedx
            if fruits[indicedx]!=tipo2 and fruits[indicedx]!=tipo1:
                sommamax=max(sommamax,(indicedx-indicesx))
                indicesx=indicedx-1
                while fruits[indicesx]==ultimovisto:
                    indicesx-=1
                indicesx+=1
                tipo1=fruits[indicesx]
                tipo2=fruits[indicedx]
                inizioultimoblocco=indicedx

            ultimovisto=fruits[indicedx]
            indicedx+=1

        sommamax=max(sommamax,(indicedx-1-indicesx+1))
        return sommamax
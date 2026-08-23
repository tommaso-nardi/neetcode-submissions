class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        if len(fruits)==1:
            return 1
        
        #Questo problema vuole che tengo conto di due tipi consecutivi
        tipo1=None
        tipo2=None

        #Approccio due puntatori
        indicesx=0
        indicedx=0

        #Oltre alla somma massima, semplice da tener traccia, serve sapere quale tipo tra 1 e 2 abbiamo visto
        #per ultimo, cioè l'ultimo tipo di frutto valido che ha visto il puntatore destro
        ultimovisto=0
        sommamax=0

        while indicedx<len(fruits):
            if tipo1==None:
                tipo1=fruits[indicedx]
                indicedx+=1
                continue
            elif tipo2==None:
                tipo2=fruits[indicedx]

            '''
            Ci serve perchè non è detto che il puntatore destro (indicedx) si sia fermato perchè è il tipo2
            quello che non troviamo più, può essere anche tipo1, validissimo, quindi il
            while fruits[indicesx] non deve essere ==tipo2 ma ==ultimovisto, siamo sicuri
            che funziona perchè sarà sempre l'ultimo tipo valido che indicedx ha visto
            e ci fermiamo quando l'elemento a cui punta indicesx è diverso da ultimovisto
            quindi ora abbiamo una nuova serie che va dal tipo ora puntato da tipo1 al
            nuovo tipo puntato da indicedx
            '''

            if fruits[indicedx]!=tipo2 and fruits[indicedx]!=tipo1:
                #Niente +1 perchè indicedx ora punta al primo errato non incluso nel range
                sommamax=max(sommamax,(indicedx-indicesx))
                indicesx=indicedx-1
                while fruits[indicesx]==ultimovisto:
                    indicesx-=1
                indicesx+=1
                tipo1=fruits[indicesx]
                tipo2=fruits[indicedx]

            ultimovisto=fruits[indicedx]
            indicedx+=1

        #Niente +1 perchè indicedx alla fine sfora sempre, quindi +1-1 sarebbe inutile
        sommamax=max(sommamax,(indicedx-indicesx))
        return sommamax
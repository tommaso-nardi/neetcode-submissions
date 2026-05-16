class Solution:
    def rob(self, nums: List[int]) -> int:
        #Logica del ladro, se devo rapinare una casa mi blocco dal prendere la prossima, con cerchio
        if len(nums)==1:
            return nums[0]

        def rapina(case):
            #Mettiamo due valori extra nel vettore dei valori per evitare i problemi di overflow o index out
            case.append(0)
            case.append(0)
            #Salviamo l'array dove salveremo il bottino massimo per ogni casa
            valore = [0] * (len(case)+2)

            #Per ogni casa, partendo dall'ultima e scorrendo indietro, vediamo se guadagniamo di più dal suo valore
            #+ quello massimo della casa a due passi oppure se dobbiamo skipparla e vedere se il bottino massimo
            #della prossima conviene di più
            for i in range(len(case)-1, -1, -1):
                valore[i] = max(case[i] + valore[i+2], valore[i+1])
            return valore[0]

        return max(rapina(nums[1:]),rapina(nums[:-1]))
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        massimo_destra = -1

        #Giriamo l'array al contrario: dall'ultimo elemento fino allo 0
        for i in range(len(arr) - 1, -1, -1):
            #Salva il valore originale
            valore_corrente = arr[i]

            #E cambia il valore arr[i] con il massimo trovato finora
            arr[i] = massimo_destra

            #Aggiorna il massimo appropriatamente
            massimo_destra = max(massimo_destra, valore_corrente)

        return arr
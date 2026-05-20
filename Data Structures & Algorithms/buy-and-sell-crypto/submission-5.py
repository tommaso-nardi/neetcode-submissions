class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        profitto=0
        punt1=0
        for punt2 in range(1,len(prices)):
            if prices[punt1]>prices[punt2]:
                punt1=punt2
        #Fa niente se dice runtime non ottimale, questo è O(1) uguale
            if prices[punt2]-prices[punt1] > profitto:
                profitto = prices[punt2]-prices[punt1]
        return profitto
            
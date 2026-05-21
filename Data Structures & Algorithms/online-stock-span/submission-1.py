class StockSpanner:

    def __init__(self):
        self.prezzi=[]

        
    #Non funzionerebbe tenendo un semplice indice i-1 perchè
    #che ne so se il 'price' di adesso non batte tutti?
    #Quindi mi serve per forza uno stack dove tolgo gli elementi precedenti più piccoli
    #assorbendone il loro conteggio, perchè sicuro batto tutti quelli che hanno battuto loro
    def next(self, price: int) -> int:
        conto=1
        while self.prezzi and self.prezzi[-1][0] <= price:
            prec=self.prezzi.pop()
            conto+=prec[1]
        self.prezzi.append([price,conto])
        return conto

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
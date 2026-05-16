class DynamicArray:
    
    def __init__(self, capacity: int):
        if (capacity<1):
            return
        self.array = [0]*capacity
        self.fill = 0
        self.capacity = capacity


    def get(self, i: int) -> int:
        return self.array[i]


    def set(self, i: int, n: int) -> None:
        self.array[i] = n


    def pushback(self, n: int) -> None:
        if (self.fill == self.capacity):
            self.resize()
        self.array[self.fill] = n
        self.fill = self.fill + 1


    def popback(self) -> int:
        self.fill = self.fill - 1
        val = self.array[self.fill]
        return val
 

    def resize(self) -> None:
        tramite = [0] * (self.capacity*2)
        for n in range(len(self.array)):
            tramite[n] = self.array[n]
        self.capacity = self.capacity*2
        self.array = tramite



    def getSize(self) -> int:
        return self.fill
        
    
    def getCapacity(self) -> int:
        return self.capacity
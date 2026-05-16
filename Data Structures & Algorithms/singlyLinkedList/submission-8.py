class Node:
    def __init__(self, val=0, next=None):
        self.valore = val
        self.prossimo = next

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.bounds = -1

    def get(self, index: int) -> int:
        if (index > self.bounds or self.head is None):
            return -1
        puntatore = self.head
        for n in range(index):
            puntatore = puntatore.prossimo
        return puntatore.valore

    def insertHead(self, val: int) -> None:
        new_node = Node(val, self.head)
        self.head = new_node
        self.bounds += 1

    def insertTail(self, val: int) -> None:
        if self.head is None:
            self.insertHead(val)
            return
        puntatore = self.head
        while puntatore.prossimo:
            puntatore = puntatore.prossimo
        puntatore.prossimo = Node(val)
        self.bounds += 1

    def remove(self, index: int) -> bool:
        if (index > self.bounds or self.head is None):
            return False
        if index == 0:
            self.head = self.head.prossimo
        else:
            puntatore = self.head
            for n in range(index - 1):
                puntatore = puntatore.prossimo
            puntatore.prossimo = puntatore.prossimo.prossimo
        self.bounds -= 1
        return True

    def getValues(self) -> List[int]:
        valori = []
        curr = self.head
        while curr:
            valori.append(curr.valore)
            curr = curr.prossimo
        return valori
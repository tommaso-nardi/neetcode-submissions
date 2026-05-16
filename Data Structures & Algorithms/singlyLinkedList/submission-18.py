class Nodo:
    def __init__(self, val, pn = None):
        self.val = val
        self.prossimo = pn

class LinkedList:
    
    def __init__(self):
        self.bounds = -1
        self.head = None
    
    def get(self, index: int) -> int:
        if (self.head == None or index > self.bounds):
            return -1
        puntatore = self.head
        for n in range (index):
            puntatore = puntatore.prossimo
        return puntatore.val

    def insertHead(self, val: int) -> None:
        mezzo = Nodo(val, self.head)
        self.bounds=self.bounds+1
        self.head = mezzo

    def insertTail(self, val: int) -> None:
        if (self.head == None):
            mezzo = Nodo(val, self.head)
            self.bounds=self.bounds+1
            self.head = mezzo
            return
        puntatore = self.head
        for n in range (self.bounds):
            puntatore = puntatore.prossimo
        mezzo = Nodo(val)
        puntatore.prossimo = mezzo
        self.bounds=self.bounds+1

    def remove(self, index: int) -> bool:
        if (self.head == None or index > self.bounds):
            return False
        if (index==0):
            self.head = self.head.prossimo
            self.bounds=self.bounds-1
            return True
        puntatore = self.head
        puntatoreprec = puntatore
        puntatoresucc = puntatore
        for n in range (index):
            puntatoreprec = puntatore
            puntatore = puntatore.prossimo
            puntatoresucc = puntatore.prossimo
        puntatoreprec.prossimo = puntatoresucc
        self.bounds=self.bounds-1
        return True

    def getValues(self) -> List[int]:
        lista = []
        puntatore = self.head
        for n in range (self.bounds+1):
            lista.append(puntatore.val)
            puntatore = puntatore.prossimo
        return lista
        

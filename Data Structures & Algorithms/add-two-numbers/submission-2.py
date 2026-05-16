# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        som=ListNode()
        inpunt=som
        riporto=0
        #Se c'è riporto o ancora numeri...
        while l1 or l2 or riporto:
            #Assegna i valori attuali con i puntatori
            if l1:
                v1=l1.val
            else:
                v1=0
            if l2:
                v2=l2.val
            else:
                v2=0

            #Sommali col riporto, poi calcola il riporto (max 1 comunque)
            #e il modulo sarà il valore da scrivere nella cella di ora
            somma=v1+v2+riporto
            riporto=somma//10
            val=somma%10
            #ListNode(val) sovrascrive lo 0 di default
            inpunt.next=ListNode(val)
            inpunt=inpunt.next

            #Vai avanti se puoi
            if l1:
                l1=l1.next
            if l2:
                l2=l2.next
        return som.next
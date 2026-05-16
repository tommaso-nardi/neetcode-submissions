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
        while l1 or l2 or riporto:
            if l1:
                v1=l1.val
            else:
                v1=0
            if l2:
                v2=l2.val
            else:
                v2=0
            somma=v1+v2+riporto
            riporto=somma//10
            val=somma%10
            inpunt.next=ListNode(val)
            inpunt=inpunt.next
            if l1:
                l1=l1.next
            if l2:
                l2=l2.next
        return som.next
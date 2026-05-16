# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if head==None or head.next==None:
            return
        slow=head
        fast=head.next
        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        #perchè dobbiamo settare la fine della prima metà in qualche modo
        app=slow.next
        slow.next=None
        #codice ripreso dall'esercizio dell'inversione
        prev=None
        curr=app
        while curr:
            dx = curr.next
            curr.next = prev

            prev=curr
            curr=dx

        sx = head
        dx = prev
        while dx:
            puntsx = sx.next
            puntdx = dx.next
            sx.next = dx
            dx.next = puntsx
            sx = puntsx
            dx = puntdx
            
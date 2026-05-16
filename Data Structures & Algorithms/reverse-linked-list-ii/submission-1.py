# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        pre=dummy
        prev=None
        curr=head
        i=1
        for _ in range(left - 1):
            pre = pre.next
    
        curr=pre.next
        obbiettivo=right-left+1
        coda=curr
        i=0
        while curr and i<obbiettivo:
            dx = curr.next
            curr.next = prev

            prev=curr
            curr=dx
            i=i+1
        
        pre.next=prev
        coda.next=curr
        return dummy.next
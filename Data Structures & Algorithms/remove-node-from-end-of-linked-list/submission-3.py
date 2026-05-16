# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        prec=None
        slow=head
        fast=head
        i=0
        for i in range(n):
            fast=fast.next
        while fast:
            prec=slow
            slow=slow.next
            fast=fast.next
        if head==slow:
            return slow.next
        prec.next=slow.next
        return head
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        ris = ListNode()
        rispunt=ris
        punt1=list1
        punt2=list2

        while punt1 and punt2:
            if punt1.val <= punt2.val:
                rispunt.next=punt1
                punt1=punt1.next
            else:
                rispunt.next=punt2
                punt2=punt2.next
            rispunt=rispunt.next

        if punt1:
            rispunt.next=punt1
        elif punt2:
            rispunt.next=punt2

        return ris.next
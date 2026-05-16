"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        ris = Node(0).next
        risindice = ris
        dictt={}

        curr = head
        while curr:
            dictt[curr] = Node(curr.val)
            curr = curr.next

        curr = head
        while curr != None:
            # Il 'next' del nuovo nodo è il corrispettivo del 'next' del vecchio
            dictt[curr].next = dictt.get(curr.next)
            # Il 'random' del nuovo nodo è il corrispettivo del 'random' del vecchio
            dictt[curr].random = dictt.get(curr.random)
            curr = curr.next

        return dictt[head]
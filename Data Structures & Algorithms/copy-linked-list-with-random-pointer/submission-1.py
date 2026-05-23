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
        nodes = {}

        pres = head

        while pres:
            nodes[pres] = Node(pres.val, None)
            pres = pres.next
        
        pres = head

        while pres:
            nodes[pres].next = nodes.get(pres.next)
            nodes[pres].random = nodes.get(pres.random)

            pres = pres.next
        
        return nodes.get(head)
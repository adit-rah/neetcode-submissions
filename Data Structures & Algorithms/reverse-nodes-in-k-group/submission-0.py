# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prevt = dummy

        while True:
            kth = prevt

            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next

            nextportion = kth.next

            # reverse group
            prev, curr = nextportion, prevt.next

            while curr != nextportion:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            tmp = prevt.next
            prevt.next = kth
            prevt = tmp
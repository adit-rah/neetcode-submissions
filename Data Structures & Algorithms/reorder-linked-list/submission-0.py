# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        slow, fast = head, head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # split properly
        second = slow.next
        slow.next = None

        # reverse second half
        prev = None
        curr = second

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        first, second = head, prev

        while second:
            t1, t2 = first.next, second.next

            first.next = second
            second.next = t1

            first, second = t1, t2
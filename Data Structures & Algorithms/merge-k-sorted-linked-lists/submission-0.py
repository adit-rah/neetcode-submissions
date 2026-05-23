# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        res = dummy = ListNode(0)
        k = len(lists)
        while lists:
            mine, mini = 1e9, -1
            for i in range(k):
                if lists[i].val < mine:
                    mini = i
                    mine = lists[i].val
            
            dummy.next = lists[mini]
            lists[mini] = lists[mini].next
            if not lists[mini]:
                lists.remove(lists[mini])
                k -=1
            dummy = dummy.next

        return res.next

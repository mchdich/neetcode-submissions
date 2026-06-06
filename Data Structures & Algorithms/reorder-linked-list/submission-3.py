# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #can only reorder for >= 3 nodes
        if not head.next or not head.next.next:
            return
        l = head
        # 2,8,4,6
        while l.next and l.next.next:
            r = l.next
            while r.next and r.next.next:
                r = r.next
            prev = r
            r = r.next
            r.next = l.next
            l.next = r
            prev.next = None
            l = r.next
        return
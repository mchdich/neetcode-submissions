# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        r = head
        for i in range(n):
            r = r.next
        node = ListNode()
        dummy = node
        node.next = head
        l = dummy
        while r:
            r = r.next
            l = l.next
        l.next = l.next.next
        return dummy.next
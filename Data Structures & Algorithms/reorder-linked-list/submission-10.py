# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head: #find 2 halves
            return
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        h1 = head
        reverse = slow.next
        slow.next = None #disconnect the lists

        prev = None #reverse 2nd half
        while reverse:
            nxt = reverse.next
            reverse.next = prev
            prev = reverse
            reverse = nxt
        h2 = prev

        curr1, curr2 = h1, h2 #stitch together
        while curr2:
            nxt1, nxt2 = curr1.next, curr2.next
            curr2.next = nxt1
            curr1.next = curr2
            curr1, curr2 = nxt1, nxt2
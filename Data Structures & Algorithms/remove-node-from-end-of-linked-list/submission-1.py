# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #1,2,3,4 n=2
        #len=4, 4-2+1=3
        #0,1,2,3,4
        curr = head
        length = 0
        while curr:
            length += 1
            curr = curr.next
        remove = length - n + 1
        index = 0
        node = ListNode()
        dummy = node
        node.next = head
        while (index + 1) != remove:
            node = node.next
            index += 1
        if (index + 1) == length:
            node.next = None
        else:
            node.next = node.next.next
        return dummy.next
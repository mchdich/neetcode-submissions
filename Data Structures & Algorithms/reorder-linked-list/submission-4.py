# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #can only reorder for >= 3 nodes
        if not head:
            return
        nodes = []
        add = head
        while add:
            nodes.append(add)
            add = add.next
        curr = head
        while curr.next and curr.next.next:
            nodes[-1].next = curr.next
            curr.next = nodes[-1]
            nodes[-2].next = None
            nodes.pop()
            curr = curr.next.next 
        
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        dummy = ListNode()
        curr = dummy
        while True:
            minList = -1
            for i in range(len(lists)):
                if not lists[i]:
                    continue
                if minList == -1 or lists[i].val < lists[minList].val:
                    minList = i
            if minList == -1:
                break
            curr.next = lists[minList]
            lists[minList] = lists[minList].next
            curr = curr.next
        return dummy.next
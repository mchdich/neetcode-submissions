# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        queue = deque([[root, subRoot]])
        while queue:
            r, sr = queue.popleft()
            if r and sr:
                if r.val == sr.val:
                    res = self.isSame(r, sr)
                    if res:
                        return True
                queue.append([r.left, sr])
                queue.append([r.right, sr])
        return False

    def isSame(self, root, subRoot):
        if not root and not subRoot:
            return True
        queue = deque([[root, subRoot]])
        while queue:
            r, sr = queue.popleft()
            if (r and not sr) or (not r and sr) or (r and sr and r.val != sr.val):
                return False
            if r and sr:
                queue.append([r.left, sr.left])
                queue.append([r.right, sr.right])
        return True
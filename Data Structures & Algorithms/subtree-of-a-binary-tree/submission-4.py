# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        stack = [[root, subRoot]]
        while stack:
            r, sr = stack.pop()
            if r and sr:
                if r.val == sr.val:
                    res = self.isSame(r, sr)
                    if res:
                        return True
                stack.append([r.left, sr])
                stack.append([r.right, sr])
        return False

    def isSame(self, root, subRoot):
        if not root and not subRoot:
            return True
        stack = deque([[root, subRoot]])
        while stack:
            r, sr = stack.pop()
            if (r and not sr) or (not r and sr) or (r and sr and r.val != sr.val):
                return False
            if r and sr:
                stack.append([r.left, sr.left])
                stack.append([r.right, sr.right])
        return True
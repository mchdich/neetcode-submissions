# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        stack = [[p, q]]
        while stack:
            cp, cq = stack.pop()
            if (cp and not cq) or (not cp and cq) or (cp and cq and cp.val != cq.val):
                return False
            if cp and cq:
                stack.append([cp.left, cq.left])
                stack.append([cp.right, cq.right])
        return True
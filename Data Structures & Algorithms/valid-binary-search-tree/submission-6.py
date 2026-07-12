# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        lB, rB = float('-inf'), float('inf')
        return self.isValidSubtree(lB, rB, root)

    def isValidSubtree(self, lB, rB, node):
        if not node:
            return True
        if not (lB < node.val < rB):
            return False
        l = self.isValidSubtree(lB, node.val, node.left)
        r = self.isValidSubtree(node.val, rB, node.right)
        return l and r
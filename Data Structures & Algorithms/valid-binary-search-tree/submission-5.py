# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        l = self.isValidSubtree(root, root.left, "left")
        r = self.isValidSubtree(root, root.right, "right")
        if not (l and r):
            return False
        l = self.isValidBST(root.left)
        r = self.isValidBST(root.right)
        return l and r
    def isValidSubtree(self, root, child, di):
        if not child:
            return True
        if di == "left" and child.val >= root.val:
            return False
        if di == "right" and child.val <= root.val:
            return False
        l = self.isValidSubtree(root, child.left, di)
        r = self.isValidSubtree(root, child.right, di)
        return l and r
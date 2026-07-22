# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:#run out of leads
            return False
        if root.val == subRoot.val:
            res = self.isSame(root, subRoot)
            if res:
                return True
        l = self.isSubtree(root.left, subRoot)
        r = self.isSubtree(root.right, subRoot)
        return l or r

    def isSame(self, r, sr):
        if not r and not sr:
            return True
        if r and sr and r.val == sr.val:
            l = self.isSame(r.left, sr.left)
            r = self.isSame(r.right, sr.right)
            return l and r
        else:
            return False
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode], left = -2**63, right = 2**63) -> bool:

        if not root: return True

        return left < root.val < right and \
            self.isValidBST(root.left, left, root.val) and \
            self.isValidBST(root.right, root.val, right)

        
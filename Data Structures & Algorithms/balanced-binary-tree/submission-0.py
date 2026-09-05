# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def check(self, node):
        if not node: return 0, True
        left_size, left_check = self.check(node.left)
        right_size, right_check = self.check(node.right)
        balanced = left_check and right_check and abs(left_size - right_size) <= 1

        return 1 + max(left_size, right_size), balanced

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        size, check = self.check(root)
        return check

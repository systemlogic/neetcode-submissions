# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int],) -> Optional[TreeNode]:
        in_enumerate = {val:index for index, val in enumerate(inorder)}
        self.start_index = 0

        def dfs(low, high):
            if low > high: return None
            value = preorder[self.start_index]
            self.start_index += 1
            mid = in_enumerate[value]
            return TreeNode(
                value,
                dfs(low, mid -1),
                dfs(mid + 1, high)
            )
        return dfs(0, len(inorder) - 1)
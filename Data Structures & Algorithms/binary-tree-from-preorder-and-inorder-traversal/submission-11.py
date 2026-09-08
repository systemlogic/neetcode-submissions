# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int],) -> Optional[TreeNode]:
        inorder_idx = {val:i for i, val in enumerate(inorder)}
        self.index = 0

        def build(low, high):
            if low > high:
                return None
            val = preorder[self.index]
            self.index += 1
            mid = inorder_idx[val]
            return TreeNode(
                val,
                build(low, mid - 1),
                build(mid + 1, high)
            )
        return build(0, len(inorder) - 1)


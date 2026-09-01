# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        level = [root] if root else []
        levels = []
        while level:
            tmp = []
            values = []
            while level:
                node = level.pop(0)
                values.append(node.val)
                if node.left:
                    tmp.append(node.left)
                if node.right:
                    tmp.append(node.right)
            levels.append(values)
            level[:] = tmp[:]
        return levels
        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        level = [root] if root else []
        right_view = []
        while level:
            first = True
            tmp = []
            while level:
                node = level.pop(0)
                if first:
                    right_view.append(node.val)
                    first = False
                if node.right:
                    tmp.append(node.right)
                if node.left:
                    tmp.append(node.left)
            level = tmp
        return right_view


        
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        lst = [root] if root else []
        right_view = []
        while lst:
            tmp = []
            first = True
            while lst:
                item = lst.pop()
                if first:
                    right_view.append(item.val)
                    first = False
                if item.right:
                    tmp.insert(0, item.right)
                    
                if item.left:
                    tmp.insert(0, item.left)
            lst[:] = tmp[:]


        return right_view
        
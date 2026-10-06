# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        counter = k
        ans = 0
        def traverse(node):
            nonlocal counter
            nonlocal ans
            if not node:
                return

            

            traverse(node.left)

            counter -= 1
            if counter == 0:
                ans = node.val

            traverse(node.right)

            return

        traverse(root)

        return ans

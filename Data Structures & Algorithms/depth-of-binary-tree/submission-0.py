# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def traverse(node: Optional[TreeNode], depth):
            nonlocal ans

            if not node:
                return

            
            depth += 1

            ans = max(ans, depth)

            traverse(node.right, depth)
            traverse(node.left, depth)

            return

        traverse(root, 0)
        return ans
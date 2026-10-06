# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = 0

        def traverse(node, maxVal = float("-inf")):
            nonlocal ans

            if not node:
                return

            if maxVal <= node.val:
                ans += 1

            maxVal = max(node.val, maxVal)


            traverse(node.left, maxVal)
            traverse(node.right, maxVal)

        
        traverse(root)

        return ans
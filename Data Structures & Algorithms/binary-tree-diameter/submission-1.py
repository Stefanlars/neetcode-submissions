# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        ans = 0

        def traverse(node):
            nonlocal ans
            if not node:
                return 0

            l_side_depth = traverse(node.left)
            r_side_depth = traverse(node.right)

            ans = max(ans, l_side_depth + r_side_depth)

            return max(l_side_depth, r_side_depth) + 1

            

        if not root:
            return 0

        traverse(root)

        return ans
        
            
            
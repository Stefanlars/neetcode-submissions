# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        

        def isBalanced(node):

            if not node:
                return 0, True

            left_h, l_bal = isBalanced(node.left)
            right_h, r_bal = isBalanced(node.right)

            sub_balanced = l_bal and r_bal

            return max(left_h, right_h) + 1, sub_balanced and abs(left_h - right_h) <= 1

        _, balanced = isBalanced(root)

        return balanced
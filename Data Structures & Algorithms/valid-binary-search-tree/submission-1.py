# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        def validate(node: Optional[TreeNode], curr_min=float("-inf"), curr_max=float("inf")):
            if not node:
                return True

            if curr_min >= node.val or curr_max <= node.val:
                return False

            
            return validate(node.left, curr_min=curr_min, curr_max=node.val) and validate(node.right, curr_min=node.val, curr_max=curr_max)

        return validate(root)

            


            
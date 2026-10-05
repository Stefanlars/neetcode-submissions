# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        
        def dfs_parrel(node_1, node_2):

            if not node_1 and not node_2:
                return True

            if not node_1 and node_2:
                return False

            if not node_2 and node_1:
                return False

            if node_1.val != node_2.val:
                return False

            left = dfs_parrel(node_1=node_1.left, node_2=node_2.left)
            right = dfs_parrel(node_1=node_1.right, node_2=node_2.right)

            return left and right

        return dfs_parrel(p, q)
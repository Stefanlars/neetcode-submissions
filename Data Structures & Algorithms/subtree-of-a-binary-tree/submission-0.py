# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        # Approach: dfs until we find a node with the same starting value. Then we can run a compare tree and return either true of false.
        if not subRoot:
            return True

        def isEqual(node_1, node_2):

            if not node_1 and not node_2:
                return True

            if node_1 and node_2 and node_1.val == node_2.val:

                print(node_1.val, node_2.val)
                return isEqual(node_1.left, node_2.left) and isEqual(node_1.right, node_2.right)
            
            else:
                return False

        def dfs(node):
            if not node:
                return False

            if node.val == subRoot.val:

                # perform the comparison here
                if isEqual(node, subRoot):
                    return True

            return dfs(node.left) or dfs(node.right)

        return dfs(root)
            
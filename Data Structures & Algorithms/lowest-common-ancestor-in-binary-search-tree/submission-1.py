# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        # initial thought is recursive solution where once we hi
        # grab all ancestors for the first node and second node. Then iterate through both lists and get the min
        ans = root

        def LCA(node: Optional[TreeNode]):
            nonlocal ans

            if not node:
                return

            # update LCA
            
            ans = node

            if p.val < node.val and q.val < node.val:
                LCA(node.left)

            elif p.val > node.val and q.val > node.val:
                LCA(node.right)

            else:
                return
            
        LCA(root)

        return ans
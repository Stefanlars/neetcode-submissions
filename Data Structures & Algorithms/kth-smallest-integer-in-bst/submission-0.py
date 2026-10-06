# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        
        val_list = []
        def traverse(node):
            nonlocal val_list
            if not node:
                return 1

            

            depth = traverse(node.left)

            val_list.append(node.val)

            depth += traverse(node.right)

            return depth + 1

        traverse(root)

        return val_list[k - 1]

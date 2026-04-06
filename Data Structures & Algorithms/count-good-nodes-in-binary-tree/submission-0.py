# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = [0]

        def dfs(node, max_val):
            if node is None:
                return

            if node.val >= max_val:
                print(node.val, max_val)
                count[0] += 1

            new_max = max(node.val, max_val)

            left = dfs(node.left, new_max)
            right = dfs(node.right, new_max)

        dfs(root, float('-inf'))

        return count[0]
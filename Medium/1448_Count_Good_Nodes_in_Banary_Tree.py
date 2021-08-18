# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def dfs(Node, max_so_far):
            if not Node: return 0
            good = 1 if Node.val >= max_so_far else 0
            max_so_far = max(max_so_far, Node.val)
            return good + dfs(Node.left, max_so_far) + dfs(Node.right, max_so_far)
        return dfs(root, -int(1e5))
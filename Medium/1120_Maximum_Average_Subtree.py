# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maximumAverageSubtree(self, root: Optional[TreeNode]) -> float:
        self.out = 0
        def helper(root):
            if not root: return [0.0, 0]
            s1, n1 = helper(root.left)
            s2, n2 = helper(root.right)
            s = s1 + s2 + root.val
            n = n1 + n2 + 1
            self.out = max(self.out, s/n)
            return [s, n]
        helper(root)
        return self.out

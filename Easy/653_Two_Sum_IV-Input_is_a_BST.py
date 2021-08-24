# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        def dfs(root, dic, k):
            if root == None: return
            diff = k - root.val
            if diff in dic: return True
            dic[root.val] = diff
            return dfs(root.left, dic, k) or dfs(root.right, dic, k)
        return dfs(root, {}, k)

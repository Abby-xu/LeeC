# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def dfs(start, end):
            if start > end: return [None]
            out = []
            for i in range(start, end+1):
                left = dfs(start, i-1)
                right = dfs(i+1, end)
                for l in left:
                    for r in right:
                        root = TreeNode(i)
                        root.left = l
                        root.right = r
                        out.append(root)
            return out
        return dfs(1,n)

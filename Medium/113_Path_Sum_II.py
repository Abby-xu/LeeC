# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> List[List[int]]:
        out = []
        def helper(curr_sum, curr, node):
            if node is None:
                return
            if not node.left and not node.right:
                if curr_sum + node.val == targetSum:  
                    out.append(curr + [node.val])
            if node.left:
                helper(curr_sum+node.val, curr+[node.val], node.left)
            if node.right:
                helper(curr_sum+node.val, curr+[node.val], node.right)
            return
        helper(0,[],root)
        return out
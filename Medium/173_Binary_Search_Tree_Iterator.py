# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator(object):
    def __init__(self, root):
        self.st = []
        self.pushLeft(root)
        
    def pushLeft(self, root):
        while root != None:
            self.st.append(root)
            root = root.left

    def next(self):
        node = self.st.pop()
        self.pushLeft(node.right)
        return node.val

    def hasNext(self):
        return len(self.st) > 0
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

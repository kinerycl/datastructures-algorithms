# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ans = 0
        def depth(node):
            if not node:
                return 0
            left = depth(node.left)  
            right = depth(node.right)
            self.ans = max(self.ans, left+right)
            return max(left, right) + 1
        depth(root)
        return self.ans

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        return self.findDepth(root, 0)
        
    def findDepth(self, node, depth):
        if node == None:
            return depth
        depth+=1
        right = self.findDepth(node.right, depth)
        left = self.findDepth(node.left, depth)
        return max(right, left)

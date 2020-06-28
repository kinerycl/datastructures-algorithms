# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def mergeTrees(self, t1, t2):
        """
        :type t1: TreeNode
        :type t2: TreeNode
        :rtype: TreeNode
        """
        if t2 == None:
            return t1
        elif t1 == None:
            return t2
        else: 
            t1.val = t1.val + t2.val
       
            t1.right = self.mergeTrees(t1.right, t2.right)
            t1.left = self.mergeTrees(t1.left, t2.left)
        
            return t1

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def __init__(self):
        self.totalPaths = 0
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if root == None:
            return 0
        self.allPaths(root, sum, 0)
        
        self.pathSum(root.left, sum)
        self.pathSum(root.right, sum)
        
        return self.totalPaths 
        
    def allPaths(self, node, sum, currSum):
        if node == None:
            return currSum
        
        currSum += node.val
        
        if currSum == sum:
            self.totalPaths += 1
            
        self.allPaths(node.left, sum, currSum)
        self.allPaths(node.right, sum, currSum)

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        if root.left == None and root.right == None:
            return 1
        return self.search(root, 0, [1000000])
              
    def search(self, node, depth, minD):
        depth +=1
        
        if node == None:
            return
        
        if node.left == None and node.right == None:
            if depth < minD[0]:
                minD[0] = depth 
            return 
                
        self.search(node.left, depth, minD)
        self.search(node.right, depth, minD)
                
        return minD[0]

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def preorder(root, lst):
            if root is not None:
                lst.append(root.val)
                preorder(root.left, lst) #go left
                preorder(root.right, lst) #go right
            return lst

            
        return preorder(root, [])
        

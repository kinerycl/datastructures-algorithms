# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def inorder(root, lst):
            if root != None:
                inorder(root.left, lst)
                lst.append(root.val)
                inorder(root.right, lst)
            return lst
        return inorder(root, [])

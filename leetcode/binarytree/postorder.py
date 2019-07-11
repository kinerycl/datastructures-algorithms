# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def post(node, lst):
            if node is not None:
                post(node.left, lst)
                post(node.right, lst)
                lst.append(node.val)
            return lst
        
        return post(root, [])

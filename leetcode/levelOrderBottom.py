# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        return self.makeList(root, 0, [])
        
    def makeList(self, node, depth, master_lst):
        if node == None:
            return master_lst
        
        if len(master_lst) <= depth:
            master_lst.insert(0,[])
            
        position = len(master_lst) - depth-1
        master_lst[position].append(node.val)
        
        depth += 1
        self.makeList(node.left, depth, master_lst)
        self.makeList(node.right, depth, master_lst)
        
        return master_lst

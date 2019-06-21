# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        ret_lst = ListNode(None)
        prev_lst = ListNode(None)
        i = 0
        count = 0
        while l1 or l2 is not None:
            count += 1
            if l1 and l2 is not None:   
                val = l1.val + l2.val
                l1 = l1.next
                l2 = l2.next
            elif l1 is None:
                val = l2.val
                l2 = l2.next
            else:
                val = l1.val
                l1 = l1.next
            if i == 1:               #accounts for prev carries
                val += 1
                i = 0
            if val > 9:  #accounts for future carries
                i = 1
                val -= 10
            val_node = ListNode(val)
            if count == 1:
                ret_lst = val_node
                prev_lst = val_node
            else:
                prev_lst.next = val_node
                prev_lst = val_node

        if i == 1:
            prev_lst.next = ListNode(1)
        return ret_lst
                

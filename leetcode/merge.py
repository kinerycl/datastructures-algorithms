class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        length = m+n
    
        pt1 = m-1
        pt2 = n-1
        insert = m+n-1
        
        while pt2 > -1:

            if pt1>-1 and nums1[pt1]>nums2[pt2]:
            
                nums1[insert] = nums1[pt1]
                pt1-=1
                
            else:
                
                nums1[insert] = nums2[pt2]
                pt2-=1
            
            insert-=1
        

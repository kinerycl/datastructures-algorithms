class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0 
        left = 0
        right = len(height) - 1 
        while left != right:
            if height[left] > height[right]:
                area = height[right] * (right - left)
                right -= 1
            else: 
                area = height[left] * (right - left)
                left += 1
            if area > max_area:
                max_area = area
        return max_area
                

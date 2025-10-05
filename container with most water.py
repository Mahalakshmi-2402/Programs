class Solution:
    def maxArea(self, height):
        l = 0
        r = len(height) - 1
        max_w = 0
        
        while l < r:
            area = min(height[l], height[r]) * (r - l)
            max_w = max(max_w, area)
            
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return max_w
class Solution:
    def maxArea(self, heights: List[int]) -> int:

        
        n = len(heights)
        l = 0
        r = n - 1
        maxArea = 0
        while l< r:
            h = min(heights[l],heights[r])
            w = r - l
            a = h * w
            maxArea = max(maxArea,a)

            if heights[l]< heights[r]:
                l = l+1
            else:
                r = r-1
        
        return maxArea
        
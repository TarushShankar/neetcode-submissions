class Solution:
    def search(self, nums: List[int], target: int) -> int:

        n = len(nums)
        left = 0
        right = n - 1

        while left <= right:
            midpoint = (right + left)//2

            if nums[midpoint] == target:
                return midpoint
            
            elif nums[midpoint] > target:
                right = midpoint - 1
            
            else:
                left = midpoint + 1
        
        return -1


        
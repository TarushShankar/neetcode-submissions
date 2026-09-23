class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        ans = []

        for i in range(len(nums)):
            square = nums[i] * nums[i]
            ans.append(square)
        
        ans.sort()
        return ans
        
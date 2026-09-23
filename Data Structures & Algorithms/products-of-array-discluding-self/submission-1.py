class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        left_multiplier = 1
        right_multiplier = 1

        left_array = [0] * n
        right_array = [0] * n

        for i in range(n):
            j = - i - 1
            left_array[i] = left_multiplier 
            right_array[j] = right_multiplier 
            left_multiplier *= nums[i]
            right_multiplier *= nums[j]
        
        return [l*r for l,r in zip(left_array,right_array)]

     
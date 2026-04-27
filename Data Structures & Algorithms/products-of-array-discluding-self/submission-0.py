class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        l_multiplier = 1
        r_multiplier = 1

        l_array = [0]*n
        r_array = [0]*n

        for i in range(n):
            j = -i - 1
            l_array[i] = l_multiplier
            r_array[j] = r_multiplier
            l_multiplier = l_multiplier * nums[i]
            r_multiplier = r_multiplier * nums[j]
        
        return [l*r for l,r in zip(l_array,r_array)]
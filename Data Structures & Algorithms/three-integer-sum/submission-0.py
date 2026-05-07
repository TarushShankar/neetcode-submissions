class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        nums.sort() #most important aspect
        n = len(nums)
        answers = []


        for i in range(len(nums)):
            if nums[i]>0:
                break
            
            elif i>0 and nums[i] == nums[i-1]:
                continue
            
            low, high = i+1, n-1

            while low< high:
                summ = nums[low] + nums[high] + nums[i]
                if summ == 0:
                    answers.append([nums[low],nums[high],nums[i]])
                    low, high = low + 1, high - 1

                    while low< high and nums[low] == nums[low-1]:
                        low += 1
                    
                    while low< high and nums[high] == nums[high+1]:
                        high -= 1
                
                elif summ < 0:
                    low += 1
                else:
                    high -= 1


        return answers
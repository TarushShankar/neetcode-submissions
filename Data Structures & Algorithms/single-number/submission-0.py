from collections import Counter

class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        count_dict = Counter(nums)

        for key in count_dict.keys():
            if count_dict[key] == 1:
                return key

        
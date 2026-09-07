from collections import Counter
import heapq
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        len_num = len(nums)

        counter = Counter(nums)
        for key, value in counter.items():
            if value > len_num // 2:
                return key


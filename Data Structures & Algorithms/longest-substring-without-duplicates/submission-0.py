class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length = 0
        l = 0
        
        n = len(s)
        sett = set()
        for r in range(n):
            while s[r] in sett:
                sett.remove(s[l])
                l += 1
            w = (r - l)+ 1
            length = max(length,w)
            sett.add(s[r])
        
        return length

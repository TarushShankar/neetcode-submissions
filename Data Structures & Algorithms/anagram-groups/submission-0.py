class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        res = defaultdict(list)

        for char in strs:
            count = [0] * 26

            for c in char:
                count[ord(c)-ord("a")]+= 1

            res[tuple(count)].append(char)
        values = []

        for value in res.values():
            values.append(value)
        return values
        
class Solution:
    def firstUniqChar(self, s: str) -> int:
        repeats = {}
        for index in range(len(s)):
            if s[index] not in repeats:
                repeats[s[index]] = 1
            else:
                repeats[s[index]] += 1
        
        for index in range(len(s)):
            if repeats[s[index]] == 1:
                return index
        return -1
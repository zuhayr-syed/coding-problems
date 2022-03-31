class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dict = {}
        s = s.upper()
        s = s.split(' ')
        if len(pattern) != len(s):
            return False
        for i in range(len(pattern)):
            if pattern[i] not in dict:
                dict[pattern[i]] = s[i]
                if s[i] not in dict:
                    dict[s[i]] = pattern[i]
                elif dict[s[i]] != pattern[i]:
                    return False
            else:
                if dict[pattern[i]] != s[i]:
                    return False
            
        return True
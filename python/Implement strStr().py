class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        letters = ""
        if (len(needle) == 0):
            return 0
        for i in range(len(haystack)):
            if (haystack[i] == needle[0]):
                letters = haystack[i:i + len(needle)]
                if (letters == needle):
                    return i
        return -1
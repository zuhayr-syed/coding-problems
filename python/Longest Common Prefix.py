class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if (len(strs) > 0):
            prefix = strs[0]
            prefix = list(prefix)
            for i in range(1, len(strs)):
                for x in range(len(strs[i])):
                    if (x  < len(prefix)):
                        if(strs[i][x] != prefix[x]):
                            prefix = prefix[:x]
                            break
                prefix = prefix[:len(strs[i])]
            return "".join(prefix)
        else:
            return ""
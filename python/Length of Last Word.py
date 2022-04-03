class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split(' ')
        last = ''
        index = len(s) - 1
        while last == '':
            last = s[index]
            index -= 1  
        return len(last)
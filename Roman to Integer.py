class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {'M': 1000,'D': 500 ,'C': 100,'L': 50,'X': 10,'V': 5,'I': 1}
        integer = 0
        for index in range(len(s)-1):
            if(roman[s[index]] >= roman[s[index + 1]]):
                integer += roman[s[index]]
            else:
                integer -= roman[s[index]]
        return integer + roman[s[-1]]
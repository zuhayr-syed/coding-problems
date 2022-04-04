class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        dict = {}
        for letter in s:
            if letter not in dict:
                dict[letter] = 1
            else:
                dict[letter] += 1
        for letter in t:
            if letter not in dict:
                return letter
            else:
                dict[letter] -= 1
                if dict[letter] < 0:
                    return letter
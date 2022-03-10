class Solution:
    def isPalindrome(self, s: str) -> bool:
        if (len(s) < 2):
            return True
        else:
            letters = []
            for char in s:
                if (char.isalnum()):
                    char = char.lower()
                    letters.append(char)
            palindrome = letters[::-1]
            if (letters == palindrome):
                return True
            return False
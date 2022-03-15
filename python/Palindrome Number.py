class Solution:
    def isPalindrome(self, x: int) -> bool:
        x = str(x)
        if (len(x) < 2):
            return True
        front = 0
        end = len(x) - 1
        while (front < end):
            if (x[front] != x[end]):
                return False
            front += 1
            end -= 1
        return True